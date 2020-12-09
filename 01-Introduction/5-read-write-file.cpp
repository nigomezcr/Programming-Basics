// Program in c++ to read from and write to a file

#include <iostream> // to write and read from standard library 
#include <cmath> // to include mathematical functions such as sqrt, sin, cos, etc
#include <fstream>  //to read from and write to a file
#include <string>

int main(void)
{
  std::fstream fin;
  std::fstream fout;
  fin.open("file.csv"); //Open files
  fout.open("file.txt", std::ios::app);
  
  //Declare local variables
  std::string str;
  double n;

  //Assign values from file to local variables
  fin >> str >> n;

  fout << str << "\t" << std::sin(n) << "\n";
  
  fin.close(); //Close files
  fout.close();
  return 0;
}
