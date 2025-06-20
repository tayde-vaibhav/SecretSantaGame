import csv
from typing import List, Dict, Tuple
from employee import Employee

class CSVHandler:
    """Handles reading and writing CSV files for Secret Santa assignments."""
    
    @staticmethod
    def read_employees(file_path: str) -> List[Employee]:
        """Read employee data from a CSV file.
        
        Args:
            file_path: Path to the employee CSV file.
            
        Returns:
            List of Employee objects.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If CSV format is invalid or required headers are missing.
        """
        try:
            with open(file_path, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                # Trim whitespace from headers and validate
                fieldnames = [name.strip() for name in reader.fieldnames]
                if not {'Employee_Name', 'Employee_EmailID'}.issubset(fieldnames):
                    raise ValueError(f"Invalid CSV headers in {file_path}. Expected: Employee_Name Employee_EmailID, Got: {fieldnames}")
                
                employees = []
                for row in reader:
                    try:
                        employee = Employee(row['Employee_Name'].strip(), row['Employee_EmailID'].strip())
                        employees.append(employee)
                    except ValueError as e:
                        raise ValueError(f"Invalid data in {file_path}: {e}")
                
                if not employees:
                    raise ValueError(f"No valid employees found in {file_path}")
                return employees
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
    
    @staticmethod
    def read_previous_assignments(file_path: str) -> Dict[Employee, Employee]:
        """Read previous year's Secret Santa assignments from a CSV file.
        
        Args:
            file_path: Path to the previous assignments CSV file.
            
        Returns:
            Dict mapping Employee to their previous secret child.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If CSV format is invalid or required headers are missing.
        """
        try:
            with open(file_path, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                required_headers = {'Employee_Name', 'Employee_EmailID', 
                                  'Secret_Child_Name', 'Secret_Child_EmailID'}
                fieldnames = [name.strip() for name in reader.fieldnames]
                if not required_headers.issubset(fieldnames):
                    raise ValueError(f"Invalid CSV headers in {file_path}. Expected: {required_headers}, Got: {fieldnames}")
                
                assignments = {}
                for row in reader:
                    try:
                        giver = Employee(row['Employee_Name'].strip(), row['Employee_EmailID'].strip())
                        receiver = Employee(row['Secret_Child_Name'].strip(), row['Secret_Child_EmailID'].strip())
                        assignments[giver] = receiver
                    except ValueError as e:
                        raise ValueError(f"Invalid data in {file_path}: {e}")
                
                return assignments
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
    
    @staticmethod
    def write_assignments(file_path: str, assignments: List[Tuple[Employee, Employee]]) -> None:
        """Write Secret Santa assignments to a CSV file.
        
        Args:
            file_path: Path to the output CSV file.
            assignments: List of (giver, receiver) Employee tuples.
            
        Raises:
            IOError: If writing to the file fails.
        """
        try:
            with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Employee_Name', 'Employee_EmailID',
                                                        'Secret_Child_Name', 'Secret_Child_EmailID'])
                writer.writeheader()
                for giver, receiver in assignments:
                    writer.writerow({
                        'Employee_Name': giver.name,
                        'Employee_EmailID': giver.email,
                        'Secret_Child_Name': receiver.name,
                        'Secret_Child_EmailID': receiver.email
                    })
        except IOError as e:
            raise IOError(f"Failed to write to {file_path}: {e}")