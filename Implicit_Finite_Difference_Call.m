clear
clc

%======================================
%            Set the Parameters
%          of European Call Option
%=======================================

% r is the risk free interest rate
% q is the yield
% sigma is the annualized volatility
% T is maturity
% K is the strike price
% t is the times step

r=0.06;
q=0;
sigma=0.4;
T=1;
K=40;
t=0.01;
stock=60:-2:0;
% r=0.1;
% sigma=0.4;
% T=5/12;
% K=50;
% t=0.5/12;

%==============================================
%              Implicit Finite Method
%==============================================
period=round(T/t);
n=length(stock);
option=zeros(n,period+1);
for j=0:n-1
    a(j+1)=0.5*(r-q)*j*t-0.5*sigma^2*j^2*t;
    b(j+1)=1+sigma^2*j^2*t+r*t;
    c(j+1)=-0.5*(r-q)*j*t-0.5*sigma^2*j^2*t;
    option(j+1,period+1)=max(stock(j+1)-K,0);
%     option(j+1,period+1)=max(K-stock(j+1),0);
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
option(:,period+1-i)=inv(matrix)*option(:,period+2-i);
% tem(:,period+1-i)=max(K-stock,0)';
tem(:,period+1-i)=max(stock-K,0)';
option(:,period+1-i)=max(option(:,period+1-i),tem(:,period+1-i));
end

%========================
%     Outputs
%========================
[stock' option(:,1)]

