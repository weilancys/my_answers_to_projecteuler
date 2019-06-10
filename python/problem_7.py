"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

def is_prime_number(number):
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_10001st_prime():
    TARGET_INDEX = 10001
    prime_numbers = []
    n = 2
    while len(prime_numbers) < TARGET_INDEX:
        if is_prime_number(n):
            prime_numbers.append(n)
        n += 1
    return prime_numbers[TARGET_INDEX - 1]

if __name__ == "__main__":
    prime = find_10001st_prime()
    print("The 10001st prime number is", prime)