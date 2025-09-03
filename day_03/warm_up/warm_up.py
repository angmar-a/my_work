import random

energy = 10
turns = 0
print (turns)

def move (energy) -> int:    
    chance = random.randint(0, 1)
    if chance <= 0.5:
        energy -= 2
        return energy
    if chance >= 0.8:
        energy += 3
        return energy
    else :
        return energy


def  rest (energy) -> int:
    energy += 2
    return energy 
    

def  guess (energy) -> int:
    target = random.randint(1, 5)
    userguess = int(input("Guess a number between 1 and 5: "))
    if userguess == target:
       energy += 5
       print("You guessed correctly! You gain 5 energy.")
       return energy
    else:
       energy -= 1
       print(f"Wrong! The correct number was {target}. You lose 1 energy.")
       return energy
    
while True: 
    turns += 1
    userinput = str(input("Choose an action: move, rest, or guess: "))
    if userinput == "move":
        energy = move(energy)
        print(f"You have {energy} energy left after {turns} turns.")
    elif userinput == "rest":
        energy = rest(energy)
        print(f"You have {energy} energy left after {turns} turns.")
    elif userinput == "guess":
        energy = guess(energy)
        print(f"You have {energy} energy left after {turns} turns.")
    else:
        print(f"Invalid input. You lose 1 energy. You have {energy} energy left")
        energy -= 1
    if energy == 0:
        print("You have run out of energy. Game over!")
        break
    if energy >= 20:
        print(f"You win! You reached {energy} energy in {turns} turns.")
        break