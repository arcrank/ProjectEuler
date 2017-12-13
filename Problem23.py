"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

#step 1: generate list of all abundant numbers

import math


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)




abundantnumbers = []
testnumbers= list(range(1,28124))
print(testnumbers)

for i in range(3,28124):
    result = list(divisorGenerator(i))[:-1]
    if sum(result)>i:
        abundantnumbers.append(i)


print(abundantnumbers)


for i in abundantnumbers:
    try:
        testnumbers.remove(i*2)
    except:
        pass

for i in abundantnumbers:
    print(i)
    for j in abundantnumbers:
        if i+j in testnumbers:
            testnumbers.remove(i+j)

print(testnumbers)
print(sum(testnumbers))