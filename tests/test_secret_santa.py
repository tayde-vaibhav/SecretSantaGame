import unittest
import os
import csv
from src.employee import Employee
from src.csv_handler import CSVHandler
from src.secret_santa_assigner import SecretSantaAssigner

class TestSecretSanta(unittest.TestCase):
    """Unit tests for the Secret Santa game solution."""

    def setUp(self):
        """Set up test data and temporary files."""
        self.test_employees = [
            Employee("Alice Smith", "alice.smith@acme.com"),
            Employee("Bob Jones", "bob.jones@acme.com"),
            Employee("Carol White", "carol.white@acme.com")
        ]
        self.test_employee_csv = "test_employees.csv"
        self.test_previous_csv = "test_previous_assignments.csv"
        self.test_output_csv = "test_output.csv"

        # Create test employee CSV
        with open(self.test_employee_csv, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Employee_Name', 'Employee_EmailID'])
            writer.writeheader()
            for emp in self.test_employees:
                writer.writerow({'Employee_Name': emp.name, 'Employee_EmailID': emp.email})

        # Create test previous assignments CSV
        with open(self.test_previous_csv, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Employee_Name', 'Employee_EmailID',
                                                  'Secret_Child_Name', 'Secret_Child_EmailID'])
            writer.writeheader()
            writer.writerow({
                'Employee_Name': "Alice Smith",
                'Employee_EmailID': "alice.smith@acme.com",
                'Secret_Child_Name': "Bob Jones",
                'Secret_Child_EmailID': "bob.jones@acme.com"
            })

    def tearDown(self):
        """Clean up temporary files."""
        for file in [self.test_employee_csv, self.test_previous_csv, self.test_output_csv]:
            if os.path.exists(file):
                os.remove(file)

    def test_employee_creation(self):
        """Test Employee class initialization and validation."""
        emp = Employee("Test User", "test.user@acme.com")
        self.assertEqual(emp.name, "Test User")
        self.assertEqual(emp.email, "test.user@acme.com")
        
        with self.assertRaises(ValueError):
            Employee("", "test@acme.com")  # Empty name
        with self.assertRaises(ValueError):
            Employee("Test User", "invalid_email")  # Invalid email

    def test_csv_handler_read_employees(self):
        """Test reading employees from CSV."""
        employees = CSVHandler.read_employees(self.test_employee_csv)
        self.assertEqual(len(employees), 3)
        self.assertEqual(employees[0].name, "Alice Smith")
        self.assertEqual(employees[0].email, "alice.smith@acme.com")

        # Test invalid file
        with self.assertRaises(FileNotFoundError):
            CSVHandler.read_employees("nonexistent.csv")

        # Test invalid CSV headers
        with open("invalid.csv", mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Wrong_Header'])
            writer.writeheader()
        with self.assertRaises(ValueError):
            CSVHandler.read_employees("invalid.csv")
        os.remove("invalid.csv")

    def test_csv_handler_read_previous_assignments(self):
        """Test reading previous assignments from CSV."""
        assignments = CSVHandler.read_previous_assignments(self.test_previous_csv)
        alice = Employee("Alice Smith", "alice.smith@acme.com")
        bob = Employee("Bob Jones", "bob.jones@acme.com")
        self.assertIn(alice, assignments)
        self.assertEqual(assignments[alice], bob)

    def test_secret_santa_assigner(self):
        """Test SecretSantaAssigner assignment logic."""
        assigner = SecretSantaAssigner(self.test_employees)
        assignments = assigner.assign_secret_santas()
        
        # Check assignments are valid
        self.assertEqual(len(assignments), 3)
        givers = {giver for giver, _ in assignments}
        receivers = {receiver for _, receiver in assignments}
        self.assertEqual(set(self.test_employees), givers)
        self.assertEqual(set(self.test_employees), receivers)
        
        # Check no self-assignments
        for giver, receiver in assignments:
            self.assertNotEqual(giver, receiver)

    def test_secret_santa_previous_assignments(self):
        """Test SecretSantaAssigner respects previous assignments."""
        previous = CSVHandler.read_previous_assignments(self.test_previous_csv)
        assigner = SecretSantaAssigner(self.test_employees, previous)
        assignments = assigner.assign_secret_santas()
        
        alice = Employee("Alice Smith", "alice.smith@acme.com")
        bob = Employee("Bob Jones", "bob.jones@acme.com")
        for giver, receiver in assignments:
            if giver == alice:
                self.assertNotEqual(receiver, bob)  # Alice should not be assigned Bob again

    def test_csv_handler_write_assignments(self):
        """Test writing assignments to CSV."""
        assignments = [(self.test_employees[0], self.test_employees[1])]
        CSVHandler.write_assignments(self.test_output_csv, assignments)
        
        with open(self.test_output_csv, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]['Employee_Name'], "Alice Smith")
            self.assertEqual(rows[0]['Secret_Child_Name'], "Bob Jones")

if __name__ == '__main__':
    unittest.main()