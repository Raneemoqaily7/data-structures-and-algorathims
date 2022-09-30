# list = [[1,2],[3]]
# print (list)
# print("\n")
# # print (list[1][1]) --> indexerror

# list2=[1,2,3,4]
# print (len(list2)-3)
# print (list2[-3])

# list3 = input ("enter elements space seperated ")
# str =list3.split()
# print(str)




# input size of the list
n = int(input("Enter the size of list : "))
# store integrs in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\
elements:").split()))[:n]

# printing the list
print('The list is:', lst)



