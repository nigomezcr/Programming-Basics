#include <iostream>

const int a = 20;

void print_message(int a)
{
    std::cout << "Hello world!\n";
    std::cout << "Parameter a: " << a << "\n";
    std::cout << "Address of a in print: " << &a << std::endl;
}

int main(void)
{
    int a = 12;
    std::cout << "Adress of a in main: " << &a << std::endl;
    print_message(a);
    return 0;
}
