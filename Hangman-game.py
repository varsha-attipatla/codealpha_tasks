import random
# Predefined list of words
words = ["python", "hangman", "code", "program", "alpha"]

# Choose a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word: ", " ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct! ", " ".join(guessed_word))
    else:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left.")
        print("Word: ", " ".join(guessed_word))

# Game result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
