# program the speed of light -- C = 299792458 m/s.

C: int = 299792458  
def main():
    while True:
        user_input = input("Enter kilos of mass (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break

        try:
            mass_in_kg: float = float(user_input)  
            energy_in_joules: float = mass_in_kg * (C ** 2)
            print("e = m * C^2...")
            print("m = " + str(mass_in_kg) + " kg")
            print("C = " + str(C) + " m/s")
            print(f"{energy_in_joules} joules of energy!\n")

        except ValueError:
            print("Invalid input. Please enter a numeric value for mass.")

if __name__ == '__main__':
    main()
