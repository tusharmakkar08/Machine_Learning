function [] = fun()

t = [0:0.01:50*pi]; 
r = 3*sin(t) + cos(2*t) - 2*sin(3*t) + 0.2*cos(10*t) - sin(2*t);

w = linspace(-11,11,length(t));
Yw = conFT(r,t,w);  

figure
subplot(2,1,1), plot(w,abs(Yw)), title('|Y(w)| Fou.Tr.');
subplot(2,1,2), plot(w,angle(Yw)), title('angle(Y(w)) Fou.Tr.');
figure
subplot(2,1,1), stem(w,abs(Yw)), title('|Y(w)| Fou.Tr.');
subplot(2,1,2), stem(w,angle(Yw)), title('angle(Y(w)) Fou.Tr.');


yw = InvCTFT(Yw,t,w);

figure
subplot(2,1,1), plot(t,r), title('r(t) Fou.Tr. Original Signal');
subplot(2,1,2), plot(t,yw), title('yc(t) Fou.Tr. Reconstructed Signal');


figure
subplot(2,1,1), stem(t,r), title('r(t) Fou.Tr. Original Signal');
subplot(2,1,2), stem(t,yw), title('yc(t) Fou.Tr. Reconstructed Signal');

y = r.*exp(-2i*t);

figure
plot(real(Yw),imag(Yw)), grid on, title('Y(w)');
stem(real(Yw),imag(Yw)), grid on, title('Y(w)');

figure
plot(real(y),imag(y)), grid on;
stem(real(y),imag(y)), grid on;
end

function [Y] = conFT(y,t,w)
dt = t(2) - t(1);
j=1;
Y = [];
for i=w
     Y(j) = sum(y.*exp(-1i*i.*t)*dt);
     j = j+1;
end
end

function [y] = InvCTFT(Y,t,w)
dw = w(2) - w(1);
j=1;
y = [];
for i=t
     y(j) = (1/(2*pi))*sum(Y.*exp(1i*i.*w)*dw);
     j = j+1;
end
end
