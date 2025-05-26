import random

def hangman():
    words = ['apple', 'banana', 'grape', 'mango', 'peach']
    word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")
    print(f"You have {attempts_left} incorrect guesses allowed.\n")

    while attempts_left > 0:
        # Show current word progress
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word:", display_word)

        # Check if player has won
        if '_' not in display_word:
            print("Congrats! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            attempts_left -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Attempts left: {attempts_left}\n")

    else:
        print("Game over! The word was:", word)

if __name__ == "__main__":
    hangman()

