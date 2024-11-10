# Fill out the chaotic_counting() function, 
# which prints the numbers from 1 to 10

import random

DONE_LIKELIHOOD = 0.3 

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  
        print(curr_num)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
