#include <iostream>
#include <vector>

typedef std::vector<double> DataT;

void fill(DataT & data, const int sizex, const int sizey);
void print(const DataT & data, const int sizex, const int sizey);
void transpose(DataT & data, DataT & dataT, const int sizex, const int sizey);
double trace(const DataT & data, const int sizex, const int sizey);

int main(int argc , char **argv)
{
    const int M = 5; // rows
    const int N = 5; // columns

    // declare variables and matrix
    DataT matrix(M*N, 0.0);

    fill(matrix, M, N);

    DataT matrixT(N*M, 0.0);
    transpose(matrix, matrixT, M, N);

    print(matrix, M, N);

    std::cout << trace(matrix, M, N) << "\n";
    std::cout << trace(matrixT, N, M) << "\n";

    return 0;
}

void fill(DataT & data, const int sizex, const int sizey)
{
    for (int ix = 0; ix < sizex; ++ix) {
        for (int iy = 0; iy < sizey; ++iy) {
            // data[ix][iy] = ix*sizey + iy;
            data[ix*sizey + iy] = ix*sizey + iy;
        }
    }
}

void print(const DataT & data, const int sizex, const int sizey)
{
    for (int ix = 0; ix < sizex; ++ix) {
        for (int iy = 0; iy < sizey; ++iy) {
            std::cout << data[ix*sizey + iy] << "  ";
        }
        std::cout << "\n";
    }
}

void transpose(DataT & data, DataT & dataT, const int sizex, const int sizey)
{
   for (int ix = 0; ix < sizex; ++ix) {
       for (int iy = 0; iy < sizey; ++iy) {
           dataT[iy*sizex + ix] = data[ix*sizey + iy];
       }
    }
}

double trace(const DataT & data, const int sizex, const int sizey)
{
    double sum = 0.0;
    for (int ix = 0; ix < sizex; ++ix) {
        sum += data[ix*sizey + ix]; // [ix][ix]
    }

    return sum;
}
