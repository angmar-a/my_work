name = input("What is your name? ")
print("Welcome,", name)
age = int(input("What is your age? "))
users = []


def age_check(age: int) -> None:
    if age <= 13:
        print("You cannot sit in the passenger seat of a car")
    elif age <= 18:
        print("You cannot vote ")
    elif age <= 25:
        print("You cannot rent a car")
    elif age >= 35:
        print("You are getting old!")
    

def language_check() -> None:
    language = input("Are you multilingual? (yes/no) ")
    if language == "yes":
        number_of_languages = int(input("How many languages do you speak? ")) 
        all_languages = []
        for n in range(number_of_languages ):
            language_name = input("Enter the name of the language: ")
            all_languages.append(language_name)
        print("You speak " + ", ".join(all_languages))
    else: 
        wish_language = input("What language would you like to learn? ")
        print(f"You wish to learn {wish_language}")
    users.append({"name": name, "age": age, "multilingual": language, "languages": all_languages if language == "yes" else wish_language})


while (True):
    age_check(age)
    language_check()
    cont = input ("Would you like to enter another user? (yes/no) ")
    if cont == "no":
        print("Thank you, goodbye!")
        break
    else:
        name = input("What is your name? ")
        print("Welcome,", name)
        age = int(input("What is your age? "))
        continue

print("\nAll users information:")
for user in users:
        print(user)


    