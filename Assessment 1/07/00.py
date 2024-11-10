# There are times where we want to return different
#  things from a function based on some condition. 

ADULT_AGE: int = 18  

def is_adult(age: int) -> bool:
    if age >= ADULT_AGE:
        return True
    return False 

def main():
    try:
        age = int(input("How old is this person?: "))
        print(is_adult(age))
    except ValueError:
        print("Please enter a valid integer for age.")
    
if __name__ == "__main__":
    main()
