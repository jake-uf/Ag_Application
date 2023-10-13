# Jacob Muller, jacobmuller@ufl.edu

import prime_factors
import headline
import bucket_sort

# Settings

# If 0, it will pick a random number
primeNumber = 0

# Bucket sorts. If integers list is empty, will generate a random list with numbers between 1 and 10000.
numBuckets = 5
integers = {}

if __name__ == '__main__':
    print("===================---===================")
    prime_factors.checkPrime(primeNumber)
    print("===================---===================")
    bucket_sort.sortBuckets(numBuckets, integers)
    print("===================---===================")
    headline.getHeadline()

