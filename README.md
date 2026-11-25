# 🛠️ Multi-Utility Toolkit – Python Modules & Packages

A Python-based **Multi-Utility Toolkit** that integrates built-in modules, custom modules, and packages to perform various useful tasks through a menu-driven interface. The project demonstrates Python modular programming, package organization, reusable functions, and dynamic module exploration.

## 📌 Project Overview

The Multi-Utility Toolkit is designed to perform multiple operations using Python's standard library and custom modules. It provides utilities for date and time calculations, mathematical operations, random data generation, unique identifier creation, file handling, and module attribute exploration.

The project emphasizes code reusability, modular structure, and the effective use of Python modules and packages.

## 🎯 Objectives

- Explore and utilize Python built-in modules.
- Implement custom modules and packages.
- Demonstrate the use of `__name__` and `__main__`.
- Perform dynamic module exploration using `dir()`.
- Develop a menu-driven user interface.
- Organize code into reusable and maintainable components.

## ✨ Features

### 📅 1. DateTime & Time Operations
Using Python's `datetime` and `time` modules:

- Display the current date and time.
- Calculate the difference between two dates or times.
- Format dates using `strftime()`.
- Implement a stopwatch.
- Implement a countdown timer.

### 🧮 2. Mathematical Operations
Using Python's `math` module:

- Calculate factorials.
- Solve compound interest problems.
- Perform trigonometric calculations.
- Calculate logarithms and other mathematical operations.
- Calculate the area of geometric shapes.

### 🎲 3. Random Data Generation
Using Python's `random` module:

- Generate random numbers.
- Generate random lists.
- Create random passwords.
- Generate OTPs.
- Simulate random sampling from datasets.
- Perform simple game simulations.

### 🔑 4. Unique Identifier Generation (UUID)
Using Python's `uuid` module:

- Generate unique identifiers.
- Create UUIDs for files, records, and user sessions.
- Demonstrate UUID generation using UUID4.

### 📁 5. File Operations (Custom Module)
Custom module for file handling operations:

- Create new files.
- Write data into files.
- Read file contents.
- Append data to existing files.

### 🔍 6. Dynamic Module Exploration
Using Python's `dir()` function:

- Explore available attributes of built-in modules.
- Display functions, methods, and attributes of modules.
- Dynamically inspect custom and built-in modules.

### 📦 7. Custom Modules & Packages

- Create separate Python files for specific functionalities.
- Organize reusable functions into custom modules.
- Group modules into packages.
- Use `__init__.py` to initialize packages.

### 🖥️ 8. Menu-Driven Interface

- Simple console-based user interface.
- Interactive menus for different operations.
- Easy navigation between modules.
- Option to exit the application.

## 📂 Project Structure

```text
Multi-Utility-Toolkit/
│
├── main.py
│
├── datetime_module.py
├── math_module.py
├── random_module.py
├── uuid_module.py
├── module_explorer.py
│
├── custom_package/
│   ├── __init__.py
│   ├── file_operations.py
│   └── math_utilities.py
│
├── README.md
└── requirements.txt
```

> **Note:** The project structure above is a suggested organization. Adjust the filenames and folders according to your actual source code.

## ⚙️ Technologies Used

- **Programming Language:** Python
- **Modules:** `datetime`, `time`, `math`, `random`, `uuid`
- **Concepts:** Modules, Packages, Functions, File Handling, `__name__`, `__main__`, `dir()`
- **Interface:** Console-based Menu System

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Multi-Utility-Toolkit.git
```

### 2. Navigate to the Project Directory

```bash
cd Multi-Utility-Toolkit
```

### 3. Run the Project

```bash
python main.py
```

> Python 3.x is required. The project primarily uses built-in Python modules, so external dependencies may not be required.

## 📖 How to Use

1. Run `main.py`.
2. Select an option from the main menu.
3. Choose the operation you want to perform.
4. Enter the required inputs.
5. View the result in the console.
6. Return to the main menu to explore other utilities.
7. Select **Exit** to close the application.

## 🧾 Main Menu

```text
==============================
Welcome to Multi-Utility Toolkit
==============================

Choose an option:

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```

## 💡 Example Operations

| Module | Example Operation | Output |
|---|---|---|
| DateTime | Display current date and time | Current date/time |
| DateTime | Difference between dates | Difference in days |
| Math | Factorial of 5 | 120 |
| Math | Compound interest | Calculated interest |
| Random | Generate password | Random password |
| UUID | Generate UUID4 | Unique identifier |
| File Operations | Write and read a file | File contents |
| Module Explorer | Explore `math` attributes | List of module attributes |

## 🧪 Sample Output

### Factorial Calculation

```text
Mathematical Operations:

1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu

Enter your choice: 1

Enter a number: 5
Factorial: 120
```

### Random Password Generation

```text
Random Data Generation:

1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Back to Main Menu

Enter your choice: 3

Enter password length: 8
Generated Password: Kd8@qzP!
```

### UUID Generation

```text
Generate Unique Identifiers:

Generated UUID:
f47ac10b-58cc-4372-a567-0e02b2c3d479
```

### File Operations

```text
File Operations:

1. Create a New File
2. Write to a File
3. Read from a File
4. Append to a File
5. Back to Main Menu

Enter your choice: 1

Enter file name: example.txt
File created successfully!
```

### Dynamic Module Exploration

```text
Explore Module Attributes:

Enter module name to explore: math

Available attributes in math module:
['acos', 'acosh', 'asin', 'asinh', 'atan',
 'atanh', 'ceil', 'comb', 'copysign', 'cos', ...]
```

## 📚 Python Concepts Demonstrated

- Importing built-in modules.
- Creating and using custom modules.
- Creating Python packages.
- Using `__init__.py`.
- Implementing `if __name__ == "__main__":`.
- Using the `dir()` function.
- File creation, reading, writing, and appending.
- Functions and code reusability.
- Menu-driven programming.
- Exception handling and user input validation.

## 📈 Future Enhancements

- Add a graphical user interface (GUI).
- Improve input validation and error handling.
- Add more mathematical and scientific operations.
- Add more file management features.
- Store operation history.
- Add more utility modules.

  ## 🎥 Project Explanation Video

Watch the complete project explanation, including its features, working, and demonstration:

🔗 **Project Video:** 



## 👨‍💻 Author

**Harsh Prajapati**

Python Project – Multi-Utility Toolkit

## 📄 License

This project is created for educational purposes and demonstrates the use of Python modules, packages, and modular programming concepts.
