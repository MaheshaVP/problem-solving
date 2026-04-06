#add two lists using map function

l1 = [1,2,3,4,5,6]
l2 = [5,6,7,8,9,5]
print(l1)
print(l2)
print("Original list")

result = map(lambda x,y:x+y,l1,l2)
result = list(result)
print(result)