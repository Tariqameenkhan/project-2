"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. This program shows how variable scope works.
"""

import random

NUM_SIDES = 6
def roll_dice():
    die1 = random.randint(1, NUM_SIDES)  
    die2 = random.randint(1, NUM_SIDES)  
    total = die1 + die2  
    print(f"Roll: {die1} + {die2} = Total: {total}") 

def main():
    print("Simulating rolling two dice three times:")
    roll_dice()  
    roll_dice()  
    roll_dice()  

if __name__ == '__main__':
    main()
