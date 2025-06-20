import random
from typing import List, Dict, Tuple
from employee import Employee

class SecretSantaAssigner:
    """Assigns secret children to employees for the Secret Santa game."""
    
    def __init__(self, employees: List[Employee], previous_assignments: Dict[Employee, Employee] = None):
        """Initialize the assigner with employees and previous assignments.
        
        Args:
            employees: List of Employee objects.
            previous_assignments: Dict mapping employees to their previous secret children.
            
        Raises:
            ValueError: If insufficient employees or invalid assignments.
        """
        if len(employees) < 2:
            raise ValueError("At least two employees are required for Secret Santa")
        self.employees = employees
        self.previous_assignments = previous_assignments or {}
        self.max_attempts = 1000  # Prevent infinite loops
    
    def assign_secret_santas(self) -> List[Tuple[Employee, Employee]]:
        """Generate valid Secret Santa assignments.
        
        Returns:
            List of (giver, receiver) Employee tuples.
            
        Raises:
            RuntimeError: If no valid assignment is possible after max attempts.
        """
        for _ in range(self.max_attempts):
            try:
                assignments = self._try_assign()
                if self._is_valid_assignment(assignments):
                    return assignments
            except ValueError:
                continue
        raise RuntimeError("Unable to generate valid Secret Santa assignments")
    
    def _try_assign(self) -> List[Tuple[Employee, Employee]]:
        """Attempt to create a valid assignment.
        
        Returns:
            List of (giver, receiver) tuples.
            
        Raises:
            ValueError: If assignment fails due to constraints.
        """
        givers = self.employees.copy()
        receivers = self.employees.copy()
        random.shuffle(givers)
        random.shuffle(receivers)
        
        assignments = []
        for giver in givers:
            # Find a valid receiver: not self and not previous assignment
            valid_receivers = [
                r for r in receivers
                if r != giver and (giver not in self.previous_assignments or 
                                  self.previous_assignments[giver] != r)
            ]
            if not valid_receivers:
                raise ValueError("No valid receiver available for giver")
            
            receiver = random.choice(valid_receivers)
            assignments.append((giver, receiver))
            receivers.remove(receiver)
        
        return assignments
    
    def _is_valid_assignment(self, assignments: List[Tuple[Employee, Employee]]) -> bool:
        """Validate the assignments against all constraints.
        
        Args:
            assignments: List of (giver, receiver) tuples.
            
        Returns:
            bool: True if assignments are valid, False otherwise.
        """
        givers = {giver for giver, _ in assignments}
        receivers = {receiver for _, receiver in assignments}
        
        # Check: Each employee is a giver and receiver exactly once
        if set(self.employees) != givers or set(self.employees) != receivers:
            return False
        
        # Check: No self-assignments and no previous assignments
        for giver, receiver in assignments:
            if giver == receiver:
                return False
            if giver in self.previous_assignments and self.previous_assignments[giver] == receiver:
                return False
        
        return True