#include <iostream>
#include <vector>

typedef std::vector<int> data_t;


int main(int argc, char **argv)
{
    const int N = 81000000; // memory size: N*4 -> max 2048000
    data_t data(N);
    std::cout << data[0] << std::endl;

    // create a new block of size N/2
    data.resize(N/2);

    // copy the N/2 old elementscopiar in the new block
    data.reserve(1000);

    // free memory of the olf block
    data.push_back(1);
    data.push_back(10);

    // ... 998
    data.push_back(20);
    // pedir nueva memoria // 2*1000 = 2000
    // copiar los datos viejos en la nueva memoria
    // liberar la memoria vieja
    data.push_back(30);

    data.size(); // cuantos datos tengo guardados
    data.capacity();

    return 0;
}
