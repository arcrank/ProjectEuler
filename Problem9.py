import math

squares = [i**2 for i in range(1,1000)]

print(squares)

for i in squares:
    for j in squares:
        if i != j:
            temp = i+j
            if temp in squares:

                if math.sqrt(i)+math.sqrt(j)+math.sqrt(temp) == 1000:
                    print(math.sqrt(i),math.sqrt(j),math.sqrt(temp))
                    print(math.sqrt(i)*math.sqrt(j)*math.sqrt(temp))