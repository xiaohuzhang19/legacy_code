function [lemda]= hazard_rate(sprd)
%% load data
% clc
% clear
% format long
%sprd=[61.5,133.1,212.12,217.7,224.7];% 1 3 5 7 10 from bloomberg citi group
sprd=sprd./10000;
rf=0.005;%at first stage assume const rf 
r=0.4;%recovery
 t=(0.25:0.25:10);%quarterly r
n=length(t);
%dicf=zeros(n,1);%discount fatcor
for i=1:n
  dicf(i)=(1+rf)^(-t(i));
end
%lemda for 1 3 5 7 10
%% solve for the 1yr hazard
for j=1:40
    X(j)=exp(-j/4);
    Y(j)=exp(-(j-1)/4);
end
df1=dicf(1:4);
x1=X(1:4);
y1=Y(1:4);
th=@(lem1)(abs(...
    ((1-r)*df1*transpose(-x1.^lem1+y1.^lem1))...
    -sprd(1)*...
    (df1*transpose((1/4)*(x1.^lem1)))...
    ));
bnd=0.0523;%Searching for between boundary 0 to bnd [0 0.0523]
%bnd=sprd(3);
lem1=fminbnd(th,0,bnd);

%% solver for three year lemda
df3=dicf(5:12);% for 2 and 3 yr
X3=X(5:12);
Y3=Y(5:12);
Numer1=(1-r)*df1*transpose(-x1.^lem1+y1.^lem1);
Denom1=df1*transpose((1/4)*(x1.^lem1));
th=@(lem3)(abs(...
    (Numer1+(1-r)*df3*transpose(-X3.^lem3+Y3.^lem3))...
    -sprd(2)*...
    (Denom1+df3*transpose((1/4)*(X3.^lem3)))...
   ));
lem3=fminbnd(th,0,bnd);

%% solve for the 5 yr lemda
df5=dicf(13:20);%for 4 and 5 yr
X5=X(13:20);
Y5=Y(13:20);
Numer3=Numer1+(1-r)*df3*transpose(-X3.^lem3+Y3.^lem3);
Denom3=Denom1+df3*transpose((1/4)*(X3.^lem3));
th=@(lem5)(abs(...
(Numer3+(1-r)*df5*transpose(-X5.^lem5+Y5.^lem5))...
-sprd(3)*...
(Denom3+df5*transpose(.25*(-X5.^lem5+Y5.^lem5))...
)));
%optimset('TolX',1e-12,'Display','off');
lem5=fminbnd(th,0,bnd);
%lem5=fzero(th,1);
%% solve for the 7yr lemda
df7=dicf(21:28);
X7=X(21:28);
Y7=Y(21:28);
Numer5=Numer3+(1-r)*df5*transpose(-X5.^lem5+Y5.^lem5);
Denom5=Denom3+df5*transpose((0.25)*(X5.^lem5));
th=@(lem7)(abs(...
    (Numer5+(1-r)*df7*transpose(-X7.^lem7+Y7.^lem7)...
    -sprd(4)*...
    (Denom5+df7*transpose(.25*(-X7.^lem7+Y7.^lem7))...
    ))));
lem7=fminbnd(th,0,bnd);
%% solve for 10yr lemda
df10=dicf(29:40);
X10=dicf(29:40);
Y10=dicf(29:40);
Numer7=Numer5+(1-r)*df7*transpose(-X7.^lem7+Y7.^lem7);
Denom7=Denom5+df7*transpose(0.25*(X7.^lem7));
th=@(lem10)(abs(...
    (Numer7+(1-r)*df10*transpose(-X10.^abs(lem10)+Y10.^abs(lem10))...
    -sprd(5)*...
    (Denom7+df10*transpose(.25*(X10.^(abs(lem10)))...
    )))));
lem10=fminbnd(th,0,bnd);

%% lemda array and probability array
lemda=[lem1 lem3 lem5 lem7 lem10]';
% hazard_rate=lemda;
% tenor=[1 3 5 7 10];
% figure
% plot(lemda)
% title('hazard rate')
% figure
% Q=survprob(lemda,tenor);
% title('survival probability')
% figure
% plot(sprd)
% title('cds spread')


