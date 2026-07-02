import random

options = ["rock", "paper", "scissors"]

score_user = 0
score_computer = 0

print("=== Rock Paper Scissors Game ===")

while True:
    user_input = input("\nEnter Rock, Paper or Scissors: ").lower()

    if user_input not in options:
        print("Invalid Choice!")
        continue

    computer_choice = random.choice(options)

    print("Your choice:", user_input)
    print("Computer Choice:", computer_choice)

    if user_input == computer_choice:
        print("It's a Tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You Win!")
        score_user += 1
    else:
        print("Computer Wins!")
        score_computer += 1

    print(f"Score -> You: {score_user} | Computer: {score_computer}")

    choice = input("Play Again? (yes/no): ").lower()
    if choice != "yes":
        break

print("\nGame Over!")
print("Final Score")
print("You:", score_user)
print("Computer:",)