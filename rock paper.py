import random  

player_choice = input("Choose rock, paper, or scissors: ").strip().lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"You chose {player_choice}, computer chose {computer_choice}.")
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "scissors" and computer_choice == "paper") or \
     (player_choice == "paper" and computer_choice == "rock"):
    print("You win!")
elif player_choice in ["rock", "paper", "scissors"]:
    print("You lose!")
    print("do you want to play again (Y/N)")
    ans=input().lower()
    if ans =='n':
        print("Thanks for playing")
        
        

   
        


