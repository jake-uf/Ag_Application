# Jacob Muller, jacobmuller@ufl.edu

import math
import random


def sortBuckets(numBuckets, integerList):
    print("Bucket Sort\n")

    # Check for empty list and fill if needed
    if not integerList:
        integerList = fillList(numBuckets)

    # Get integer range of highest and lowest values
    maxNum = max(integerList)

    # Time to make buckets!
    buckets = list()
    count = numBuckets
    while count > 0:
        buckets.append(list())
        count -= 1

    # Fill the buckets!
    scale = maxNum/numBuckets

    # Find the bucket to move each integer to
    for i in integerList:
        # Round UP to avoid <0
        index = math.ceil(float(i)/scale)
        # Index - 1 because the very first bucket is actually bucket #0
        buckets[index - 1].append(i)

    # Sort each bucket individually
    for bucket in buckets:
        sortBucket(bucket)

    # Recombine
    sortedList = list()
    for bucket in buckets:
        for b in bucket:
            sortedList.append(b)

    # Print statements
    print("Number of Integers:", str(len(integerList)))
    printCount = 0
    for bucket in buckets:
        printCount += 1
        print(f'Bucket # {printCount}  {bucket}')
    print(f'Original List: {integerList}')
    print(f'Sorted List: {sortedList}')


def sortBucket(bucket):
    # Insertion sort within each bucket
    for i in range(1, len(bucket)):
        number = bucket[i]
        j = i - 1

        while j >= 0 and number < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = number


# Only needed if no list is given
def fillList(numBuckets):
    integerList = list()
    # Make a list with at least as many integers as buckets
    listSize = random.randint(numBuckets, numBuckets + random.randint(0, 100))
    while listSize > 0:
        integerList.append(random.randint(0, 1000))
        listSize -= 1
    return integerList
