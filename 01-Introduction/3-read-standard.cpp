// Reading from screen in standard form
#include <iostream>
#include <string>

int main(int argc, char **argv)
{
    std::string fullname;
    std::cout << "Hi, write your full name, please:\n";
    //std::cin >> fullname; //reads only one word
    std::getline(std::cin, fullname); // reads all the line, including spaces
    std::cout << "Hi, " << fullname << "!" << std::endl;

    return 0;
}
