# def sumDigit (string):
#     if len (string) == 1:
#         return int(string)

#     return int (string[0])  + sumDigit (string[1:])
# #2 + 


# print (sumDigit ("2345"))  #14




#  1, 1, 2, 3, 5, 8, 13, 21 

# def fibonacci(n):
#     """ Returns Fibonacci Number at nth position using recursion"""
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
 
# print (fibonacci (15))

# def factorial(n):
#     if n == 1:
#         return 1
#     return n *factorial(n-1)
        
        
# print (factorial(6))



# def summation (n):
#     if n == 0:
#         return 0 

#     return n + summation (n-1)


# print (summation (4))


# def fibonacci_seq (num) :
#     if num <0:
#           print("Please provide a positive integer value")
#     if num == 0:
#            return 0
#     elif num == 1:
#           return 1
#     else:
#         return fibonacci_seq (num-1) +fibonacci_seq(num-2)

        

    
# print (fibonacci_seq (7))


# def even(k):
#     if k <= 0:
#         print("please enter a positive value")
#     elif k == 1:
#            return 0
#     else:
#        return even(k-1) + 2
# print(even(6))




# def n_power(n):
#     if n < 0:
#        print ("please enter a positive value")
#     elif n == 0:
#         return 1
#     else:
#        return n_power(n-1)*3
# print (n_power(4))


########################################################3
# write a function to multiply all the numbers in a list using recursion 
def multiply_list (list1):
    if len(list1) == 1:
        return (list1[0])

    else:
        return list1[0] * multiply_list (list1[1:])
        

print (multiply_list([2,3,4,5])) #120