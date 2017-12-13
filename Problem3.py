#The prime factors of 13195 are 5, 7, 13 and 29.
import math
#What is the largest prime factor of the number 600851475143 ?


targetNumber = 600851475143
maxPrimeFactor = 1
listOfFactors = []


for i in range(3,math.floor(math.sqrt(targetNumber)),2):


    while(targetNumber%i == 0):

        targetNumber = targetNumber/i
        listOfFactors.append(i)

print(listOfFactors[-1])

