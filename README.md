# Student Result Manager

A simple, beginner-friendly **Student Result Manager** built using Python. This project allows users to add student records, view their marks, calculate percentages, and save records to a text file so they can be accessed the next time the program runs.

```text
   _____ _             _            _   
  / ____| |           | |          | |  
 | (___ | |_ _   _  __| | ___ _ __ | |_ 
  \___ \| __| | | |/ _` |/ _ \ '_ \| __|
  ____) | |_| |_| | (_| |  __/ | | | |_ 
 |_____/ \__|\__,_|\__,_|\___|_| |_|\__|

       +--------------------------------+
       |     STUDENT RESULT MANAGER     |
       +--------------------------------+
       |  1. Add Student                |
       |  2. View Students              |
       |  3. Exit                       |
       +--------------------------------+
             Built with Python
```

## Features

- **Add Students:** Enter the name and marks of multiple students.
- **View Student Records:** Display student names and their subject-wise marks.
- **Calculate Percentages:** Automatically calculate the average percentage across Physics, Chemistry, and Mathematics.
- **Save Records:** Store student data in a local `students.txt` file.
- **Load Records:** Automatically load previously saved records when the program starts.
- **Simple Menu:** Navigate through the application using a command-line menu.
- **Basic Error Handling:** Handle missing data files without crashing.

## Technologies Used

- **Language:** Python 3
- **Data Storage:** Text file (`students.txt`)
- **Concepts:** Lists, dictionaries, functions, loops, conditionals, file handling, exception handling, and string formatting.

## Project Structure

```text
Student-Result-Manager/
│
├── student_result_manager.py   # Main Python program
├── students.txt                # Student records (created automatically)
└── README.md                   # Project documentation
```

## Getting Started

### Prerequisites

- Python 3 installed on your computer.
- A code editor such as VS Code (optional).

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Student-Result-Manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Student-Result-Manager
   ```

3. Run the program:

   ```bash
   python student_result_manager.py
   ```

   On some systems, you may need to use `python3` instead of `python`.

## How to Use

After launching the program, you'll see the following menu:

```text
===== Student Result Manager =====
1. Add Student
2. View Students
3. Exit
Enter your choice:
```

- Enter `1` to add student records.
- Enter `2` to display all saved student records.
- Enter `3` to exit the program.

Student records are saved in `students.txt` and loaded automatically on the next launch.

## Example Output

```text
Student Records
----------------------------
Name: Rahul
Physics: 85
Chemistry: 90
Math: 95
Percentage: 90.0
```

## Percentage Calculation

The program calculates the percentage using the average of the three subject marks:

```python
total = physics + chemistry + math
percentage = total / 3
```

This assumes that each subject is marked out of 100.

## Learning Objectives

This project was created to practise fundamental Python programming concepts, including:

- Working with lists and dictionaries.
- Creating reusable functions.
- Taking user input.
- Using loops and conditional statements.
- Reading from and writing to files.
- Handling exceptions.
- Organizing a small command-line application.

## Future Improvements

Possible features to add in future versions:

- Input validation for marks and menu choices.
- Unique student IDs or roll numbers.
- Search, update, and delete student records.
- Grade calculation and pass/fail status.
- Sorting students by percentage.
- Exporting records to CSV.
- A database using SQLite.
- A graphical user interface.

BY LAkshya :)
