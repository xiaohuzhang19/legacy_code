#include"timeseriesdata.h"

Timeseriesdata::Timeseriesdata(void)
{

}

Timeseriesdata::Timeseriesdata(double* dataarray, int n)
{
  //dataarray is a array pass data into class
  for (int i=0;i<n;i++)
    {
      Data.pushback(dataarray[i]);
     }
}


Timeseriesdata::~Timeseriesdata() {}

void Timeseriesdata::addnewdataitem(double dataitem)
{
  Data.pushback(dataitem);
}

int Timeseriesdata::getDatasize£¨£©const 
{
  return Data.size;
}

double*Timeseriesdata::getData() const
{
  int n=Data.size();
    double* dataarray=new double[n];
  for (int i=0;i<n;i++)
    dataarray[i]=Data[i];
  return dataarray;
} 
double Timeseriesdata::getDataitem(int data_index) const
{
  if(data_index<Data.size()) return Data[data_index];
  return -1;  
}

Timeseriesdata* Timeseriesdata::getndataitem(int n) const
{
  int size=Data.size();
  if(n>size) return 0;
  Timeseriesdata*td=new Timeseriesdata;
  for (int i=0;i<n;i++)
    {
      td->addnewdataitem(Data[size-i-1]);
      return td;
    }

}
