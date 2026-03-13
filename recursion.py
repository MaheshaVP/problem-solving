#recursion example of count down
#the function call itself

def countdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

num = int(input("Enter a number" + " "))
countdown(num)