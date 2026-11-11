"""
PROJECT: OHM'S LAW AND ELECTRICAL POWER CALCULATOR
AUTHOR: Abigail Micah-Chu
DEPARTMENT: ND1 Mechatronics Engineering
INSTITUTION: Yaba College of Technology
"""

import datetime

# Store calculations made during the current session.
calculation_history = []


def get_number(prompt):
    """Collect a valid non-negative number from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Negative values are not accepted.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_nonzero_number(prompt):
    """Collect a number that is greater than zero."""
    while True:
        value = get_number(prompt)
        if value == 0:
            print("This value cannot be zero.")
        else:
            return value


def display_result(result):
    """Display the result of a calculation."""
    print("\\n" + "=" * 45)
    print("CALCULATION SUCCESSFUL")
    print(result)
    print("=" * 45)


def save_to_history(result):
    """Save a result and its date/time in the history list."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    calculation_history.append(f"{timestamp} - {result}")
    print("Calculation added to history.")


def calculate_voltage():
    """Calculate voltage using V = I x R."""
    print("\\nVOLTAGE CALCULATION: V = I x R")
    current = get_number("Enter current (Amperes): ")
    resistance = get_number("Enter resistance (Ohms): ")
    result = f"Voltage = {current * resistance:.2f} Volts"
    display_result(result)
    return result


def calculate_current():
    """Calculate current using I = V / R."""
    print("\\nCURRENT CALCULATION: I = V / R")
    voltage = get_number("Enter voltage (Volts): ")
    resistance = get_nonzero_number("Enter resistance (Ohms): ")
    result = f"Current = {voltage / resistance:.2f} Amperes"
    display_result(result)
    return result


def calculate_resistance():
    """Calculate resistance using R = V / I."""
    print("\\nRESISTANCE CALCULATION: R = V / I")
    voltage = get_number("Enter voltage (Volts): ")
    current = get_nonzero_number("Enter current (Amperes): ")
    result = f"Resistance = {voltage / current:.2f} Ohms"
    display_result(result)
    return result


def calculate_power():
    """Calculate electrical power using P = V x I."""
    print("\\nPOWER CALCULATION: P = V x I")
    voltage = get_number("Enter voltage (Volts): ")
    current = get_number("Enter current (Amperes): ")
    result = f"Electrical Power = {voltage * current:.2f} Watts"
    display_result(result)
    return result


def view_history():
    """Display calculations made during this session."""
    print("\\nCALCULATION HISTORY")
    if not calculation_history:
        print("No calculations have been recorded.")
    else:
        for number, record in enumerate(calculation_history, start=1):
            print(f"{number}. {record}")


def clear_history():
    """Clear the history after asking for confirmation."""
    if not calculation_history:
        print("There is no history to clear.")
        return

    answer = input("Clear all calculation history? (yes/no): ").strip().lower()
    if answer == "yes":
        calculation_history.clear()
        print("History cleared.")
    else:
        print("Operation cancelled.")


def export_history():
    """Append the current session's history to a text file."""
    if not calculation_history:
        print("There is no history to save.")
        return

    try:
        with open("calculation_history.txt", "a", encoding="utf-8") as file:
            file.write("\\nELECTRICAL CALCULATION RECORDS\\n")
            for record in calculation_history:
                file.write(record + "\\n")
        print("History saved to calculation_history.txt.")
    except OSError:
        print("Error: Unable to save the history file.")


def formula_guide():
    """Show the formulas and their measurement units."""
    print("\\nELECTRICAL FORMULA GUIDE")
    print("Voltage:     V = I x R  (Volts)")
    print("Current:     I = V / R  (Amperes)")
    print("Resistance:  R = V / I  (Ohms)")
    print("Power:       P = V x I  (Watts)")
    print("V = Voltage, I = Current, R = Resistance, P = Power")


def main_menu():
    """Display the menu and run the selected operation."""
    while True:
        print("\\n" + "=" * 50)
        print("OHM'S LAW AND ELECTRICAL POWER CALCULATOR")
        print("=" * 50)
        print("1. Calculate Voltage")
        print("2. Calculate Current")
        print("3. Calculate Resistance")
        print("4. Calculate Electrical Power")
        print("5. View Calculation History")
        print("6. Save History to File")
        print("7. Clear Calculation History")
        print("8. View Formula Guide")
        print("9. Exit")

        choice = input("Select an option (1-9): ").strip()

        if choice == "1":
            save_to_history(calculate_voltage())
        elif choice == "2":
            save_to_history(calculate_current())
        elif choice == "3":
            save_to_history(calculate_resistance())
        elif choice == "4":
            save_to_history(calculate_power())
        elif choice == "5":
            view_history()
        elif choice == "6":
            export_history()
        elif choice == "7":
            clear_history()
        elif choice == "8":
            formula_guide()
        elif choice == "9":
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid selection. Choose a number from 1 to 9.")


# Start the program.
if __name__ == "__main__":
    print("Welcome, Abigail Micah-Chu!")
    main_menu()
