#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

int main(int argc, char *argv[])
{
    std::vector<std::tuple<std::string, std::string, int, int>> network;
    std::string edge, startVertex, endVertex;
    int weight;

    std::cout << argv[1] << std::endl;
    std::ifstream in;
    in.open(argv[1]);
    while(std::getline(in, edge))
    {
        std::stringstream inputString(edge);
        std::string tempString;

        std::getline(inputString, startVertex,',');
        std::getline(inputString, endVertex,',');
        std::getline(inputString, tempString,',');
        weight = std::atoi(tempString.c_str());
        network.push_back(std::tuple<std::string, std::string, int, int>(startVertex, endVertex, weight, 0));
        std::cout << startVertex << " " << endVertex << " " << weight << std::endl;
    }
    in.close();

    return 0;
}