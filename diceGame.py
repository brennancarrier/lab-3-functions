import random
NUM_DICE_TO_ROLL = 5
SEED = 2183

def rollDice(numDice):
    dice = []
    for i in range(numDice):
        dice.append(random.randint(1, 6))
    return dice

def mostRepeats(dice):
    kind = 1
    for i in range(len(dice)):
        count = 0
        for j in range(len(dice)):
            if dice[i] == dice[j]:
                count += 1
        if count > kind:
            kind = count
    return kind

def main():

    random.seed(SEED)
    continueLoop = "Y"

    while continueLoop.upper() == "Y":
        dice = rollDice(NUM_DICE_TO_ROLL)
        repeats = mostRepeats(dice)
        print("Your roll of", dice, "contains", repeats, "of a kind.")
        continueLoop = input("Do you want to roll again (Y/N)? ")

if __name__ == "__main__":
    main()