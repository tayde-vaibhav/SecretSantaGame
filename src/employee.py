class Employee:
    """Represents an employee with a name and email address."""
    
    def __init__(self, name: str, email: str):
        """Initialize an Employee with name and email.
        
        Args:
            name: Employee's full name.
            email: Employee's email address.
            
        Raises:
            ValueError: If name is empty or email is invalid.
        """
        if not name.strip():
            raise ValueError("Employee name cannot be empty")
        if not self._is_valid_email(email):
            raise ValueError(f"Invalid email address: {email}")
            
        self.name = name.strip()
        self.email = email.strip()
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Validate email address format.
        
        Args:
            email: Email address to validate.
            
        Returns:
            bool: True if email is valid, False otherwise.
        """
        # Basic email validation: contains @ and . with non-empty parts
        if not email or '@' not in email or '.' not in email:
            return False
        local, domain = email.split('@', 1)
        return bool(local and domain and '.' in domain)
    
    def __eq__(self, other) -> bool:
        """Compare employees based on email (unique identifier).
        
        Args:
            other: Another Employee object.
            
        Returns:
            bool: True if emails match, False otherwise.
        """
        if not isinstance(other, Employee):
            return False
        return self.email == other.email
    
    def __hash__(self) -> int:
        """Generate hash based on email for use in sets/dicts."""
        return hash(self.email)
    
    def __repr__(self) -> str:
        """String representation of the Employee."""
        return f"Employee(name='{self.name}', email='{self.email}')"