```python
# Logic/Ethics Gate Component for Utah_1_Thought_Autogenerator_Logic_v2
# This component filters raw ideas based on predefined logic and ethical guidelines.

import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogicEthicsGate:
    def __init__(self):
        # Initialize the gate with default rules and constraints
        self.rules = {
            "no_harm": lambda idea: not any(keyword in idea for keyword in ["harm", "injure", "kill"]),
            "positive_outcome": lambda idea: any(keyword in idea for keyword in ["help", "aid", "benefit"]),
            "feasibility": lambda idea: len(idea.split()) > 5,  # Simple heuristic for feasibility
        }

    def filter_idea(self, raw_idea):
        """
        Filters a raw idea based on the defined rules and ethical guidelines.
        
        Parameters:
        - raw_idea (str): The raw idea to be filtered.
        
        Returns:
        - bool: True if the idea passes all filters, False otherwise.
        """
        logging.info(f"Filtering idea: {raw_idea}")
        for rule_name, rule_function in self.rules.items():
            if not rule_function(raw_idea):
                logging.warning(f"Idea failed {rule_name} check.")
                return False
        logging.info("Idea passed all checks.")
        return True

# Example usage
if __name__ == "__main__":
    gate = LogicEthicsGate()
    test_ideas = [
        "A plan to help the homeless with a new shelter.",
        "An idea to create a device that can harm criminals.",
        "A concept for a public art installation that benefits the community."
    ]
    
    for idea in test_ideas:
        if gate.filter_idea(idea):
            print(f"Approved: {idea}")
        else:
            print(f"Rejected: {idea}")
```

### Explanation of the Code:

1. **Logging Configuration**: Sets up logging to track the flow and decisions made by the filter.
2. **LogicEthicsGate Class**:
   - **Initialization (`__init__`)**: Initializes with a set of rules that define what constitutes an acceptable idea.
     - `no_harm`: Ensures the idea does not contain harmful keywords.
     - `positive_outcome`: Ensures the idea contains keywords indicating a positive impact.
     - `feasibility`: A simple heuristic to ensure the idea is detailed enough to be feasible.
   - **filter_idea Method**: Takes a raw idea and checks it against each rule. If any rule fails, the idea is rejected.
3. **Example Usage**: Demonstrates how to use the `LogicEthicsGate` class with some test ideas.

This code ensures that only ideas meeting ethical standards and logical feasibility are approved for further processing.