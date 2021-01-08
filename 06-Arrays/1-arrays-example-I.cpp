#include <iostream>

int main(int argc, char **argv)
{
  const int N = 11; //Number of elements
  int data[N] {0};  //Name of the array, this initialize it with zeros

  //Fill the array
  for(int ii = 0; ii < N; ++ii) // <= N is an error
  {
    data[ii] = 2*ii + 1;
  }

  //Operate with it
  double sum = 0.0;
  for (int ii = 0; ii < N; ++ii) {
    sum += data[ii];
  }
  std::cout << "avg array 1: " << sum/N << "\n";

  //Python-like way of filling the array
  int ii = 0;
  for (auto & val : data) {
      val = 3*ii + 2;
      ii++;
  }

  sum = 0.0;
  for (auto val : data) {
    sum += val;
  }
  std::cout << "avg array 2: " << sum/N << "\n";

  //Use initializer list
  int data2[N]{ 1, 3, 6, 8, 21, 437}; //the rest are zeros

  sum = 0.0;
  for (auto val : data2) {
    sum += val;
  }
  std::cout << "avg array 3: " << sum/N << "\n";


  return 0;
}
