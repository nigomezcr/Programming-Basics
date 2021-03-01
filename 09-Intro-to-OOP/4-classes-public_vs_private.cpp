//Taken from learncpp.com
#include <iostream>

struct DateStruct // members are public by default
{
    int month; // public by default, can be accessed by anyone
    int day; // public by default, can be accessed by anyone
    int year; // public by default, can be accessed by anyone
};

class DateClassPrivate // members are private by default
{
    int m_month; // private by default, can only be accessed by other members
    int m_day; // private by default, can only be accessed by other members
    int m_year; // private by default, can only be accessed by other members

public:
    void setDate(int month, int day, int year) // public, can be accessed by anyone
    {
        // setDate() can access the private members of the class because it is a member of the class itself
        m_month = month;
        m_day = day;
        m_year = year;
    }

    void print() // public, can be accessed by anyone
    {
        std::cout << m_month << '/' << m_day << '/' << m_year << "\n";
    }
};

class DateClassPublic
{
public: // note use of public keyword here, and the colon
    int m_month; // public, can be accessed by anyone
    int m_day; // public, can be accessed by anyone
    int m_year; // public, can be accessed by anyone
};


int main(int argc, char **argv)
{
  DateStruct Today;
  Today.month = 10;    //ok
  Today.day = 14;      //ok
  Today.year= 2020;    //ok
/*
  DateClassPrivate Tomorrow;
  Tomorrow.m_month = 10;  // error
  Tomorrow.m_day = 15;    // error
  Tomorrow.m_year = 2020; // error
*/
  DateClassPublic Tomorrow;
  Tomorrow.m_month = 10;  // ok because they are public
  Tomorrow.m_day = 15;    // ok because they are public
  Tomorrow.m_year = 2020; // ok because they are public

  DateClassPrivate Yesterday;
  Yesterday.setDate(10, 14, 2020); // okay, because setDate() is public
  Yesterday.print(); // okay, because print() is public

  return 0;
}
