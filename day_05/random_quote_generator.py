# Starter file for students to create a Random Quote Generator

# Step 1: Import any necessary modules
import random

# Step 2: Define a function to load quotes from a file when called
# Step 3: Define a function that returns a random quote when called
# Step 4: Define a main function that runs the program. Make sure to call the function.

# Function takes in filename parameter and returns list of strings with lines from file
def load_quotes(filename = "quotes.txt"):
    with open(filename, "r") as file:
        quotes = [line.strip() for line in file if line.strip()]
    return quotes


# Function takes in list of strings and randomly chooses one to return
def get_random_quote(filename = "quotes.txt"):
    quotes = load_quotes(filename)
    print(random.choice(quotes))


# Runs program. Main() is the only function called so that it calls the other functions appropriately and controls logic flow.
def main():
    print ("Welcome to the Random Quote Generator!")
    get_random_quote()

main()
    





