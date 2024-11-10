"""
A program to convert feet to inches.
There are 12 inches in 1 foot.
"""

INCHES_IN_FOOT: int = 12  

def main():
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * INCHES_IN_FOOT
    print(f"That is {inches} inches!") 

if __name__ == '__main__':
    main()
