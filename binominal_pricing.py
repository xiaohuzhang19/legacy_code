'''
Created on 1.10.2014

@author: xiaohu zhang
'''

import numpy as np
from scipy.stats import norm

def normpdf(x):
    normpdf=np.exp(-x**2/2)/np.sqrt(2*3.1415926)
    return normpdf

def blackscholes(s,x,r,v,t):
    '''
    stock,strike risk free rate volatility time to maturity
    return: call delta vega(dollar vega)  gamma(dollar gamma)
    '''
    d1 = (np.log(s/x)+(r+v**2/2)*t)/(v*np.sqrt(t))
    delta=norm.cdf(d1) 
    d2=d1-np.sqrt(v*t)
    c=norm.cdf(d1)*s-x*norm.cdf(d2)*np.exp(-r*t)
    vega=norm.pdf(d1)*s*np.sqrt(t)*100
    gamma=norm.pdf(d1)/(s*v*np.sqrt(t))*100
    return delta,vega,gamma
   

   
def binominal_model(s,x,r,v,t,n):
    '''    
        stock,strike risk free rate volatility time to maturity n:steps
        return: call delta vega(dollar vega)  gamma(dollar gamma)
    '''       
    dt=t/n
    u=np.exp(v*np.sqrt(dt))
    d=1.0/u
    p=(np.exp(r*dt)-d)/(u-d)                                        # Prob
    s_t=np.zeros((n+1,n+1))
    s_t[0,0]=s
    c_t=np.zeros((n+1,n+1))                                         #n+1 by n+1 index: 0 to n
    for i in range(1,n+1):                                          #upper path     index:1 to n
        s_t[i,0]=s_t[i-1,0]*u
        for j in range(1,i+1):                                      #down path      index 1 to i
            s_t[i,j]=s_t[i-1,j-1]*d
    #assume EU style option
    for i in range(n+1):                                            #index 0 to n
        c_t[n,i]=max(s_t[n,i]-x,0)                                  #compare with terminal node
    
    #backward induction
    for i in range(n-1,-1,-1):                                      #last begin increment
        for j in range(i+1):
            c_t[i,j]=np.exp(-r*dt)*(p*c_t[i+1,j] + (1-p)*c_t[i+1,j+1])
    #Greeks letters
    call_price=c_t[0,0]
    delta=(c_t[1,0]-c_t[1,1])/(s_t[1,0]-s_t[1,1])
    deltaup=(c_t[2,0]-c_t[2,1])/(s_t[2,0]-s_t[2,1])
    deltadown=(c_t[2,1]-c_t[2,2])/(s_t[2,1]-s_t[2,2])
    gamma=(deltaup-deltadown)/(0.5*(s_t[2,0]-s_t[2,2]))*100             #dollar gamma=100*(delta_up-delta_down)/(0.5*(s_uu-s_dd))
    return delta,gamma,call_price
        
def vega_binomial(s,x,r,v,t,n):
    vup=v+0.01
    vdown=v-0.01
    c=binominal_model(s,x,r,vup,t,n)
    c_vup=c[2]
    c=binominal_model(s,x,r,vdown,t,n)
    c_vdown=c[2]
    vega=100*(c_vup-c_vdown)/0.02                                       #dollar vega= [c(v_up)-c(v_down)/(2*0.01)] *100
    return vega
    
if __name__ == "__main__":    
    param=np.zeros(3)
    param_binomial=np.zeros(3)
    param=blackscholes(80.0,100.0,0.05,0.15,0.5)
    param_binomial=binominal_model(80.0,100.0,0.05,0.15,0.5,250)
    vega=vega_binomial(80.0,100.0,0.05,0.15,0.5,250)
    print("Black Scholes Delta Vega Gamma is ",param)
    print ("binomial Delta is" ,param_binomial[0])
    print("binomial Vega is", vega)
    print("binomial Gamma is", param_binomial[1])
    
    