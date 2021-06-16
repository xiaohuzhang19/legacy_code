#include<iostream>
#include"timeseriesdata.h"
using namespace std;

int main(void)
{
  double dataarray[10]={1,2,3,4,5,6,7,8,9,10};
  cout<<dataarray[0]<<'\t';//<<dataarray[10];
  cout<<dataarray[9]<<endl;
    
Timeseriesdata test(dataarray,10);
//  cout<<test;

  



  return 0;
}
