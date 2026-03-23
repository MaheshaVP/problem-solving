#find the largest among three inputs

#using max function
# list = [12,20,36]
# print(max(list))

# largest = max(num1,num2,num3)
# print("largest is : ",largest)

num1 = float(input("Enter a number :"))
num2 = float(input("Enter a number :"))
num3 = float(input("Enter a number :"))

if (num1>=num2) and (num1>=num3):
    largest = num1
elif (num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3

print("largest number is : ",largest)
