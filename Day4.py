import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
computer = random.choice(choices)
user = int(input("Rock Paper or Scissors? 0 for Rock, 1 For Scissors, 2 for Paper!"))
ui = []

if user == 0:
    ui = rock
elif user == 1:
    ui = paper
else:
    ui = scissors



if computer == rock and ui == scissors:
    print("Computer's Choice:",computer, "Your Choice:", ui, "Computer wins, you lose.")
elif computer == paper and ui == rock:
    print("Computer's Choice:",computer, "Your Choice:", ui, "Computer wins, you lose.")
elif computer == scissors and user == paper:
    print("Computer's Choice:",computer, "Your Choice:", ui, "Computer wins, you lose.")
elif computer == rock and ui == paper:
    print("Computer's Choice:",computer,"Your Choice:", ui ,"You win! WOOHOO!")
elif computer == scissors and ui == rock:
    print("Computer's Choice:",computer, "Your Choice:", ui, "You win! WOOHOO!")
elif computer == paper and ui == scissors:
    print("Computer's Choice:",computer, "Your Choice:", ui, "You win! WOOHOO!")

