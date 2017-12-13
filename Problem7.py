import math


#Define Sieve to ballpark
def sievePrimes(number):
    primeNumbers = int(number*2*math.log(number))
    sieve = [True]*primeNumbers
    count = 0



    for i in range(2,primeNumbers):
        if sieve[i]:
            count +=1
            if count == number:
                return i
            for j in range(2*i,primeNumbers,i):
                sieve[j] = False


primeTest = sievePrimes(10001)



print(primeTest)