print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Please type all answers in lowercase letters.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first = input("You come to a crossroad in the woods. You can choose left or right. Please type 'left' or 'right'")

left = input("You chose left. The path leads to a cabin in the woods. Do you choose to go in the cabin or continue down the path? Please type 'cabin' or 'path'")
right = "You chose right. Your path led to a cliff and you fell off. *GAME OVER*"

cabin = input("You chose to go into the cabin. You find a secret room with three doors. Next to the doors on a small table is a piece of laminated paper with three bullet points. The first bullet point says 'you can only enter one door.' The second bullet point says 'the treasure lies behind one of these doors.'The third bullet point says 'You only have one choice. Choose wisely, and good luck.'' Please type 'first', 'second', or 'third'")
path = "You chose to continue down the path. Around the very next bend a bolt of lighting strikes a tree and lands on you. *GAME OVER*."

first = "You chose the first door. Really that lazy, huh? You open the door and find an empty white room with no exit! HAVE FUN *GAME OVER*"
second = "You chose the second door. The middle child is always underappreciated. YOU CHOOSE CORRECTLY. YOUR PRIZE IS *drumroll* *drumroll* *drumroll* A HALF OFF COUPON TO YOUR LOCAL CHINESE BUFFET. CONGRATS! *GAME OVER*"
third = "You chose the third door. You are eternally stuck in algebra 2 class. *GAME OVER*"

if first != "left" and first != "right":
 print("You have chosen poorly. *GAME OVER*.")
else:
  if first == "left":
    print(left)
  else:
    print(right)


if left != "cabin" and left != "path":
  print("You have chosen poorly. *GAME OVER*.")
else:
  if left == "cabin":
    print(cabin)
  else:
    print(path)


if cabin != "first" and cabin != "second" and cabin != "third":
  print("You made it so far just to fail like this? A TYPO? THIS IS WHY WE CANT HAVE NICE THINGS. *GAME OVER*")
else:
  if cabin == "first":
    print(first)
  elif cabin == "second":
    print(second)
  else:
    print(third)

print("Thank you for playing my game. Go eat a cookie.")
