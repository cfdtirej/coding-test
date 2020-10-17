# 白昼夢
# 'dreamer'と'erase'の'er'が重なってしまうため'eraser','erase','dreamer','dream'の順で置換しないといけない
s = input().replace('eraser','').replace('erase','').replace('dreamer','').replace('dream','')
if s == '':
    print('YES')
else:
    print('NO')
