```python
# Import necessary libraries
import numpy as np
from google.cloud import firestore

# Initialize Firestore client for potential cloud storage needs
db = firestore.Client()

class PossibilityWaveCollapse:
    def __init__(self):
        # Initialize with default parameters
        self.random_seed = None
        self.global_constraints = {}
    
    def set_random_seed(self, seed):
        """
        Set the random seed for reproducibility.
        
        :param seed: Integer value to seed the random number generator
        """
        np.random.seed(seed)
        self.random_seed = seed
    
    def set_global_constraints(self, constraints):
        """
        Set global constraints that will influence the wave collapse process.
        
        :param constraints: Dictionary of constraints
        """
        self.global_constraints = constraints
    
    def generate_raw_idea(self):
        """
        Generate a raw idea by collapsing the possibility wave based on random noise and constraints.
        
        :return: A dictionary representing the raw idea
        """
        # Example constraint application: limit the range of possible ideas
        min_value = self.global_constraints.get('min_value', 0)
        max_value = self.global_constraints.get('max_value', 100)
        
        # Generate random noise within the constrained range
        random_noise = np.random.uniform(min_value, max_value)
        
        # Construct a raw idea dictionary (this can be expanded with more complex structures)
        raw_idea = {
            'id': np.random.randint(1, 10000),
            'value': random_noise,
            'description': f"Generated idea with value {random_noise}"
        }
        
        return raw_idea

# Example usage
if __name__ == "__main__":
    # Initialize the Possibility Wave Collapse component
    gen_1 = PossibilityWaveCollapse()
    
    # Set a random seed for reproducibility
    gen_1.set_random_seed(42)
    
    # Define global constraints
    constraints = {
        'min_value': 10,
        'max_value': 90
    }
    gen_1.set_global_constraints(constraints)
    
    # Generate a raw idea
    raw_idea = gen_1.generate_raw_idea()
    print(raw_idea)
```

This code defines the `PossibilityWaveCollapse` class, which is responsible for generating raw ideas by collapsing the possibility wave. It uses random noise within specified constraints to create these ideas. The class includes methods to set a random seed and global constraints, as well as to generate a raw idea. Firestore from Google Cloud Platform is initialized but not used in this snippet; it can be integrated for storing generated ideas if needed.