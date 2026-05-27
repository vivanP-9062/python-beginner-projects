print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to a zombie invasion")
print("Your mission is to find the chest which contains a gun and essentials to leave this place alive.")
choice = input("you're at a traffic light choose left or right\n").lower()
if choice == "left" or choice == "Left":
    print("you found a armored car keep going straight with the car")

    choice_two = input('''there is a zombie horde in front of you.
type 'straight' if you wanna ride over them. type 'exit' if you wanna exit and take an alternative route\n''' ).lower()
    if choice_two == "straight":
        door= input('''you ran over the zombies you arrived at a safehouse unarmed. there are 3 doors in front of you
red, blue and black\n''').lower()

        if door == "red":
            print("CONGRATULATIONS! you found the chest required to survive the zombie invasion. you make it out alive")
        elif door == "blue" or door == "black":
            print("there was a zombie boss in front of this door you got infected. GAME over")
        else:
            print("wrong input")


    elif choice_two == "exit":
        print("the horde noticed you exited and ran straight towards you killing you. GAME OVER")
else:
    print("there was a gas bomb in that direction you inhaled a lot of it resulting in a chemical death. GAME OVER")





