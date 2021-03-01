#include <iostream>

struct Fractional {
    // by default, structs use public:
    int numerator {0};
    int denominator {1};
	};


void print(const Fractional  m);

Fractional plus(const Fractional & f1, const Fractional & f2);
Fractional minus(const Fractional & f1, const Fractional & f2);
Fractional mult(const Fractional & f1, const Fractional & f2);
Fractional div(const Fractional & f1, const Fractional & f2);


int main(int argc, char **argv) {

    //Declare Fractionsl objetcs
    Fractional f, g {2, 3};

    // access internal variables: write
    f.numerator = 4; // public access
    f.denominator = 7;       // public access

    print(f);
    print(g);


    // operator overloading
    Fractional h;

    h = plus(f, g); //h = f+g;
    print(h);

    h = minus(f, g); //h = f-g;
    print(h);
    h = mult(f, g);  //h = f*g;
    print(h);
    h = div(f, g);   //h = f/g;
    print(h);

    return 0;
}

void print(const Fractional  m)
{
    std::cout << "( " << m.numerator << " / " << m.denominator << " )\n";
}

// a/b + c/d = (ad + bc)/(bd)
Fractional plus(const Fractional & f1, const Fractional & f2)
{
    Fractional result;
    result.numerator = f1.numerator*f2.denominator + f2.numerator*f1.denominator;
    result.denominator = f1.denominator*f2.denominator;
    return result;
}

// a/b - c/d = (ad - bc)/(bd)
Fractional minus(const Fractional & f1, const Fractional & f2)
{

    Fractional result;
    result.numerator = f1.numerator*f2.denominator - f2.numerator*f1.denominator;
    result.denominator = f1.denominator*f2.denominator;
    return result;
}

// a/b * c/d = (ac)/(bd)
Fractional mult(const Fractional & f1, const Fractional & f2)
{
    Fractional result;
    result.numerator = f1.numerator*f2.numerator;
    result.denominator = f1.denominator*f2.denominator;
    return result;
}

Fractional div(const Fractional & f1, const Fractional & f2)
{
    Fractional result;
    result.numerator = f1.numerator*f2.denominator;
    result.denominator = f1.denominator*f2.numerator;
    return result;
}
