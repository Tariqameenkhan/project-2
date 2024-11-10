# Write a program that doubles each element in a list of numbers 

def main():
    numbers: list[int] = [1, 2, 3, 4]  
    numbers = [elem * 2 for elem in numbers]
    print(numbers)  

if __name__ == '__main__':
    main()
