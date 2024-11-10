"""In this program we show an example of using 
   dictionaries to keep track of information in a phonebook.

"""

def read_phone_numbers():
    
    phonebook = {}  

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to look up: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            print(f"{name}'s number is {phonebook[name]}")

def main():
    phonebook = read_phone_numbers()
    print("\nPhonebook entries:")
    print_phonebook(phonebook)
    print("\nLookup numbers:")
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
