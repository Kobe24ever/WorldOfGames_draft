from Utils import screen_cleaner
from Score import add_score, initialize_score


def load_game():
    new_score = 0  # Initialize new_score
    while True:
        print("Please choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("2. Guess Game - guess a number and see if you chose like the computer")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

        # Get the chosen game input from the user
        game_choice = input("Enter the number of the game you want to play (1-3), or 'q' to quit: ")

        if game_choice == 'q':
            break

        # Check if the input is a valid game choice (1, 2, or 3)
        if game_choice not in ['1', '2', '3']:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        # Get the level of difficulty input from the user
        difficulty = input("Please choose game difficulty from 1 to 5: ")

        # Check if the input is a valid difficulty level (1, 2, 3, 4, or 5)
        if difficulty not in ['1', '2', '3', '4', '5']:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        # Save the chosen game and difficulty level to variables
        chosen_game = int(game_choice)
        chosen_difficulty = int(difficulty)

        if chosen_game == 1:
            print(f"You chose Game {chosen_game} with difficulty level {chosen_difficulty}. Let's play!")
            from MemoryGame import play_memory_game
            result = play_memory_game(chosen_difficulty)
        elif chosen_game == 2:
            print(f"You chose Game {chosen_game} with difficulty level {chosen_difficulty}. Let's play!")
            from GuessGame import play_guess_game
            result = play_guess_game(chosen_difficulty)
        elif chosen_game == 3:
            print(f"You chose Game {chosen_game} with difficulty level {chosen_difficulty}. Let's play!")
            from CurrencyRouletteGame import play_roulette_game
            result = play_roulette_game(chosen_difficulty)
        else:
            print("Invalid game choice.")
            continue

        if result['success']:
            # Call add_score function to add the new score to Scores.txt
            new_score = add_score(chosen_difficulty)
            if new_score != -1:
                print(f"Congratulations! Your new score is: {new_score}")
            else:
                print("Failed to update the score.")

        # Ask the user if they want to continue to a new game
        while True:
            play_again = input("Do you want to play another game? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == 'no':
            # Print the final score if the user chooses not to play another game
            print(f"Your final score: {new_score}")
            break
        else:
            # Clear the screen before starting a new game
            screen_cleaner()

    print("Thank you for playing!")


def welcome():
    user_name = input("Enter your name: ")
    initialize_score()  # Initialize the score file to 0
    return f"Hello {user_name} and welcome to the World of Games (WoG). Here you can find many cool games to play."
