# CodeAlpha_ProjectName hangman game
import random

def play_hangman():
    # 1. Predefined list of 5 words
    words = ["python", "program", "script", "source", "intern"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6  # Limit incorrect guesses to 6

    print("--- Welcome to Hangman! ---")
    print(f"Guess the word. You have {max_incorrect} incorrect attempts allowed.")

    while incorrect_guesses < max_incorrect:
        # Display the current state of the word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord: ", display_word.strip())
        print(f"Incorrect attempts remaining: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check for win condition
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word correctly: '{secret_word}' 🎉")
            break

        # Get user input
        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Check if guess is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    else:
        print(f"\nGame Over! You've run out of attempts. The word was: '{secret_word}'")

if __name__ == "__main__":
    play_hangman()
