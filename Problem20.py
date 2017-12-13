import math


number = math.factorial(99)
asString = [int(i) for i in str(number)]
print(sum(asString))