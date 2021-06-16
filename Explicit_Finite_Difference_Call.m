clear
clc

r=0.06;
sigma=0.2;
T=2;
K=40;
t=0.01;
period=T/t+1;
q=0;
stock=60:-2:0;
n=length(stock);


%======================================
%        Explicit Finite Method
%======================================
option=zeros(n,period+1);
for j=0:n-1
    a(j+1)=(1/(1+r*t))*(-0.5*(r-q)*j*t+0.5*sigma^2*j^2*t);
    b(j+1)=(1/(1+r*t))*(1-sigma^2*j^2*t);
    c(j+1)=(1/(1+r*t))*(0.5*(r-q)*j*t+0.5*sigma^2*j^2*t);
    option(j+1,period+1)=max(stock(j+1)-K,0);
end

matrix=zeros(n,n);
for i=1:n
    matrix(i,i)=b(n+1-i);
end
 for i=1:n-1
    matrix(i,i+1)=a(n+1-i);
    matrix(i+1,i)=c(n-i);
 end

for i=1:period
option(:,period+1-i)=matrix*option(:,period+2-i);
tem(:,period+1-i)=max(stock-K,0)';
option(:,period+1-i)=max(option(:,period+1-i),tem(:,period+1-i));
end
[stock' option(:,1)]

