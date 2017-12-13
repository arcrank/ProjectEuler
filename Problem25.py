import itertools as it

a,b = 1,1
fibSeq = [a,b]
count = 2
while len(str(b)) < 1000:
    a,b = b,a+b


    fibSeq.append(b)
    count += 1
    if (len(str(b)) > 999):
        print(b)
        print(count)
        break



print(b)
print(len(str(b)))
print(count)