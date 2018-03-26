

import math




for i in range(3,100000):
    num = [int(x) for x in str(i)]
    if i == sum([math.factorial(n) for n in num]):
        print(i)


print(145+40585)