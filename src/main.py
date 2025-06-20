from csv_handler import CSVHandler
from secret_santa_assigner import SecretSantaAssigner

def main():
    """Main function to run the Secret Santa assignment program."""
    try:
        # Read input files
        employees = CSVHandler.read_employees('Employee-List.csv')
        previous_assignments = CSVHandler.read_previous_assignments('Secret-Santa-Game-Result-2023.csv')
        
        # Generate assignments
        assigner = SecretSantaAssigner(employees, previous_assignments)
        assignments = assigner.assign_secret_santas()
        
        # Write output
        CSVHandler.write_assignments('Secret-Santa-Game-Result-2024.csv', assignments)
        print("Secret Santa assignments generated successfully. Output written to Secret-Santa-Game-Result-2024.csv")
        
    except (FileNotFoundError, ValueError, RuntimeError, IOError) as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()