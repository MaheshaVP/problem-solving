#find the largest number in the list

#using max function
# list = [12,31,42,51,28]
# largest = max(list)
# print("larget is : ",largest)


#using sort
# list = [12,31,42,51,123,15,28]
# list.sort()
# print("largest number is :",list[-1])

#using logic
list = [12,31,358,2170,42,51,123,15,28]

largest = list[0]

for num in list:
    if num > largest:
        largest = num

print("Largest number in the list is :",largest)