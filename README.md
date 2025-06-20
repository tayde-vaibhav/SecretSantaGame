**Secret Santa Game Solution**

**Overview**

This Python-based solution automates the assignment of Secret Santa pairs for Acme's annual event. It reads employee data from a CSV file, assigns each employee a unique secret child while respecting constraints (no self-assignment, no repeat assignments from the previous year), and generates a new CSV file with the results. The solution is modular, extensible, includes comprehensive unit tests, and follows object-oriented programming (OOP) principles.

**Requirements**

- Python 3.8 or higher
- No external dependencies (uses standard library modules: csv, random, unittest)

**Setup Instructions**

- - Place the provided input files (Employee-List.xlsx, Secret-Santa-Game-Result-2023.xlsx) in the project root, converted to CSV format (see below).

1. **Convert Input Files to CSV**:
    - Save them as Employee-List.csv and Secret-Santa-Game-Result-2023.csv in the project root.

2. **Project Structure**:

secret-santa-game/

├── Employee-List.csv

├── Secret-Santa-Game-Result-2023.csv

├── src/

│ ├── employee.py

│ ├── csv_handler.py

│ ├── secret_santa_assigner.py

│ └── main.py

├── tests/

│ └── test_secret_santa.py

└── README.md

**Running the Program in VSCode**

1. **Open the Project**:
    - Launch VSCode and open the secret-santa-game folder via File > Open Folder.
2. **Run the Program**:
    - Open src/main.py in VSCode.
    - Right-click the file and select Run Python File in Terminal, or use the terminal:

python src/main.py

- The program reads Employee-List.csv and Secret-Santa-Game-Result-2023.csv, generates assignments, and outputs Secret-Santa-Game-Result-2024.csv in the project root.

1. **Run Unit Tests**:
    - In the terminal, navigate to the project root:

cd path/to/SecretSantaGame

- Run tests:

python -m unittest discover -s tests

- Tests verify employee parsing, CSV handling, assignment logic, and constraint enforcement (no self-assignments, no repeats from previous year).

**Code Structure**

- **src/employee.py**: Defines the Employee class with name and email attributes, including email validation.
- **src/csv_handler.py**: Handles reading employee data and previous assignments, and writing results, with error handling.
- **src/secret_santa_assigner.py**: Implements assignment logic, ensuring constraints are met using a randomized approach.
- **src/main.py**: Orchestrates the program flow, integrating all components.
- **tests/test_secret_santa.py**: Contains unit tests for core functionality, including edge cases and error handling.

**Usage**

- Ensure Employee-List.csv and Secret-Santa-Game-Result-2023.csv are in the project root.
- Run src/main.py to generate Secret-Santa-Game-Result-2024.csv.
- The output CSV contains columns: Employee_Name, Employee_EmailID, Secret_Child_Name, Secret_Child_EmailID.

**Error Handling**
- Handles missing or invalid input files.
- Validates CSV headers and data integrity.
- Ensures no self-assignments or repeat assignments from the previous year.
- Raises clear exceptions with actionable messages.

**Version Control**

- Initialize a Git repository in the project root:

git init

git add .

git commit -m "Initial commit: Secret Santa Game solution with tests"

- Push to a remote repository (GitHub) for submission:

git remote add origin &lt;repository-url&gt;

git push -u origin main

**Notes**
- **Testing**: The test_secret_santa.py file creates temporary CSV files for testing and cleans them up afterward. Run tests using python -m unittest discover -s tests to verify functionality.
- **Extensibility**: The modular design supports future enhancements, such as integrating with a RESTful API or cloud storage, aligning with the job’s requirements for modern web technologies and microservices.