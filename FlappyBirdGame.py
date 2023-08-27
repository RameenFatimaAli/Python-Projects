import random

def choose_word():
    words = ["apple", "banana", "cherry", "dog", "elephant", "frog", "giraffe", "honey", "iguana", "jacket"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts -= 1
            print(f"Attempts left: {attempts}")

        display = display_word(word_to_guess, guessed_letters)
        print(display)

        if display == word_to_guess:
            print("Congratulations! You've guessed the word.")
            break

        if attempts == 0:
            print("Game over! The word was:", word_to_guess)
            break

hangman()
