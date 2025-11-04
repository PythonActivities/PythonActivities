"""Python does not have a built-in switch statement like other languages.
Instead, developers use if-elif-else statements or dictionary mapping.
From Python 3.10 onwards, a new feature called match-case works similar to switch."""

# Function to convert number into Months of the Year
# Using dictionary mapping like a switch statement
def numbers_to_months(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    # If argument is not in dictionary, return "Invalid Entry"
    return switcher.get(argument, "Invalid Entry")


# Driver Program
if __name__ == "__main__":
    print(numbers_to_months(0))   # Argument 0
    print(numbers_to_months(6))   # Argument 6
    print(numbers_to_months(10))  # Argument 10
    print(numbers_to_months(14))  # Argument 14
