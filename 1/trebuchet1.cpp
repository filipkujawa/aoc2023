#include <iostream>
#include <fstream>
#include <string>
#include <fstream>

int main()
{
    std::ifstream inputFile("input.txt");
    if (!inputFile)
    {
        std::cerr << "Failed to open input file." << std::endl;
        return 1;
    }

    int sum = 0;
    std::string line;
    while (std::getline(inputFile, line))
    {

        std::string first_digit = "";
        std::string last_digit = "";
        for (int i = 0; i < line.length(); i++)
        {
            if (isdigit(line[i]))
            {
                if (first_digit.empty())
                {
                    first_digit += line[i];
                    last_digit += line[i];
                }
                else
                {
                    last_digit = "";
                    last_digit += line[i];
                }
            }
        }

        std::string l = first_digit + last_digit;
        int li = std::stoi(l);

        sum += li;
    }

    inputFile.close();
    std::cout << "Sum: " << sum << std::endl;
    return 0;
}