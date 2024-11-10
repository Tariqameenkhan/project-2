# Use Python to calculate the number of seconds in a year,

DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def main():
    second_in_a_year=str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) 

    print("There are " + (second_in_a_year) + " seconds in a year!")

if __name__ == '__main__':
    main()
