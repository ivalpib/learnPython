# age1 = int(input("Enter the first age: "))
# age2 = int(input("Enter the second age: "))

# # comparing the ages
# if age1 > age2:
#     print(f"First person is older by {age1 - age2} years compare to the second person")
# elif age1 < age2:
#     print(f"First person is younger by {age2 - age1} years compare to the second person")
# else:
#     print(f"First person is the same age as the second person which is {age1} years old")


# checking eligibility to vote

# person_age = int(input("Enter the first age: "))
# status = input("Are you a citizen? (YES/NO)")
# person_citizenship_status = status.lower()
# if person_citizenship_status == 'yes' and person_age>=18:
#     print("You are eligible to vote")
# elif person_citizenship_status == 'no':
#     print(" First, you need to be a Citizen to vote")
# else:
#     print(" You need to be 18 years old or higher to vote")

# check if the input element is present in list or not

# elements = ['air', 'water', 'rock', 'fire','metal']
# user_input = input(" Enter the element: ").lower()

# print(user_input in elements)
# if user_input not in elements:
#     print(f"{user_input} is not in element list")
# else:    
#     print(f"{user_input} is in element list")

# print cube of the input number
# number = int(input("Enter the number: "))
# print(f" The cube of {number} is {number ** 3}")

# string methods in Python
# name = input("Enter your fulname: ")
# clear_space = name.strip() 
# formatted_name = clear_space.title() #capitalise first character for every word
# print(f"The input user name is:  {formatted_name}")
# replaced_user_name = formatted_name.replace('Biplav','Sribika')
# print(f"The new user is {replaced_user_name}")
 #split the words by space but can use anything inside ""
# userlist = replaced_user_name.split(" ")
# print(f"The firstname is: {userlist[0]}")