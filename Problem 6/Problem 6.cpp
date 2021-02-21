#include <iostream>
#include <cmath>

//Find the sum of natural numbers from 1 up to and including the upper bound
int sumOfNums(int upperBound) {
    return (upperBound * (upperBound + 1)) / 2;
}

//Find the sum of the squares of natural numbers from 1 up to and including the upper bound
int sumOfSquaredNums(int upperBound) {
    return ((upperBound) * (upperBound + 1) * (2 * upperBound + 1)) / 6;
}

int main() {
    int numsSum = sumOfNums(100);
    int numsSumSquared = std::pow(numsSum, 2);

    int sumNumsSquared = sumOfSquaredNums(100);
    std::cout << (numsSumSquared - sumNumsSquared);
    return 0;
}