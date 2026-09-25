import random

print("Rock Paper Scissors Game!")

item_list = ["ROCK", "PAPER", "SCISSOR"]
score = 0

while True:

    user_choice = input("Enter your move: ").upper()
    if user_choice == "Q":
        break
    if user_choice not in item_list:
        print("Please choose ROCK, PAPER or SCISSOR")
        continue

    comp_choice = random.choice(item_list)

    print(f"user choice = {user_choice}, computer choice = {comp_choice} ")

    if user_choice == comp_choice:
        print("TIE!")
    elif (user_choice == "ROCK" and comp_choice == "SCISSOR") or \
         (user_choice == "SCISSOR" and comp_choice == "PAPER") or \
         (user_choice == "PAPER" and comp_choice == "ROCK"):
         print("You Win!")
         score += 1
    else:
        print("computer wins")
        score -= 1

    print("Score",score)
