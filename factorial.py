#factorial of a number

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)
    
number = int(input("Enter a number "))
result = factorial(number)
print(result)