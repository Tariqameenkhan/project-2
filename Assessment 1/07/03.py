""" Sophia has a fruit store. She has written a function 
   num_in_stock which takes a string fruit as a parameter and
   returns how many of that fruit are in her inventory"""

def num_in_stock(fruit: str) -> int:
   
    inventory = {
        'apple': 2,
        'durian': 4,
        'pear': 1000
    }
    
    return inventory.get(fruit, 0)

def main():
    fruit: str = input("Enter a fruit: ")
    
    stock = num_in_stock(fruit)
    
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == '__main__':
    main()
