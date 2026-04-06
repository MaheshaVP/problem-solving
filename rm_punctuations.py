#remove punctuations from the string

punctuations = "''/!@#$%^&*()_+{}<>:|,.."
mystr = input("Enter the string : ")
new_str = " "

for x in mystr:
    if x not in punctuations:
        new_str += x

print(new_str)
