"""
Simulation of the Monty Hall problem.
https://en.wikipedia.org/wiki/Monty_Hall_problem
"""

import random
TRIALS = 10000

wins_with_switch = 0
wins_without_switch = 0

for _ in range(TRIALS):
    # Randomly place the prize behind one of the three doors
    prize_door = random.randint(0, 2)
    # Contestant makes a random choice
    contestant_choice = random.randint(0, 2)

    # Monty opens a door that is not the prize door and not the contestant's choice
    # makes a list of doors where door != contestant_choice and door != prize_door
    remaining_doors = [door for door in range(3) if door != contestant_choice and door != prize_door]
    #randomly picks a remaining door of the 1 or 2 remaining
    monty_opens = random.choice(remaining_doors)

    # The door that remains closed and is not the contestant's initial choice
    # ramdomly picks one of the other doors that is not contestant_choice and monty_opens
    switch_choice = [door for door in range(3) if door != contestant_choice and door != monty_opens][0]

    # Check if sticking or switching would have won the prize
    if contestant_choice == prize_door:
        wins_without_switch += 1
    if switch_choice == prize_door:
        wins_with_switch += 1

# Run the simulation
print(f"Trials: {TRIALS}")
print(f"Wins without switching: {wins_without_switch} ({100 * wins_without_switch / TRIALS}%)")
print(f"Wins with switching: {wins_with_switch} ({100 * wins_with_switch / TRIALS}%)")
