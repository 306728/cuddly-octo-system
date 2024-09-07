import time
import sys
import random

options = ["very easy", "easy", "average", "hard", "very hard"]
f = open("/workspaces/cuddly-octo-system/AS/AS09/wordlist.txt", "r")
wordlist = []

for line in f:
    wordlist.append(line.split())

# very easy: 4-5
# easy 6-8
# average: 9-10
# hard: 11-12
# very hard: 13-15

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def hack(words):
    attempts = 4
    possible_words = []

    for i in range(16):
        random_word = random.choice(words)
        while random_word in possible_words:
            random_word = random.choice(words)
        possible_words.append(random_word)
        delay_print(possible_words[i] + " ")

    password = random.choice(possible_words)
    delay_print("\nOne of the above 16 words is the password.\nGuess a word.\n")

    while attempts != 0:
        likeness = 0
        delay_print(f"\nAttempts Remaining: {attempts}")
        guess = input("\n > ").upper()
        if guess == password:
            return "Access granted."
        else:
            for i in range(len(guess)):
                if guess[i] == password[i]:
                    likeness += 1
            attempts -= 1
            delay_print(f"Entry denied.\nLikeness: {likeness}")
    else:
        return "\nYou have failed to hack the terminal.\nTerminal permanently locked."

delay_print("Choose difficulty level (very easy, easy, average, hard, very hard)")
difficulty = input("\n> ").lower()

delay_print(f"Welcome to ROBCO Industries (TM) Termlink\nPassword required\n")

match difficulty:
    case "very easy":
        delay_print(hack(wordlist[random.randint(0, 1)]))
    case "easy":
        delay_print(hack(wordlist[random.randint(2, 4)]))
    case "average":
        delay_print(hack(wordlist[random.randint(5, 6)]))
    case "hard":
        delay_print(hack(wordlist[random.randint(7, 8)]))
    case "very hard":
        delay_print(hack(wordlist[random.randint(9, 11)]))
