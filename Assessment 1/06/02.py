# Fill out the function count_even(lst) 

def count_even(lst):
  
    count = 0  
    for num in lst:  
        if num % 2 == 0:  
            count += 1  

    print(count)  

def get_list_of_ints():
    lst = []  
    user_input = input("Enter an integer or press enter to stop: ")  
    while user_input != "":  
        lst.append(int(user_input))  
        user_input = input("Enter an integer or press enter to stop: ")  

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)


if __name__ == '__main__':
    main()


# method 2

# def count_even(lst):
    
#     count = 0
#     for num in lst:
#         if num % 2 == 0:
#             count += 1
#     return count  

# def get_list_of_ints():
    
#     lst = []
#     while True:
#         user_input = input("Enter an integer or press enter to stop: ")
#         if user_input == "":  
#             break
#         try:
#             lst.append(int(user_input))  
#         except ValueError:
#             print("Please enter a valid integer.") 

#     return lst

# def main():
#     lst = get_list_of_ints()
#     even_count = count_even(lst)  
#     print(f"Number of even integers: {even_count}")  

# if __name__ == '__main__':
#     main()
