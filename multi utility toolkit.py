import datetime
import time
import math
import random
import string
import uuid

# =========================
# DATETIME AND TIME TOOLS
# =========================
def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Date and Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif choice == "2":
            try:
                date1 = datetime.date.fromisoformat(input("Enter first date (YYYY-MM-DD): "))
                date2 = datetime.date.fromisoformat(input("Enter second date (YYYY-MM-DD): "))
                print("Difference:", abs((date2 - date1).days), "days")
            except ValueError:
                print("Invalid date format.")
        elif choice == "3":
            fmt = input("Enter format (e.g. %d-%m-%Y %I:%M %p): ")
            print("Formatted Date:", datetime.datetime.now().strftime(fmt))
        elif choice == "4":
            input("Press Enter to start stopwatch...")
            start = time.perf_counter()
            input("Press Enter to stop...")
            print(f"Elapsed time: {time.perf_counter() - start:.2f} seconds")
        elif choice == "5":
            try:
                seconds = int(input("Enter countdown seconds: "))
                if seconds < 0:
                    print("Seconds cannot be negative.")
                    continue
                while seconds > 0:
                    print(f"Time remaining: {seconds}", end="\r", flush=True)
                    time.sleep(1)
                    seconds -= 1
                print("Time's up!             ")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


# =========================
# MATHEMATICAL TOOLS
# =========================
def compound_interest(principal, rate, years, frequency=1):
    amount = principal * (1 + rate / (100 * frequency)) ** (frequency * years)
    return amount - principal

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Unit Conversion")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                n = int(input("Enter a non-negative integer: "))
                if n < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("Factorial:", math.factorial(n))
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "2":
            try:
                p = float(input("Enter principal amount: "))
                r = float(input("Enter rate of interest (%): "))
                t = float(input("Enter time (years): "))
                if p < 0 or r < 0 or t < 0:
                    print("Values cannot be negative.")
                    continue
                ci = compound_interest(p, r, t)
                print(f"Compound Interest: {ci:.2f}")
                print(f"Total Amount: {p + ci:.2f}")
            except ValueError:
                print("Enter valid numeric values.")
        elif choice == "3":
            try:
                degree = float(input("Enter angle in degrees: "))
                rad = math.radians(degree)
                print(f"sin({degree}) = {math.sin(rad):.6f}")
                print(f"cos({degree}) = {math.cos(rad):.6f}")
                print(f"tan({degree}) = {math.tan(rad):.6f}")
            except ValueError:
                print("Enter a valid angle.")
        elif choice == "4":
            print("\nArea of Shapes:")
            print("1. Circle  2. Rectangle  3. Triangle  4. Square")
            shape = input("Choose shape: ")
            try:
                if shape == "1":
                    r = float(input("Radius: "))
                    print("Area:", math.pi * r * r if r >= 0 else "Radius cannot be negative.")
                elif shape == "2":
                    l = float(input("Length: "))
                    w = float(input("Width: "))
                    print("Area:", l * w if l >= 0 and w >= 0 else "Dimensions cannot be negative.")
                elif shape == "3":
                    b = float(input("Base: "))
                    h = float(input("Height: "))
                    print("Area:", 0.5 * b * h if b >= 0 and h >= 0 else "Dimensions cannot be negative.")
                elif shape == "4":
                    s = float(input("Side: "))
                    print("Area:", s * s if s >= 0 else "Side cannot be negative.")
                else:
                    print("Invalid shape.")
            except ValueError:
                print("Enter valid dimensions.")
        elif choice == "5":
            print("\nUnit Conversion:")
            print("1. Kilometers to miles")
            print("2. Miles to kilometers")
            print("3. Celsius to Fahrenheit")
            print("4. Fahrenheit to Celsius")
            conversion = input("Choose conversion: ")
            try:
                value = float(input("Enter value: "))
                if conversion == "1":
                    print(f"{value} km = {value * 0.621371:.4f} miles")
                elif conversion == "2":
                    print(f"{value} miles = {value / 0.621371:.4f} km")
                elif conversion == "3":
                    print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
                elif conversion == "4":
                    print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


# =========================
# RANDOM DATA TOOLS
# =========================
def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling from Dataset")
        print("6. Number Guessing Game")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                low = int(input("Minimum: "))
                high = int(input("Maximum: "))
                if low > high:
                    print("Minimum cannot exceed maximum.")
                else:
                    print("Random Number:", random.randint(low, high))
            except ValueError:
                print("Enter valid integers.")
        elif choice == "2":
            try:
                count = int(input("How many numbers? "))
                low = int(input("Minimum: "))
                high = int(input("Maximum: "))
                if count < 0 or low > high:
                    print("Invalid count or range.")
                else:
                    print("Random List:", [random.randint(low, high) for _ in range(count)])
            except ValueError:
                print("Enter valid integers.")
        elif choice == "3":
            try:
                length = int(input("Password length: "))
                if length < 1:
                    print("Length must be at least 1.")
                else:
                    chars = string.ascii_letters + string.digits + string.punctuation
                    print("Generated Password:", "".join(random.choice(chars) for _ in range(length)))
            except ValueError:
                print("Enter a valid length.")
        elif choice == "4":
            try:
                digits = int(input("OTP length (default 6): ") or "6")
                if digits < 1:
                    print("Length must be positive.")
                else:
                    print("Generated OTP:", "".join(str(random.randint(0, 9)) for _ in range(digits)))
            except ValueError:
                print("Enter a valid length.")
        elif choice == "5":
            dataset = [item.strip() for item in input("Enter comma-separated values: ").split(",") if item.strip()]
            try:
                size = int(input("Sample size: "))
                if size < 0 or size > len(dataset):
                    print("Sample size must be within dataset size.")
                else:
                    print("Random Sample:", random.sample(dataset, size))
            except ValueError:
                print("Enter a valid sample size.")
        elif choice == "6":
            secret = random.randint(1, 20)
            print("Guess the number from 1 to 20!")
            while True:
                try:
                    guess = int(input("Your guess: "))
                    if guess == secret:
                        print("Correct! You guessed it.")
                        break
                    print("Too low!" if guess < secret else "Too high!")
                except ValueError:
                    print("Enter a whole number.")
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


# =========================
# UUID TOOLS
# =========================
def uuid_menu():
    while True:
        print("\nGenerate Unique Identifiers (UUID):")
        print("1. Generate UUID4")
        print("2. Generate Multiple UUIDs")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Generated UUID:", uuid.uuid4())
        elif choice == "2":
            try:
                count = int(input("How many UUIDs? "))
                if count < 1:
                    print("Enter a positive quantity.")
                else:
                    for _ in range(count):
                        print(uuid.uuid4())
            except ValueError:
                print("Enter a valid number.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# =========================
# FILE OPERATIONS
# =========================
def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "5":
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice.")
            continue

        filename = input("Enter file name: ").strip()
        if not filename:
            print("Filename cannot be empty.")
            continue
        # Use only the filename (no folder traversal) for basic safety.
        filename = filename.replace("\\", "/").split("/")[-1]
        try:
            if choice == "1":
                open(filename, "a", encoding="utf-8").close()
                print("File created successfully!")
            elif choice == "2":
                data = input("Enter data to write: ")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(data)
                print("Data written successfully!")
            elif choice == "3":
                try:
                    with open(filename, "r", encoding="utf-8") as f:
                        print("\nFile Content:\n" + f.read())
                except FileNotFoundError:
                    print("File does not exist.")
            elif choice == "4":
                data = input("Enter data to append: ")
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(data + "\n")
                print("Data appended successfully!")
        except OSError as error:
            print("File operation error:", error)


# =========================
# DYNAMIC MODULE EXPLORER
# =========================
def explore_module():
    while True:
        name = input("\nEnter module name to explore (or 'back'): ").strip()
        if name.lower() == "back":
            return
        modules = {
            "math": math,
            "random": random,
            "datetime": datetime,
            "time": time,
            "uuid": uuid,
            "string": string
        }
        module = modules.get(name)
        if module is None:
            print("Module not in supported list. Try math, random, datetime, time, uuid, or string.")
        else:
            attributes = dir(module)
            print(f"\nAvailable attributes in {name} module:")
            print(attributes)
            print("Total attributes:", len(attributes))


# =========================
# MAIN MENU / ENTRY POINT
# =========================
def main_menu():
    while True:
        print("\n" + "=" * 34)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 34)
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main_menu()
