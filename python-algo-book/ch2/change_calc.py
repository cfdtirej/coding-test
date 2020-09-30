import sys

input_price = input('Insert: ')
if not input_price.isdecimal():
    print(f"{input_price} is not integer.")
    sys.exit()

product_price = input('product: ')
if not product_price.isdecimal():
    print(f"{product_price} is not integer.")
    sys.exit()

change = int(input_price) - int(product_price)

if change < 0:
    print("Not enough money")
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(f"{i}: {r}")