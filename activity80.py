import random

def get_computer_choice():
    """Randomly selects Rock, Paper, or Scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the rules of Rock, Paper, Scissors."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

    while True:
        
        user_choice = input("Your choice: ").strip().lower()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

if __name__ == "__main__":
    main()
