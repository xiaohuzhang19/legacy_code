#ifndef TIMESERIESDATA_H
#define TIMESERIESDATA_H
#include<iostream>
#include <vector>
using namespace std;

class Timeseriesdata
{

private:
  vector <double> Data;

public:
  Timeseriesdata(void);//default constructor
  Timeseriesdata(double* dataarray, int n);
  ~Timeseriesdata();
  void addnewdataitem(double dataitem);
  int getDatasize(void) const;
  double* getData() const;//
  double getDataitem(int data_index) const;

  Timeseriesdata* getndataiterms(int n) const;/* if the member function doesn't change the object, it must be declare as const*/
  Timeseriesdata* getdatasegment(int start, int n) const;
  Timeseriesdata* getmovingaverage(int n,int m);
  Timeseriesdata& operator+=(const double& data);/*same like stl string::operator+=*/
  friend ostream& operator<<(ostream&os,Timeseriesdata &td);

};

#endif
