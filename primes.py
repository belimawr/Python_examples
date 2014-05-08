'''Function to print prime numbers

This function prints the first n prime numbers'''
import math


def first_n_primes(n):
    '''Prints the first n prime numbers'''
    may_be_prime = 2
    counter = 0
    while(counter != n):
        prime_number = True
        for divisor in xrange(2, int(math.sqrt(may_be_prime))+1):
            if(may_be_prime % divisor == 0):
                prime_number = False
                break
        if(prime_number):
            print(may_be_prime)
            counter += 1
        may_be_prime += 1
