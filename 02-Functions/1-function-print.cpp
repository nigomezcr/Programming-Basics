//Simple function to print
#include <iostream>

void print_message(double a) //declaring and implementing function
{
    std::cout << "Hello world!\n"; 
    std::cout << "Parametro a: " << a << "\n"; 
}

int main(void)
{
    int m = 12;
    print_message(m); //calling function
    return 0;
}
