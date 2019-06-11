"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def is_prime_number(number):
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_sum_of_all_primes_below_two_million():
    sum = 0
    for i in range(2, 2000001):
        if is_prime_number(i):
            sum += i 
    return sum

if __name__ == "__main__":
    sum = find_sum_of_all_primes_below_two_million()
    print("The sum of all primes below two million is", sum)