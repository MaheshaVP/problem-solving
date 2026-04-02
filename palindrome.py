#find the string is palindrome or not

print("Program to check Palindrome or not")
s = input("Enter the string : ")


def palindrome(text):
    if text==text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome") 
    
palindrome(s)
