import random

def hangman():
    words = ["python", "django", "programming", "hangman", "challenge", "developer"]
    word_to_guess = random.choice(words).lower()
    guessed_word = ["_" for _ in word_to_guess]
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!\n")
    print("Guess the word:", " ".join(guessed_word))

    while attempts_left > 0 and "_" in guessed_word:
        print(f"\nAttempts remaining: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts_left -= 1

        print("\nWord to guess:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nGame over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
