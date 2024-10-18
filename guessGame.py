import random


count = 1
while(count <= 3):
    print(f"You have {4-count} try")
    user_guess = int(input("Guess the number between 1 to 6: "))
    random_number = random.randint(1,6)
    if user_guess == random_number:
        print("Your guess is right")
        break
    else:
        print ("Try again")
    count+=1