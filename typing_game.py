import random
import time

# List of possible letters

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Variables

letter1 = ""
letter2 = ""
letter3 = ""
letter4 = ""
letter5 = ""

word = ""

user_input = ""

num_correct = 0

start = 0
end = 0

start = time.time()

# Function that generates random pattern

def generate_pattern():
    
    # Make global variables

    global letter1
    global letter2
    global letter3
    global letter4
    global letter5
    global word

    # Assign random letters

    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    letter4 = random.choice(letters)
    letter5 = random.choice(letters)

    # Concatenate to make word

    word = letter1 + letter2 + letter3 + letter4 + letter5
    print(word)

    get_user_answer()

# Functions grabs user input, then passes input to check function
    
def get_user_answer():
    global user_input

    user_input = input("Type: ")

    check(user_input)

# Function checks the user input

def check(check_this_answer):
    global num_correct
    global end

    if check_this_answer == word:
        num_correct += 1
        generate_pattern()
        get_user_answer()
    elif check_this_answer == "end":
        end = time.time()
        print("You typed " + str(num_correct) + " patterns in " + str(round(end - start)) + " seconds.")
    elif check_this_answer != word or check_this_answer != "end":
        print("Incorrect. Try again.")
        get_user_answer

print("Rules: You have 60 seconds to type as many patterns correctly as possible. Type 'end' to end game.")
generate_pattern()
