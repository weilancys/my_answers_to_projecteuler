"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_evenly_divisible_from_1_to_20(number):
    for divisor in range(1, 21):
        if number % divisor != 0:
            return False
    return True

def find_smallest_number_evenly_divisible_from_1_to_20():
    number = 1
    while True:
        if is_evenly_divisible_from_1_to_20(number):
            return number
        number += 1


if __name__ == "__main__":
    smallest = find_smallest_number_evenly_divisible_from_1_to_20()
    print("The smallest positive number evenly divisible by all of the numbers from 1 to 20 is", smallest)