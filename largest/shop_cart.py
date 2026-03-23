#Shooping cart simple example

item = input("Enter your fav item? ")
price = float(input("Enter the price? "))
quantity = int(input("Enter the quntity? "))

bill = price * quantity
print(f"The total bill is {bill}")