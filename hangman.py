import random

print("===== HANGMAN =====")

words = ["python", "computer", "programming", "keyboard", "developer"]
word = random.choice(words)

hidden_word = ["_"] * len(word)
guessed_letters = []
attempts = 6

print("Guess the word!")
print(" ".join(hidden_word))

while attempts > 0 and "_" in hidden_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        attempts -= 1
        print(f"Wrong! Attempts remaining: {attempts}")

    print(" ".join(hidden_word))

if "_" not in hidden_word:
    print(f"\nYou won! The word was: {word}")

else:
    print(f"\nYou lost! The word was: {word}")