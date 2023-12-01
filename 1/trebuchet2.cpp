#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <fstream>

void replaceAll(std::string &s, const std::string &search, const std::string &replace)
{
    size_t pos = 0;
    while ((pos = s.find(search, pos)) != std::string::npos)
    {
        s.replace(pos, search.length(), replace);
        pos += replace.length();
    }
}

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

        replaceAll(line, "zero", "z0ro");
        replaceAll(line, "one", "o1e");
        replaceAll(line, "two", "t2o");
        replaceAll(line, "three", "thr3e");
        replaceAll(line, "four", "f4ur");
        replaceAll(line, "five", "f5ve");
        replaceAll(line, "six", "s6x");
        replaceAll(line, "seven", "se7en");
        replaceAll(line, "eight", "ei8ht");
        replaceAll(line, "nine", "n9ne");

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