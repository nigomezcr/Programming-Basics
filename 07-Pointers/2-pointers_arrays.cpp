#include <iostream>

int main(int argc, char **argv)
{
    const int N = 5;
    int data [N] {1, 2};
    int * ptr = nullptr;

    std::cout << "Value of fist element: " <<  data[0] << std::endl;
    std::cout << "Memory address of first element: " << &data[0] << std::endl;
    std::cout << "Memory address of first element: " <<  data << std::endl;
    std::cout << "Memory address of second element: " << (data+1) << std::endl;
    std::cout << "Value of the second element: "  << *(data+1)<< std::endl;
    std::cout << "prt -> " << ptr << std::endl;

    ptr = data;
    std::cout << "prt -> " << ptr << std::endl;
    std::cout << "*(prt+1): " << *(ptr+1) << std::endl;

    // data = &N; // ERROR: data cannot point to other memory addresses

    return 0;
}
