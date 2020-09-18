N = int(input())
A = list(map(int, input().split()))
A = [382253568, 723152896, 37802240, 379425024, 404894720, 471526144]
div_count = []
for idx, num in enumerate(A):
    count = 0
    while num % 2 == 0:
        count += 1
        num /= 2
    div_count.append(count)
print(min(div_count))


    