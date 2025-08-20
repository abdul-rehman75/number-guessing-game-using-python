import random

def get_custom_range():
    print("\nSet your custom range:")
    
    while True:
        try:
            lower_limit = int(input("Enter lower limit: "))
            upper_limit = int(input("Enter upper limit: "))
            
            if lower_limit == upper_limit:
                print("Range must have at least one number difference. Try again.")
                continue
            
            if lower_limit > upper_limit:
                lower_limit, upper_limit = upper_limit, lower_limit
                print(f"Range adjusted to: {lower_limit} to {upper_limit}")
            
            return lower_limit, upper_limit
            
        except ValueError:
            print("Please enter valid numbers for both limits.")

def play_game(lower_limit=1, upper_limit=100):
    guess_number = random.randint(lower_limit, upper_limit)
    attempts_left = 10
    
    print(f"Guess the number between {lower_limit} and {upper_limit}")
    print(f"You have {attempts_left} attempts.")
    
    while attempts_left > 0:
        try:
            user_guess = int(input(f"\nEnter your guess: "))
            print()
            
            if user_guess == guess_number:
                print(f"Congratulations! You found the number {guess_number}!")
                attempts_used = 10 - attempts_left + 1
                print(f"You used {attempts_used} attempts.")
                return attempts_used
            
            attempts_left -= 1
            print("Incorrect, try again!")
            
            if attempts_left > 0:
                print(f"Attempts left: {attempts_left}")
                
                if user_guess < guess_number:
                    print("Hint: The number is higher")
                else:
                    print("Hint: The number is lower")
            else:
                print(f"\nGame Over! You ran out of attempts.")
                print(f"The correct number was: {guess_number}")
                return None
                
        except ValueError:
            print("Please enter a valid number!")
            continue

def show_menu(best_score):
    print("\n")
    print("GAME MENU")
    print("\n")
    print("1. Play again")
    print("2. Quit")
    
    if best_score:
        print(f"\nBest Score: {best_score} attempts")
    else:
        print(f"\nBest Score: No wins yet")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1 or 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Please enter 1 or 2")
        except ValueError:
            print("Please enter a valid number (1 or 2)")

def main():
    print("WELCOME TO NUMBER GUESSING GAME")
    
    best_score = None
    first_turn = True
    
    while True:
        if first_turn:
            result = play_game()
            first_turn = False
        else:
            lower, upper = get_custom_range()
            result = play_game(lower, upper)
        
        if result:
            if best_score is None or result < best_score:
                best_score = result
                print(f"New best score: {best_score} attempts!")
        else:
            print("Better luck next time!")
        
        choice = show_menu(best_score)
        
        if choice == 2:
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
