import random

# ask user where they want to go
print("welcome to the castle! choose which room you would like to visit: \n 1. bedroom1 \n 2. bedroom2 \n 3. living room \n 4. party room \n 5. bathroom \n 6. kitchen")
selection = str(input("Enter your selection: "))
selection2 = ""
num = random.randint(1,100)
# print out survival rate of each room

# once they pick a room, print description and ask where they want to go next
if selection == "bedroom1":
    if num > 90:
        print("You're dead now.")
        exit()
    else:
        print("welcome to bedroom1! this is my bedroom, so it is the biggest one in the castle. unfortunately, the treasure is not in this room, so please pick another room. if you would like to exit the game, type 'exit':")
        print("choose which room you would like to visit next: \n 2. bedroom2 \n 4. party room \n 6. kitchen")
        selection2 = str(input("Enter your selection: "))
        print(selection2)
if selection2 == "quit":
    quit()

if selection == "bedroom2":
    if num > 90:
        print("You're dead now.")
        exit()
    else:
        print("welcome to bedroom2! this is my guest room. fun fact: michael jordan has slept here before. unfortunately, the treasure is not in this room, so please pick another room. if you would like to exit the game, type 'exit':")
        print("choose which room you would like to visit next: \n 1. bedroom1 \n 3. living room \n 5. bathroom")
        selection2 = str(input("Enter your selection: "))
        print(selection2)
if selection2 == "quit":
        quit()

if selection == "living room":
    if num > 90:
        print("You're dead now.")
        exit()
    else:
        print("welcome to the living room! every year, we host the largest jousting festival in england. unfortunately, the treasure is not in this room, so please pick another room. if you would like to exit the game, type 'exit':")
        print("choose which room you would like to visit next: \n 2. bedroom2 \n 4. party room \n 6. kitchen")
        selection2 = str(input("Enter your selection: "))
        print(selection2)
if selection2 == "quit":
    quit()

if selection == "party room":
    print("welcome to the party room! in this room, the great gastby throws the biggest parties imagineable. congrats! the treasure is in the room. you have successfully completed the adventure. thank you for playing! ")
    quit()

if selection == "bathroom":
    if num > 90:
        print("You're dead now.")
        exit()
    else:
        print("welcome to the bathroom! a little confused as to why you wanted to visit the bathroom. unless you had to use it. unfortunately, the treasure is not in this room, so please pick another room. if you would like to exit the game, type 'exit':")
        print("choose which room you would like to visit next: \n 2. bedroom2 \n 4. party room \n 6. kitchen")
        selection2 = str(input("Enter your selection: "))
        print(selection2)

if selection2 == "quit":
    quit()

if selection == "kitchen":
    if num > 90:
        print("You're dead now.")
        exit()
    else:
        print("welcome to the kitchen! world renownded chef, gordan ramsey, films the hit show 'Hell's Kitchen' here. unfortunately, the treasure is not in this room, so please pick another room. if you would like to exit the game, type 'exit':")
        print("choose which room you would like to visit next: \n 1. bedroom1 \n 3. living room \n 5. bathroom")
        selection2 = str(input("Enter your selection: "))
        print(selection2)
if selection2 == "quit":
    quit()
