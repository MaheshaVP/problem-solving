#check a number prime or not

n = int(input("Enter a number : "))

def check_prime(number):
    if number > 1:
        for num in range(2, number):
            if number%num == 0:
                return f"{number} not prime"
        return f"{number} is prime"
    return f"{number} not prime"

print(check_prime(n))