
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



def decotaror (func):
    print ("iam decorator") 
    return func ()
    


@decotaror
def say_hello():
    p="hello world"
    return p

print (say_hello)

