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
# test_str = "geeks for geeks"

# # printing original string
# print("The original string is : " + str(test_str))

# # Using str.title()
# # Initial character upper case
# res = test_str[0].upper() + test_str[1:]

# # printing result
# print("The string after uppercasing initial character : " + str(res))


################################################################
# write  a function to remove empty string from list of strings 
## input = ["hello" , "" , "bye"]
## output = ["hello" , "bye"]

# def filterdData (list1):
# first way using append to a list 
#     l2 = []
#     for i in range (len(list1)) : 
#         if list1[i] != "":
#             l2.append (list1[i] )
#     return l2

# print (filterdData([2 , "" , 1]))



# 2nd way using filter
#     return  list (filter (None , list1))

# print (filterdData ([2 , "" , 1 , "" , "kkkkk" , 6]))


#######################
#extend list and append 

# list1= [ "a" , "b" , ["c" ,["d" , "e" ,["f" , "g"] ,"k"],"l"] ,"m" , "n"]
# list1[2][1][2].extend(["h" ,"i" , "j"])

# print (list1)

# #output === >  ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# list2= [ "a" , "b" , ["c" ,["d" , "e" ,["f" , "g"] ,"k"],"l"] ,"m" , "n"]
# list2[2][1][2].append(["h" ,"i" , "j"])
# print (list2)

#output === >  ['a', 'b', ['c', ['d', 'e', ['f', 'g', ['h', 'i', 'j']], 'k'], 'l'], 'm', 'n']




# def extend (l1 , sl):
#      l1.extend (sl)
#      return l1

# print ( extend ([1,2,3]  , [4,5]))

################################################################3
# write a fnction to check if a value is present and replace it with a nother given value 
# def found (l1 ,n ,m ):
#     for i in l1:
#         if n in l1:
#             index = l1.index(n)
#             l1[index] = m 
        
        
            

#             return (l1) 
#         return("value not exist" )


# print (found( [ 1 ,2 ,3,4 , 4] , 4 ,20) )


##############################
# write a program to remove all occurence of a specific item 

#input = [5,6,7,20,7,8,20,6,9] , 20
# output = [5,6,7,7,8,6,9]

# def filterData (l1 , n ) :
#     res =[]
#     for i in range (len(l1)):
#         if l1[i] !=n:
#             res.append(l1[i])

#     return res

# print (filterData([5,6,7,20,7,8,20,6,9] , 20))



######################################################
# Given an array of integers nums and an integer target,
#  return indices of the two numbers such that they add up to target.


# def sum (list1 , target):
#     for i in range (len (list1)):
#         k = i+1
#         for j in range (k,len(list1)):
#             if list1[i] + list1[j] == target :
#                 res = [i , j]
#     return res 

# print (sum ( [3,6,9] , 12))
                
##########################################################################################
# list1 = [0,0,0,1,1,1,2,3,4]




# def duplicated (parts) :
   
#     sen = ""
#     for part in parts :
#         if part.next() == "," :
#          sen += part
#     # sen = " ".join(parts)
          
                
#     return f"{sen}."


# print(duplicated(["Hello" , "," ,"my" , "world"]))
# def max (list1):
#     max = 0
#     for i in list1:
#         if i > max :
#             max = i
#     return max
# print (max([1,2,5,3,4]))

# def min (l1):
#     min = l1[0]
#     for i in l1:
#         if i < min :
#             min = i
#     return min 
# print (min ([5,2,0,3,4]))

# def shulfed(list1):

#Solution1 
    # list1.sort()
    # sum = 0
    # for i in list1:
    #     sum +=i
    # if len (list1)== 0:
    #     missing =1
    # total = (list1[-1] * (list1[-1] +1)) /2
    # missing = total - sum 
    # if missing ==0 :
    #     return list1[-1] +1

    # return missing





    

#Solution2 
    # min = list1[0]
    # for i in range(len(list1 )):
    #         if list1[i] < min :
    #             min = list1[i]
    


    # if min != 1 :
    #     return 1
    
    # if len(list1) == 0:
    #     return 1

    # for _ in list1:
        
        

    #     if min in list1  :
          
    #         min +=1  
            
            
        
        
    # return min

 

#Solution 3 
#     max = 0
#     for i in l1:
#         if i > max :
#             max = i
#     missing =max +1

#     min = l1[0]
#     for i in l1:
#         if i < min :
#             min = i


#     for _ in l1 :
#         if max in l1  :

#             max = max-1
#         if   max ==  min :
#             max = missing
#         if min !=1 :
#             return 1

        
        
        
#     return max

# print (shulfed([5,4,3,2,1]))



# #Solution 4
#     n = len (list1)+1 
#     return (n * (n+1)) //2  - sum(list1)


# print (shulfed([1,3,4]))  




# def split_integer(num, parts):
#     quotient, remainder = divmod(num, parts)
#     lower_elements = [quotient for i in range(parts - remainder)]
#     higher_elements = [quotient + 1 for j in range(remainder)]
#     return lower_elements + higher_elements

# print (split_integer(21,6))


#############################################################################################
# write a function which will create a stringfrom a list of strings , seperated by space 
# example : ["hello" , " world"] ----> "hello world"


# def words_to_sentence (words):
#     return "".join (words)

# print (words_to_sentence (["hello" , " world"]))



#################################################################################################
# write a function to give this pattern of output 

# example :
#(abcd) -- > (ABbCccDddd)
#(rsftgj) --> (RSsFffTtttGggggJjjjjj)




# def accum(string):

#Solution 1
    # l=""
    # k=0
    # for i in range(len(string)) :
       
        
    #         l +=string[i].upper() + string[i].lower()*k 
            
    #         k+=1
    #         if i != len(string)-1 :
    #             l+="-"
            
    # return l

#Soution 2

    # R = "-".join(c.upper()+c.lower()*i for i,c in enumerate(string)) 
    # return R
# print (accum("abcD"))

##########################################################################################


#adding arrays of letters 
#write a function that takes an array of letters and combine them into words in a sentence 

# def add_Arr (list1) :
#     r=""
#     z =len(list1[0])
#     for i in range (z) :
            
#             for j in list1:
        
                 
#                 r+=j[i]
#             if i < (len(j) -1) :
#              r+= " " 
#     return r
  
       
    
# print (add_Arr([["j" ,"l" ,"l" ,"m","","s" ,"l" ,"l" ,"k" ,"l"] , ["u" ,"d" ,"i" ,"a","k","k" ,"l" ,"l" ,"k" ,"l"] ,["s" ,"v" ,"f" ,"n","f","k" ,"l" ,"l" ,"k" ,"l"] ,["t", "l" ,"e" ,"k" ,"l" ,"l" ,"k" ,"l","","p"] , ["a" ,"b" ,"c" ,"d" ,"" ,"k" ,"l" ,"l" ,"k" ,"l"],["f" , "" ,"g" ,"k" ,"u" ,"k" ,"l" ,"l" ,"k" ,"l"]])) 

# Last Survivor 
# given a string  of letters and list of mumbers , the numbers indecates position of letters that must be removed 
# in order , starting from the begggining of the array
#  example :
# str = "zbl" , arr = [0,1]  ---output ---> "b" 


# def last_survivor (letters , list1):

    # --------->str = " ".join (letters)
    # ----------> r = str.split()
    # the join and split same as using :
#     letters=list(letters)
#     for i in list1:
#         for j in range (len(letters)):
#             if i == j :
#                 letters.pop(j)
#     letters = "".join (letters)
                
#     return letters



  
# print (last_survivor("zbl"  , [0,1]))





##################################################################################################


# def reverse (s):

#     str =""
#     r = s.split()

# #   r = ["hello" , "world"]
 
#     for i in r :
#         for j in range(1,len(i)):

#             str +=i[-j]
#         str+=i[0]
#         str+=" "
            
#     return  str
    
        
        
# shout = reverse        
        

# print (shout  ("hello world"))




##################################################################
# def average (list1):
#     sum = 0
#     for i in list1 :
#         sum +=i
#     average = sum / len (list1)
#     return average 
# print (average([1,2,3,4,5,6]))



###############################################################


