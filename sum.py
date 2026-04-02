#clculate the sum of the list

list = [1,2,3,4,5,6,7,8,9,10]


def sum_nums(list):
    total = 0

    for x in list:
        total += x
    return total

print(sum_nums(list))


# list = input("Enter the nums seperated by space : ")
# nums_list = list.split()
# nums_list = [int(i) for i in nums_list]


# def sum_nums(list):
#     total = 0

#     for x in list:
#         total += x
#     return total

# print(sum_nums(nums_list))