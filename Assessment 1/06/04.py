# Fill out the double(num) function to return 
# the result of multiplying num by 2. 

def double(num: int) -> int:
    return num * 2

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()

# 2nd method

# def double(num: int) -> int:
#     return num * 2

# def main() -> None:
#     while True:
#         try:
#             num = int(input("Enter a number: "))
#             break  
#         except ValueError:
#             print("Please enter a valid integer.")

#     num_times_2 = double(num)
#     print("Double that is", num_times_2)

# if __name__ == '__main__':
#     main()
