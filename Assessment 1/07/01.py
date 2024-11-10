# We've written a helper function for you called greet(name)
#  which takes as input a string name and prints a greeting. 

def greet(name: str):
    print("Greetings " + name.capitalize() + "!") 

def main():
    name: str = input("What's your name? ")  
    greet(name)  

if __name__ == '__main__':
    main()
