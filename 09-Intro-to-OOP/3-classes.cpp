#include<iostream>

//Define the class
class Fractional
{
public:
    int m_num {0};
    int m_den {1};

    void print()
    {
        std::cout << m_num << "/" << m_den << std::endl;
    }

    Fractional operator+(const Fractional & f2);
    Fractional operator-(const Fractional & f2);
    Fractional operator*(const Fractional & f2);
    Fractional operator/(const Fractional & f2);
};

int main(int argc, char **argv)
{
    Fractional f;
    Fractional g {5,6};
    Fractional h;

    f.m_num = 8; // f = 8/1
    h = f + g;
    h.print();
    h = f - g;
    h.print();
    h = f*g;
    h.print();
    h = f/g;
    h.print();

}


Fractional Fractional::operator+(const Fractional & f2)
{
    Fractional result;
    result.m_num = m_num*f2.m_den + f2.m_num*m_den;
    result.m_den = m_den*f2.m_den;
    return result;
}


Fractional Fractional::operator-(const Fractional & f2)
{
    Fractional result;
    result.m_num = m_num*f2.m_den - f2.m_num*m_den;
    result.m_den = m_den*f2.m_den;
    return result;
}

Fractional Fractional::operator*(const Fractional & f2)
{
    Fractional result;
    result.m_num = m_num*f2.m_num;
    result.m_den = m_den*f2.m_den;
    return result;
}

Fractional Fractional::operator/(const Fractional & f2)
{
    Fractional result;
    result.m_num = m_num*f2.m_den;
    result.m_den = m_den*f2.m_num;
    return result;
}
