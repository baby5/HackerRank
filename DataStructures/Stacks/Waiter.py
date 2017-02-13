#coding:utf-8
import math

def judge_prime(num):
    for i in xrange(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True 

def get_primes(amount):
    primes = []
    p = 1
    for _ in xrange(amount):
        while 1:
            p += 1
            if judge_prime(p):
                primes.append(p)
                break
    return primes

N, Q = map(int, raw_input().split())
n_stack = map(int, raw_input().split())

for p in get_primes(Q):
    a_stack = []
    b_stack = []
    while n_stack:
        n = n_stack.pop()
        if n % p == 0:
            a_stack.append(n)
        else:
            b_stack.append(n)

    while a_stack:
        print a_stack.pop()
    n_stack = b_stack

while n_stack:
    print n_stack.pop()
