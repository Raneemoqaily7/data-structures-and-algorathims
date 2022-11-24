
# def myFunc(a):
#  print("\t Value received in 'a' =", a)
#  a+=2
#  print("\tValue of 'a' changes to :",a)
 
# num=13
# print("Initial number: ", num)
# myFunc(num)
# print("Value of number= ", num)

# def my_func (a):
#     return a+2

# a =13 
# print (a)
# print (my_func (5))
# print (a)



# def myFunc(myList):
#  print("\t List received: ",myList)
#  myList.append(3)
#  myList.extend([7,1])
#  print("\t List after adding some elements:", myList)
#  myList.remove(7)
#  print("\t List within called function:", myList)
#  return
 
# List1=[1]
# print("Listyy before function call :",List1)
# myFunc(List1)
# print("\t List after function call: ",List1)




# def myFunc(myList):
#  print("\t List received: ",myList)
#  myList.append(3)
#  myList.extend([7,1])
#  print("\t List after adding some elements:", myList)
#  myList.remove(7)
#  myList=[3, 4, 6]
#  print("\t List within called function:", myList)
#  return
 
# List1=[1]
# print("List before function call :",List1)
# myFunc(List1)
# print("\t List after function call: ",List1)



# def decotaror (func):
#     print ("iam decorator") 
#     return func ()
    


# @decotaror
# def say_hello():
#     p="hello world"
#     return p

# print (say_hello)



# list = [i for i in range (2 , 11) if i %2 == 0]
# print (list)



# matrix = [ [j for j in range  (3)] for  _ in range (6)]
# print (matrix)

# list = [i  for  i in "hello world"]
# print (list)


# list = ["even number" if i %2 == 0 else "odd number" for i in range (11)]
# print (list)



# list = [i for i in range (11) if i %2 == 0 if i%2 !=0]
# print (list)

# Reverse each string in tuple
# List = [string[::-1] for string in ["geeks" ,"for"]]

# # Display list
# print(list)


# def sum (i):
    
#         sum = 0
#         for j in str (i) :
#             sum += int (j)
#         return sum 

# list = [231 ,345,53]

# list1 = [sum(j) for j in list ]
# print (list1)
        

            
class Car :
    def __init__(self , name , price , model):
        self.name = name 
        self.price = price
        self.model = model

    def difintion (self):
        if self.model > 2019 :
            self.price = self.price + 20
        else :
                self.price = self.price -20
        return self.price

Bmw = Car ("Bmw" , 29 , 1999)
# print (Bmw.price  )

print (Bmw.difintion())
print (Bmw.price)




