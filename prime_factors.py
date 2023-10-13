# Jacob Muller, jacobmuller@ufl.edu

import random


def checkPrime(number):
    # Check for no number and fill
    if number == 0:
        number = random.randint(1, 100000)

    print("Check Prime Factor")
    print("\nNumber: " + str(number))

    # Make a list of factors. Test if 2 is the first factor because we don't need 1
    factors = dict()
    currentFactor = 2

    while number > 1:

        # Try the current factor as many times as it appears
        # Add it to the dict if it does appear, and increment the number of times
        while number % currentFactor == 0:
            factors[currentFactor] = factors.get(currentFactor, 0) + 1
            number /= currentFactor

        # Save some time by avoiding even numbers after 2, but not necessary
        if currentFactor != 2:
            currentFactor += 2
        else:
            currentFactor += 1

    print("Factors: ")
    for factor in factors:
        print(f' {factor}^{factors[factor]}')

