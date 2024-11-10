"""There's a small fruit shop nearby your house that you like
 to buy from. Since you buy several fruit at a time, you want 
 to keep track of how much the fruit will cost before you go."""

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print(f"Your total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
