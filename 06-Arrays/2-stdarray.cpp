#include <iostream>
#include <array>

int main(int argc, char **argv)
{
  const int N = 2150000;

  //Declare the array as any other variable, specifying type and number of entries
  std::array<int, N> array {0};

  //Standard functions on arrays
  data.resize(N);
  std::cout << "Size of the array: " << data.size() << "\n";
  std::cout << data.max_size() << "\n";

  int ii = 0;
  for (auto & val : data) {
      val = 2*ii + 1;
      ii++;
  }

  double sum = 0.0;
  for (auto val : data) {
    sum += val;
  }
  std::cout << "avg: " << sum/N << "\n";

  return 0;
}
