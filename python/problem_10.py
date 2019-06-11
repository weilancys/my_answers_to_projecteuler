"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import threading
from queue import Queue

sum = 0

def make_queue():
    queue = Queue()
    for i in range(2, 2000001):
        queue.put(i)
    return queue

def is_prime_number(number):
    if number == 2:
        return True
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True

def thread_worker(number, lock):
    global sum
    if is_prime_number(number):
        with lock:
            sum += number


def find_sum_of_all_primes_below_two_million():
    queue = make_queue()
    lock = threading.Lock()

    while not queue.empty():
        t = threading.Thread(target=thread_worker, args=(queue.get(), lock))
        t.start()

    return sum

if __name__ == "__main__":
    sum = find_sum_of_all_primes_below_two_million()
    print("The sum of all primes below two million is", sum)