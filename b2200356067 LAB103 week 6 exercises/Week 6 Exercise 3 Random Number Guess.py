import random
number = random.randint(0,100)
while True:
    a = int(input("Please enter your number: "))
    if a > number:
        print("Please decrease your number: ")
    elif a < number:
        print("Please increase your number: ")
    else:
        print("Your guess is correct. ")
        print("Algorithim closing..")
        break