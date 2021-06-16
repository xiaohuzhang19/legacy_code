
//      h1q3.cpp
//      C++
//      Copyright 2012 Xiaohu Zhang 
//      ID:A09364980   Financial Programing



#include <stdio.h>
#include <sys/time.h>//or can use <ctime>
#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;
//call the library, call the function get time today(gettimeofday)


int main()
{
	//To ensure this program can generate different number every time
	// we must use the system time to ensure different start time
	//use time as seed since time has randomness properity 
  int i;
  int n=1000000;
  float a[n];

  struct timeval startTime;
  struct timeval endTime;
  //get the starting time
      gettimeofday(&startTime, NULL);
      //random number geneartor
         srand((time(0)));       //seed a (0,1) random number)
         //if change the scope, we can use srand((time(NULL)));
        float sum=0;

         for(i=0;i<n;i++)
         {
         
          a[i] = rand()%2;  //key to generat the random number
//generate random number from 0 to 1, if generate number in other scope ,you can use 
//a[i]=rand();
             sum=sum+a[i];
             //cout<<a[i]<<endl;
             

}
//find the scope of the random number
float max,min;
max=a[0];//intalize the max value at o
min=a[0];//intalize the miniunm the value
 
for( i=0; i<n; i++){
if(a[i]>max){
max=a[i];//store a(i) as maxium number
}
if(a[i]<min){
min=a[i];
}
}

   float av;
// calculate the mean
av=sum/n;// av means average
   float diff,vari;

// calculate the variance 
float sigma,sigmacube,sigmah,skwn;

for(i=0;i<n;i++)
{
	

diff+=(a[i]-av)*(a[i]-av);//variance (x-avg(x))^2/n

}
vari=diff/n;
//calculate the skewness
sigma=sqrt(vari);
for(i=0;i<n;i++)
{

sigmah+=(a[i]-av)*(a[i]-av)*(a[i]-av);
}

sigmacube=pow(sigma,3);//get the denominator
skwn=sigmah/n/sigmacube;
 	cout<<"The upper bound of random number is:\n"<<max<<endl;
 	cout<<"The lower bound of random number is:\n"<<min<<endl;
  cout << "Mean:\n" <<av<< endl;
  cout <<"Variance:\n"<<vari<< endl;
  cout<<"Skewness:\n"<<skwn<<endl;
  
  gettimeofday(&endTime,NULL);//output the time
	double tS=startTime.tv_sec*1000000+(startTime.tv_usec);
	double tE=endTime.tv_sec*1000000+(endTime.tv_usec);
	cout<<"Time Taken: "<<tE-tS<<"  Microseconds\n";
	return 0;
  
  
}
