a, b = map(int, input().split())
c = a * b
if c % 2 == 0:
    print('Even')
elif c % 2 != 0:
    print('Odd')