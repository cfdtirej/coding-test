# Card Game for Two

N = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

alice = 0
bob = 0
for idx, value in enumerate(a):
    if idx % 2 == 0:
        bob += value
    else:
        alice += value

print(bob - alice)
