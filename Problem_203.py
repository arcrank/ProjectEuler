import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

all = []
for i in range(0,51):
    level = []

    for r in range(0,i+1):

        level.append(nCr(i,r))
        all.append(nCr(i,r))




rall = set(all)

squarefree = []
for i in rall:
    output = True

    for j in range(2,int(math.sqrt(i))+1):

        ja = j*j
        if i % ja == 0:
            output = False




    if output == True:

        squarefree.append(i)


sq = set(squarefree)
print(sum(sq))