# Kagami Mochi

N = int(input())
d = sorted([int(input()) for _ in range(N)], reverse=True)

cnt = 0
size = 0
for i in d:
    if cnt == 0:
        cnt += 1
        size = i
    elif size > i:
        cnt += 1
        size = i
print(cnt)

