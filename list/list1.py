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
# n = int(input("Enter the size of list : "))
# store integrs in a list using map,
# split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").split()))[:n]

# # printing the list
# print('The list is:', lst)


# swap first and last element in a given list 

# def swaplist (newlist):
#     temp =newlist[0]
#     newlist[0] =newlist[-1]
#     newlist[-1] =temp
#     return newlist
# newlist = [6,5,4,3,2,1]
# print (swaplist (newlist))



# check if element exist in a list :'

# def new(listt ,v ):
#     vari = False
#     for i in listt :
#         if v == i :
#            vari = True
#     print (vari)
       

# new ([4,5,6,7,0] , 4)


# def clear (list1):
#     list1 *=0
#     return list1

# print (clear ([4,6,8,9]))

#####################################################3
# sum of elements in a list 
# def sum (list1):
#     sum = 0
#     for i in list1:
#         sum+=i
#     return sum 

# print (sum([5,6,9]))

######################################################

# find smallest number in a list 

# def find_smallest (list1):
#     small = list1[0]
#     for i in list1:
#         if i < small :
#             small = i

#     return small

# print (find_smallest([10,5,0,8,1,5,4]))



###############################################################

# def find_largest (list1):

#     largest = list1[0]
#     for i in list1 :
#         if i > largest :
#             largest = i 


#     return largest 

# print (find_largest ([3,2,5,8,4,10]))



########################################################################



# find second largest number in a list 

# def find_largest (list1):

#     list2 = list(set(list1))

#     list2.sort()

#     return list2[-2]

# print(find_largest([5,6,9,0,3,2,19]))

#############################################################################

# def second_largest (list1):

#     list2= list(set(list1))
#     list2.sort()
#     return list2[-2]
    
# print(second_largest ([3,5,2,7,8,7,10,-4]))


###################################################################################

# print even numbers in a gven list 

# def even (list1):

#     for i in list1 :
#         if i %2 == 0 :
#             print (i)

# even ([4,5,9,8,0,2,2])

######################################################################################

# Python program to remove multiple
# elements from a list

# creating a list

# def remove (list1):
#     # will create a new list,
#     # excluding all even numbers
#     list1 = [ elem for elem in list1 if elem % 2 != 0]

#     return (list1)

# print(remove ([11, 5, 17, 18, 23, 50]))


###############################################################################################3
# count number of occurence 
# def count (list1 , x):
#     cnt = 0 
#     for i in list1 :
#         if i ==x :
#             cnt +=1 


#     return cnt

# print ( count ([5,3,4,5,6,5] , 5))


#################################################################################################

# def find (list1 , list2):

#     temp = 0
#     list3 =[]
#     for i in list1 :
#         temp = i 
#         if temp not in list2:
#                 list3.append (temp)
#     return list3

# print (find([5,6,8,9] , [5,6,7,4]))


###########################################################3333


# def countList(lst1, lst2):
# 	return [sub [i] for i in range(len(lst2))
# 					for sub in [lst1, lst2]]
	
# # Driver code
# lst1 = [1, 2, 3]
# lst2 = ['a', 'b', 'c']
# print(countList(lst1, lst2))


####################################################################
# from collections import deque 
# def find_sub_heigher(list1):
#     stack =deque ()

#     for i in range(len (list1)):

#         while stack and stack [-1] < list1[i]:
#             stack.pop()

#         stack.append(list1[i])

#     while stack :
#         print(stack.pop(), end=' ')
      

# find_sub_heigher([1,7,10,8,5,9,3,4])

###################################################################################


# # Python3 program to Find the two
# repeating elements in a given array

# def printRepeating(arr, size):

# 	print("Repeating elements are ",
# 						end = '')
# 	for i in range (0, size-1):
# 		for j in range (i + 1, size):
# 			if arr[i] == arr[j]:
# 				print(arr.index(i), end = ' ')
	
# # Driver code
# arr = [4, 2, 4, 5, 2, 3, 1]
# arr_size = len(arr)
# printRepeating(arr, arr_size)

# # This code is contributed by Smitha Dinesh Semwal



# Python3 code to demonstrate working of
# Initial character upper case
# Using title function of string

# initializing string
test_str = "geeks for geeks"

# printing original string
print("The original string is : " + str(test_str))

# Using str.title()
# Initial character upper case
res = test_str[0].upper() + test_str[1:]

# printing result
print("The string after uppercasing initial character : " + str(res))
