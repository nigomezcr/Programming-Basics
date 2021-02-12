#include<iostream>

int main(void)
{

  int x = 5;

  std::cout << "Value of var: " << x << "\n";
  std::cout << "Address of var: " << &x << "\n";
  std::cout << "Value at address of var: " << *&x << "\n";

  int *ptr = &x; //int pointer
  int *ptr = 0; //null pointer

  std::cout << "Value of ptr to x : " << ptr << "\n";
  std::cout << "Value stored where ptr is pointing: " << *ptr << "\n";

  std::cout << "///Changing ptr valua also changes var value///" << '\n';
  *ptr = 7; // *ptr is the same as value, which is assigned 7

  std::cout << "New value of var: "<< x << '\n'; // prints 7


  return 0;
}
