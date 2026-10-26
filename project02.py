import random
import string
from collections import Counter
import os

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100!")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congrats! Guessed in {attempts} attempts!")
                score = (max_attempts - attempts + 1) * 10
                print(f"Score: {score}")
                return
        except ValueError:
            print("Enter a number!")
    print(f"Game Over! Number was {secret_number}")

def word_counter_tool():
    print("\n--- Word Counter ---")
    sample = "sample.txt"
    if not os.path.exists(sample):
        with open(sample, "w") as f:
            f.write("Python is fun. Python is easy.\nThis project uses loops and random module.\n")
    filename = input(f"Enter file (Enter for {sample}): ").strip()
    if filename == "":
        filename = sample
    try:
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        cleaned = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
        freq = Counter(cleaned)
        print(f"\nWords: {len(words)}, Chars: {len(text)}, Lines: {len(text.splitlines())}")
        print("Top 5 words:")
        for w,c in freq.most_common(5):
            print(f"  {w}: {c}")
    except:
        print("File not found!")

def main():
    while True:
        print("\n1.Guessing Game 2.Word Counter 3.Exit")
        ch = input("Choose: ")
        if ch == '1':
            number_guessing_game()
        elif ch == '2':
            word_counter_tool()
        elif ch == '3':
            break

if __name__ == "__main__":
    main()