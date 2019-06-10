"""
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1 squared + 2 squared + ... + 10 squared = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10) squared = 55 squared = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

MAX_NUMBER = 100

def sum_of_squared_from_1_to_max_number(max_number):
    sum = 0
    for i in range(1, max_number + 1):
        sum += i * i
    return sum

def squared_of_sum_of_from_1_to_max_number(max_number):
    sum = 0
    for i in range(1, max_number + 1):
        sum += i
    return sum * sum

if __name__ == "__main__":
    sum_of_square = sum_of_squared_from_1_to_max_number(MAX_NUMBER)
    square_of_sum = squared_of_sum_of_from_1_to_max_number(MAX_NUMBER)
    print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is", square_of_sum - sum_of_square)