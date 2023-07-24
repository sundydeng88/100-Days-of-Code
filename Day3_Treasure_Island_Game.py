print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("Your mission is to find the treasure.")
direction = input("You're at a crossroad. Which direction should you go, 'left' or 'right'?").lower()
if direction == "left":
    move = input("There is a sea you must cross, however there is a large tsunami. Should you 'swim' in the tsunami or 'wait' for it to clear?").lower()
    if move == "wait":
        door = input("You approach three coloured doors. Which should you go through? 'blue', 'red', or 'yellow'?").lower()
        if door == "blue" or door == "red":
            print("There were tigers behind the door and they ate you. Game Over.")
        else:
            print("You win! You are rich now!")
    else:
        print("You drowned. Game Over.")
else:
    print("You got shot. Game Over.")
