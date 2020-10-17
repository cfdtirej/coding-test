import math

n = int(input())
x = list(map(int,input().split()))

manhattan = 0
euclid = 0
cheby = []

for i in x:
    manhattan += abs(i)
    euclid += abs(i) ** 2
    cheby.append(abs(i))

print(manhattan)
print(math.sqrt(euclid))
print(max(cheby))



