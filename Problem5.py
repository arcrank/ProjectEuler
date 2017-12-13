"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

'''
for i in range(2520,10000000000):
    if i%2==0 and i%3 ==0 and i%4 ==0 & i%5 ==0 & i%6 ==0 & i%7 ==0 & i%8 ==0 & i%9 ==0 & i%10 ==0 & i%11 ==0 & i%12 ==0 & i%13 ==0 & i%14 ==0 & i%15 ==0 & i%16 ==0 & i%17 ==0 & i%18 ==0 & i%19 ==0 & i%20 ==0:
        print(i)
        break
'''
g = list(range(2,20))

print(g)
i = 5000
ads= True
while ads:
    for j in g:
        if i%j != 0:
            i += 20
            break
        print(i,"is divisible by ",j)
        if j == g[-1]:
            print(i)
            ads = False

