def main() -> None:
    # Asks the user to enter their birth year
    # Converts the input into an integer using int()
    birth_year: int = int(input("Enter your birth year (ex: 2000): "))

    # Display a message showing the birth year in format: "Your birth year is: XXXX"
    print("Your birth year is: " + str(birth_year))

    # What is Typecasting in Python?
    # The process of changing a variable from one data type to another

    print("Data type of birth_year variable is: " + str(type(birth_year)))


if __name__ == "__main__":
    main()
