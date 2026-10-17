import random

words = ["python", "nurse", "hospital", "medicine", "patient"]


word = random.choice(words)

guessed_letters = []      
incorrect_guesses = 0     
max_incorrect = 6         

print("=== Welcome to Hangman! ===")
print("Guess the word one letter at a time.")
print(f"You are allowed {max_incorrect} incorrect guesses.\n")

while incorrect_guesses < max_incorrect:
    
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")


    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower().strip()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")
else:
    
    print("Game over! You ran out of guesses.")
    print("The word was:", word)
