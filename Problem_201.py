"""
S is set of {1,4,9,16,..10000}

there are nCr(100,50) subsets -- 100891344545564193334812497256

realize that of these, each element will occur in half of those, so instead of trying to iterate through subsets,
just find sum of all elements times amount of times they occur



"""
S = [i**2 for i in range(1,101)]


k = 50

sums = dict()
for i in range(k):
    sums += [{}]

for s in S:
    for j in range(k-1,-1,-1):
        L = sums[j].keys()
        for s0 in L:
            s1 = s + s0
            if sums[j][s0] == 2 or s1 in sums[j+1]:
                sums[j+1][s1] = 2
            else:
                sums[j+1][s1] = 1

print(sum(i for i in sums[k] if sums[k][i] == 1))

