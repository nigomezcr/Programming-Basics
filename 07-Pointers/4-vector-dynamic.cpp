#include <iostream>
#include <vector>

typedef std::vector<int> data_t;


int main(int argc, char **argv)
{
    const int N = 81000000; // memory size: N*4 -> max 2048000
    data_t data(N);

    std::cout << "Size of the vector: " << data.size() << std::endl;
    //this creates a new block of size N/2
    data.resize(N/2);
    std::cout << "New size: " << data.size() << std::endl;

    //if we don't know the numbers of elements we will need for data,  we reserve some
    data.reserve(1000);

    // assing number to last element in the vector with push_back
    data.push_back(1);
    std::cout << "After push_back" << std::endl;
    std::cout << "Vector has size: " <<  data.size() << std::endl;
    std::cout << "Value of last element: " <<data[N/2] << std::endl;

    data.push_back(10);
    std::cout << "Vector has size: " <<  data.size() << std::endl;
    std::cout << "Value of last element: " <<data[N/2+1] << std::endl;


    return 0;
}
