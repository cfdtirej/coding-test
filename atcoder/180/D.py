x, y, a, b = map(int,input().split())

exp = 0
while True:
    if (x * a >= y) or (x + b >= y):
        break
    if x * a < x + b:
        x *= a
        exp += 1
    elif x + b < x * a:
        x += b
        exp += 1
    else:
        x += b
        exp += 1
print(exp)
