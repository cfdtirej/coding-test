N, A, B = map(int, input().split())

count = 0
for i in range(1, N + 1):
    num = 0
    for j in list(str(i)):
        num += int(j)
    if (A <= num) and (B >= num):
        count += i

print(count)
