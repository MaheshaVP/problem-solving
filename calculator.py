#calculator

num1 = float(input("Enter num 1 : "))
num2 = float(input("Enter num 2 : "))
operator = input("Enter the operator (+,-,*,/) :")

if operator == '+':
    result = num1 + num2
    print(round(result,3))
elif operator == '-':
    result = num1 - num2
    print(round(result,3))
elif operator == '*':
    result = num1 * num2
    print(round(result,3))
elif operator == '/':
    result = num1 / num2
    print(round(result,3))
else:
    print(f"{operator} is not a valid operator")
    print("Please enter a valid operator ")


    