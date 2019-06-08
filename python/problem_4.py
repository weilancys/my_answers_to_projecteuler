"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

from math import ceil

def is_palindromic_number(number):
    """
    A number is determined as palindromic or not by comparing its corresponding digits at both ends.
    Index for corresponding digits are "index <=> length - index - 1".
    Looping should start from index 0 through index of the middle, which is "ceil(len(number_str) / 2) - 1".
    """
    
    number_str = str(number)
    LENGTH = len(number_str)
    MIDDLE_INDEX = ceil(len(number_str) / 2) - 1

    for index in range(MIDDLE_INDEX + 1):
        opposite_index = LENGTH - index - 1
        if number_str[index] != number_str[opposite_index]:
            return False
        
    return True


def find_largest_palindromic_number():
    """
    Find possible palindromic_numbers and return the largest one.
    """
    palindromic_numbers = set()

    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if is_palindromic_number(product):
                palindromic_numbers.add(product)
    
    return max(palindromic_numbers)


if __name__ == "__main__":
    largest = find_largest_palindromic_number()
    print("The largest palindromic number is", largest)