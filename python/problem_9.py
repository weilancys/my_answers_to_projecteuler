"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a ** 2 + b ** 2 = c ** 2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_product():
    for i in range(1, 1001):
        for j in range(1, 1001):
            for k in range(1, 1001):
                if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                    return i * j * k
    raise ValueError("No product found.")

if __name__ == "__main__":
    product = find_product()
    print("The product abc is", product)