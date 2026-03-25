#shopping cart using list

fruits = []
prices = []
total = 0

while True:
    fruit = input("Enter the fruits (q for quit): ")
    if fruit.lower() == 'q':
        break
    else:
        price = int(input("Enter the price of above fruit : "))
        fruits.append(fruit)
        prices.append(price)

print("-----your cart-----")

for fruit in fruits:
    print(fruit)

for price in prices:
    total += price

print(f"Your bill is : {total}")
print("Happy shopping")


