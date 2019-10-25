% Reference - Code taken from slides, updated myself for the given part of the question

close all
clear all
clc
%% estimation by modelling - blind deconvolution
ffull = imread('cameraman.tif');
f = (ffull(1:256,1:256));  % image to be degraded
imshow(f,[])
title('orig')
constant = .0025;
for k =0:511
    for l = 0:511
%         H(k+1,l+1) = (1/(pi*(k+l)))*sin(pi*(k+l))*exp(-1i*pi*(k+l));  % motion blur kernel
        H(k+1,l+1) = exp(-constant*(k^1+l^1)^(5/6));  %%% atmospheric turbulence
    end
end
gF = H.*fft2(f,512,512); % blurring
g = real(ifft2(gF)); %spatial domain
figure,imshow(g(1:256,1:256),[])
title('degraded image')

%% Inverse filtering in absence of noise
gdeblur = real(ifft2(fft2(g)./H)); % deblur
figure,imshow(gdeblur(1:256,1:256),[])
title('deconvolved')

%% original image for degradation
% ffull = imread('x5.bmp');
ffull = imread('cameraman.tif');
f = (ffull(1:256,1:256));  % image to be degraded
imshow(f,[])
title('orig')

%% zero padding
M = 280;N=280;
fz=zeros(M,N);hp=fz;
fz(1:256,1:256) = f;

%%  Laplacian for smothness
hp(1,1)=-8; hp(2,1)=1; hp(1,2)=1; % Center is at (1,1)
hp(M,1)=1; hp(1,N)=1; % Indices modulo P or Q
hp(M,2) = 1; hp(2,N) = 1;hp(2,2)=1;hp(M,N) = 1;
hp = hp;
%%  degradation function
hz = zeros(3);
h=[1.6 2.9 0;1.3 1 0; 0 0 0;];  
h = h./sum(sum(h));
hz(1:3,1:3) = h;  % 
% h = hz;

%% 
gconv = conv2(double(f),double(h));  % obtain degraded image using convolution  h*f
figure,imshow(gconv,[])
title('degraded without noise')

%% using fft to obtain conv
G = fft2(h,M,N).*fft2(f,M,N) ;  % extension is taken care by FFT = H.*F
gspace = real(ifft2(G,M,N)) ;
g = gspace(1:256,1:256); %% obtain the degraded image without noise
%g = mat2gray(g)*255;
%% AWGN
g = uint8(g) + uint8(30*randn(256));   % get h*f + n = HF + N
G = fft2(g,M,N);  %% FFT to get Fourier of observed image
gim = g;
figure, imshow(gim,[]) % Show observed image
title('observed')

%% 
H = fft2(h,M,N);  % FFt of impulse response/PSF
Hp = fft2(hp,M,N); %%% for constrained filtering

%% Inverse filtering in presence of noise
gdeblur = real(ifft2(fft2(gim,M,N)./H)); % deblur G./H
figure,imshow(gdeblur(1:256,1:256),[])
title('deconvolved using Inverse filtering in presence of noise ')
%% 
K =0.001:.04:4;err=zeros(1,length(K));

lap=fft2([0 -1 0; -1 4 -1; 0 -1 0],M,N)

for i = 1:length(K)
    
    %%  for Wiener
    %F = conj(H).*G./(abs(H).^2+K(i));
    F=fft2(f,M,N)./(K(i).*lap.^2 +1)
    f1 = real(ifft2(F));
    fim = f1(1:256,1:256);
    mserestore = mean(mean((fim-double(f)).^2));
    err(i) = mserestore;
    
    %% for constrained filtering
    F = conj(H).*G./(abs(H).^2+K(i)*abs(Hp).^2);
    f1 = real(ifft2(F));
    fim = f1(1:256,1:256); %5 best restored image
    mserestore = mean(mean((fim-double(f)).^2));
    errconst(i) = mserestore;
end

%% Show best restored Wiener
[val,indW] = min(err);
F = conj(H).*G./(abs(H).^2+K(indW));
f1 = real(ifft2(F));
fim = f1(1:256,1:256); %5 best restored image
figure,imshow(fim,[])
title('best Wiener restored')
snrwiener = 20*log10(255/(sqrt(min(err))));  % SNR for restored

%% Show best restored constrained
[val,ind] = min(errconst);
F = conj(H).*G./(abs(H).^2+K(ind)*abs(Hp).^2);
f1 = real(ifft2(F));
fim = f1(1:256,1:256); %5 best restored image
figure,imshow(fim,[])
title('best constrained filteirng')
snrconstrained = 20*log10(255/(sqrt(min(errconst))));  % SNR for restored

%%  Degraded image
mse = mean(mean((double(gim)-double(f)).^2));
snrdegraded = 20*log10(255/(sqrt(mse))); % SNR degraded

%% for inverse filter
F = G./H;
f1 = real(ifft2(F));
fim = f1(1:256,1:256); %5 best restored image
figure,imshow(fim,[])
title('inverse filter restored')
mse = mean(mean((fim-double(f)).^2));
snrinverse = 20*log10(255/(sqrt(mse))); % SNR restored inverse filtering

%% Matlab inbuilt
J= wiener2(gim,[5 5]);
figure, imshow(J,[])
title('Matlab Wiener restored')
mse = mean(mean((double(J)-double(f)).^2));
snrMatWien = 20*log10(255/(sqrt(mse))); % SNR restored using MAtlab Wiener2
