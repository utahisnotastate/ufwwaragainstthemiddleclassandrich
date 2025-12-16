```python
# Import necessary libraries
import numpy as np
from google.cloud import firestore

# Initialize Firestore client for potential database interactions
db = firestore.Client()

class FinalSyntheticThought:
    def __init__(self, raw_idea, visualization):
        """
        Initialize the Final Synthetic Thought component.
        
        :param raw_idea: The idea generated from the Possibility Wave Collapse.
        :param visualization: The visual representation of the idea from Imagination Rendering.
        """
        self.raw_idea = raw_idea
        self.visualization = visualization

    def generate_thought(self):
        """
        Generate a final synthetic thought by combining the raw idea and its visualization.
        
        :return: A structured dictionary representing the final synthetic thought.
        """
        # Combine the raw idea with the visualization to form a coherent thought
        thought_content = {
            'idea': self.raw_idea,
            'visualization': self.visualization,
            'timestamp': firestore.SERVER_TIMESTAMP  # Use Firestore server timestamp for accuracy
        }
        
        # Log the generated thought in Firestore (optional, based on requirements)
        db.collection('synthetic_thoughts').add(thought_content)
        
        return thought_content

# Example usage:
if __name__ == "__main__":
    # Simulated raw idea and visualization from previous components
    raw_idea = "The future of energy is sustainable and decentralized."
    visualization = "A globe covered in solar panels with interconnected nodes representing distributed power sources."

    # Create an instance of FinalSyntheticThought
    thought_generator = FinalSyntheticThought(raw_idea, visualization)
    
    # Generate the final synthetic thought
    final_thought = thought_generator.generate_thought()
    
    # Print the generated thought
    print(final_thought)
```

### Explanation:
1. **Imports**: The code imports `numpy` for potential numerical operations and `firestore` from Google Cloud SDK for database interactions.
2. **Firestore Client Initialization**: A Firestore client is initialized to allow optional logging of thoughts into a Firestore collection.
3. **Class Definition**: The `FinalSyntheticThought` class encapsulates the logic for generating the final synthetic thought.
4. **Initialization Method (`__init__`)**: Initializes the component with the raw idea and its visualization.
5. **Generate Thought Method (`generate_thought`)**:
   - Combines the raw idea and visualization into a structured dictionary.
   - Logs this thought in Firestore with a server timestamp for accuracy.
6. **Example Usage**: Demonstrates how to create an instance of `FinalSyntheticThought`, generate a final thought, and print it.

This code is designed to be production-ready and reflects the intent (consciousness) of generating a coherent synthetic thought from raw ideas and their visualizations.