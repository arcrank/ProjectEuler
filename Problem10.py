"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


#Lends from problem 7
import math


#Define Sieve to ballpark
def sievePrimes(number):
    primeNumbers = int(number*2*math.log(number))
    sieve = [True]*primeNumbers
    count = 0



    for i in range(2,primeNumbers):
        if i > 2000000:
            break
        if sieve[i]:
            count += i
            print("found prime {}, adding it to toal".format(i))
            for j in range(2*i,primeNumbers,i):
                sieve[j] = False
    return count


primeTest = sievePrimes(148934)



print(primeTest)