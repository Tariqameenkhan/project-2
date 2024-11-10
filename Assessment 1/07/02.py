# Implement the following function which takes in
#    3 integers as parameters:

def in_range(n: int, low: int, high: int) -> bool:
  
    if low <= n <= high:
        return True
    return False

def main():
    n = int(input("Enter the number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()
