#find the second largest number

numbers = [10, 20, 42, 50, 30, 35, 50]

# unique = list(set(numbers))
# unique.sort()

# print(unique[-2])

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(f"Second largest number is : {second}")