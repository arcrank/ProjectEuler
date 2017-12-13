import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


print(220+284+1184+1210+2620+2924)

nums = [0]*10000

for i in range(10000):

    nums[i] =sum(list(divisorGenerator(i))[:-1])

print(sum(list(divisorGenerator(220))[:-1]))



for index,i in enumerate(nums):
    if i == 0 or nums[i] == i:
        continue
    print(i)
    if nums[i] == index:
        print("found a match, nums {} and {}".format(nums[i],i))

print(220+284+1184+1210+2620+2924)
print(nums[220],nums[284])

