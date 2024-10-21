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

# use assert to terminate the program if condition does not meet 
#example age = -16
# assert age > 0
# print (age) //it won't print age unless assert condition is met

# expenses = [889, 788, 5656, 4455, 455, 45]
# total = 0
# for each in expenses:
#     total += each

# average = total / len(expenses)
# print(f" the number of element in expenses is {len(expenses)}")
# print(f" The total expenses is: {total}")
# print(f" The average expenses is: {average}")

# values = [10, 0, 25, 0, 50, -1, 40]
# total = 0
# n = 0
# for tot in values:
#     if tot == 0:
#         continue
#     elif tot < 0:
#         break
#     total+=tot
#     i +=1

# print(f" The total value is: {total}")
# print(f" The average value is: {total/n}")

# name_list = ['Samir','Suman',"Shai",'Sulav','Simran','Sahil','Summer','Sandhya']
# name_list.remove(name_list[6])
# name_list.remove(name_list[6])
# print(name_list)

#challenge 15

# days = []
# days.append("Sunday")
# days.append("Monday")
# days.append("Tuesday")
# days.append("Wednesday")
# days.append("Thursday")
# days.append("Friday")
# days.append("Saturday")
# print(days)

# select_day = [day for day in days if day.startswith('S')]
# print(select_day)

# challenge set

# set_A = {'rum', 'whisky', 'brandy'}
# set_B = {'vodka','beer','whisky'}

# print(set_A.difference(set_B))
# print(set_A.intersection(set_B))
# print(set_A.union(set_B))
# print(set_A.symmetric_difference(set_B))
# set_A.symmetric_difference_update(set_B)
# print(set_A)

# dictionary

personal_info = {
    'name': 'Biplav',
    'surname':'Karki',
    'address': '7 Wallace St',
    'movies': ['Mission Impossible','Catch me if you can','Jason Bourne'],
    'hobbies': {
        'sport': 'football',
        'online_game': 'pubg'
    }
}

# print(personal_info['hobbies']['sport'])
# personal_info['hobbies']['music'] = 'too much love will kill you'
# personal_info['something'] = 'anything'
# print(personal_info['something'])
# print(personal_info['hobbies']['music'])
# personal_info.pop('something')
# print(personal_info)
# y = []
# for x in range(1,6):
#     y.append(x)
# print(y)

# z = [x ** 2 for x in range(1,6) if x > 2]
# print(z)
# choice = 'yes'
# student_score = {}
# while choice == 'yes':
#     name = input("Enter the name of the student: ")
#     score = float(input(f" Enter the score of {name}: "))
#     student_score.update({name:score})
#     choice = input(' You want to add more score: (YES/NO) ').lower()
#     print(choice)
#     if choice == 'y':
#         choice = 'yes'
#     print(choice)
# print(student_score)
# above_80 = { name:score for name,score in student_score.items() if score > 80}
# print(above_80)

# # functions
# from datetime import datetime

# def findCube(x):
#     result = x ** 3
#     return result

# def calculateAge(year):
#     age = datetime.today().year  - year
#     print(age)

# print(findCube(2))
# calculateAge(1995)

# inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make 
        self.model = model

    def get_details(self):
        print(f"This vehicle is made by {self.make} and the model is {self.model}")

class Car(Vehicle):
    def __init__(self, year, make, model):
        self.year = year
        super().__init__(make, model)
    
    def get_details(self):
        print(f"The car is built in {self.year}")
        return super().get_details()

car1 = Car(1995, 'Toyota', 'Sedan')
car1.get_details()


