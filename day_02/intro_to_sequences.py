"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ['apple', 'banana', 'carrot', 'donut', 'egg']

# Access items by index (first = 0):
print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")

# Bug Exploration:
# Try printing foods[100] below.
#print (foods [100])
# Q: What error do you get, and what does it mean?
# list index out of range, meaning the index you are trying to access does not exist in the list.


# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()
foods.append('fish')

# TODO: Insert a food at the beginning with .insert()
foods.insert(0,'grape')    

# TODO: Remove one food from the list with .remove()
foods.remove('carrot')  

# TODO: How many foods are in the list? Use len()
print(len(foods))

# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why? - IndentationError: unexpected indent, becuse there is no such item in the list.


# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.
for i in range(len(foods)-1):
    print(f'current food is {foods[i]}')

for food in foods:
    print(f'current food is {food}')

# Bug Exploration:
# Change your loop to go past the length of the list:
# for i in range():
    # print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error? - Because while teh loop continues running, there is nothing else to print.  


# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
# me = { "name": "Kevin",  "age": 30, "student": False }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.
me = {
    "name": "Angelina",
    "age": 17, 
    "favorite_color": "blue"
    }

# Access values using keys by using the .get() method rather than indexing
print(f"My name is {me['name']}")
print(f"My age is {me['age']}")
print(f"My favorite color is {me['favorite_color']}")

# Bug Exploration:
# Try printing a key that doesn’t exist.
print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?


# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.
me['hometown'] = 'Boston'

# TODO: Change the value of an existing key.
me['age'] = 18

# TODO: Remove one key-value pair.
del me['favorite_color']

# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?


# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()

for key, value in me.items():
    print(f"{key} -> {value}")

# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?


# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.

Friends = [
    {"name": "Alice", "favorite_food": "pizza", age: 25},
    {"name": "Bob", "favorite_food": "sushi", age: 30},
    {"name": "Charlie", "favorite_food": "ice cream", age: 15}

# TODO: Print the favorite food of the second friend.
print(Friends[2]["favorite_food"])

# TODO: Loop through and print "<name> likes <food>" for each friend.
for friend in Friends:
    print(f"{friend['name']} likes {friend['favorite_food']}")


# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?


# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# 2. When would you want to use a dictionary instead of a list?
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# 4. What types of mistakes gave you the most errors today?
# 5. How might noticing errors actually help you learn?