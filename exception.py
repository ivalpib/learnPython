abc = 0
def checkEvenOdd():
    global abc
    try:  
        if abc == 0:
            number = input("ENter the number: ")
        else:
            number = input(abc)
        number = int(number)
        if number % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
    except (ValueError):
        abc = f" '{number}' is not a number. Please enter the number: "
        checkEvenOdd()
    finally:
        print("The program ran successfully.")
checkEvenOdd()
