import random

def choose_random_word():
    words = ['python', 'programming', 'codealpha',  'developer', 'hangman', 'challenge', 'algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!\n")
    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if set(word).issubset(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()