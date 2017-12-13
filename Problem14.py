

def iterSeq(n):
    count = 0
    while n != 1:
        count +=1
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
    return count
n = 1000000

print("n is {}".format(n))





countArray =[0]*1000000

for i in range(1,1000000):

    countArray[i] = iterSeq(i)
    if i == 837799:
        print(countArray[i])

print(countArray)
print(max(countArray))
print(countArray.index(max(countArray)))
print(countArray[837799])