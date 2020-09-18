N = int(input())
A = list(map(int, input().split()))
div_count = []
for idx, num in enumerate(A):
    count = 0
    while num % 2 == 0:
        count += 1
        num /= 2
    div_count.append(count)
print(min(div_count))


    