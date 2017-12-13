print(999*999)

i = 999
j = 999

products = []

for i in range(999):
    for j in range(999):
        products.append(i*j)

print(len(products))
#print(products)

products.sort(reverse=True)


for p in products:
    temp = str(p)
    #print(temp)
    if temp == temp[::-1]:
        print(temp)
        break



