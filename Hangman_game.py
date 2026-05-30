import random

# list of 5 predefined words
words = ["apple", "python", "cloud", "robot", "laptop"]

# choosing random word
chosen_word = random.choice(words)

# storing guessed letters
guessed_letters = []

# wrong guesses count
wrong_guesses = 0

print("WELCOME TO HANGMAN GAME")

# game loop
while wrong_guesses < 6:

    display = ""

    # showing guessed letters and hidden letters
    for letter in chosen_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord :", display)

    # checking win condition
    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    # taking input
    guess = input("Enter a letter : ").lower()

    # checking if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter")

    # correct guess
    elif guess in chosen_word:
        print("Correct Guess")
        guessed_letters.append(guess)

    # wrong guess
    else:
        print("Wrong Guess")
        wrong_guesses = wrong_guesses + 1
        guessed_letters.append(guess)

        print("Remaining chances :", 6 - wrong_guesses)

# game over condition
if wrong_guesses == 6:
    print("\nGame Over")
    print("The word was :", chosen_word)
