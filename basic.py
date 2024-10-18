from datetime import datetime

# assigning variable
name = "Biplav Karki"
number = 1
print("My name is",number)

# check variable data type 
num1 = 10
num2 = 10.23
print(type(num1))

# inside small bracket ()) is tuple
print("*** TUPLE ***")
tuple = ('I live in',7,'Wallace','Street',2148)
print(type(tuple[1]))
print(type(tuple))

# inside big brackets [] is list
print("*** LIST ***")
list = ['I live in',7,'Wallace','Street',2148]
print(type(list[1]))
print(type(list))

# inside curly brackets {} are either set or dictionary
print("*** SET ***")
set = {'I live in',7,'Wallace','Street',2148}
# can't use indexing cause its unordered
#if want to then need to change it to tuple or list or iterate all the values
# example for abc in set: print(abc)
# print(type(set[1])) 
print(type(set))

# Dictionary use curly braces {}
print("*** DICTIONARY ***")
dict = {
    "name":"Biplav",
    "address":"7 Wallace Street",
    "Job":"Amazon Associate"
}
print(type(dict["name"]))
print(type(dict))

#find age utilising datetime from datetime
birthYear = int(input("Enter the you are born: "))
currentYear = datetime.now().year
age = currentYear - birthYear
print(age)

# double slash (//) is an integer division 
num1 = 7
num2 = 2
result = num1//num2 
print(f"The result is: {result}")# output would be 3 