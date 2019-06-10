"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# A prime number has only ONE factor which is itself.
# The largest prime factor of a number is the quotient of dividing the number by a smallest number.

NUMBER = 600851475143

def is_prime_number(number):
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_largest_prime_factor():
    global NUMBER
    for i in range(2, NUMBER):
        if NUMBER % i == 0 and is_prime_number(NUMBER // i):
            return NUMBER // i

if __name__ == "__main__":
    largest = find_largest_prime_factor()
    print("The answer is", largest)
