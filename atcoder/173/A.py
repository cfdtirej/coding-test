'''
問題文
  お店でN円の商品を買います。
  1000円札のみを使って支払いを行う時、お釣りはいくらになりますか？
  ただし、必要最小限の枚数の1000円札で支払いを行うものとします。
制約
  1≤N≤10000
  Nは整数
'''

N = int(input())
for i in range(11):
    b = i * 1000
    c = b - N
    if c >= 0:
        break
print(c)