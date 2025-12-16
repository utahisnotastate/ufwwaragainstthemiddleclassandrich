```python
# Import necessary libraries
from google.cloud import firestore
import re

# Initialize Firestore client
db = firestore.Client()

def process_invention(raw_content):
    """
    Process raw content to extract and categorize inventions.

    Args:
        raw_content (str): The raw text content that may contain invention descriptions.

    Returns:
        list: A list of dictionaries, each representing an invention.
    """
    # Regular expression to identify potential inventions
    invention_pattern = re.compile(r'\b(?:invention|device|contraption|gadget)\s+([\w\s]+)(?=\.)', re.IGNORECASE)
    
    # Find all matches in the raw content
    matches = invention_pattern.findall(raw_content)
    
    # List to store processed inventions
    inventions = []
    
    for match in matches:
        # Clean up the matched text
        invention_name = match.strip()
        
        # Create a dictionary for each invention
        invention = {
            'name': invention_name,
            'description': f'Detailed description of {invention_name} goes here.',
            'status': 'pending',  # Status can be pending, reviewed, approved, etc.
            'date_added': firestore.SERVER_TIMESTAMP
        }
        
        # Append the invention to the list
        inventions.append(invention)
    
    return inventions

def store_inventions(inventions):
    """
    Store processed inventions in Firestore.

    Args:
        inventions (list): A list of dictionaries, each representing an invention.
    """
    for invention in inventions:
        # Add each invention to the 'inventions' collection in Firestore
        db.collection('inventions').add(invention)

def main(raw_content):
    """
    Main function to process raw content and store inventions.

    Args:
        raw_content (str): The raw text content that may contain invention descriptions.
    """
    # Process the raw content to extract inventions
    inventions = process_invention(raw_content)
    
    # Store the extracted inventions in Firestore
    if inventions:
        store_inventions(inventions)

# Example usage
if __name__ == "__main__":
    example_content = "This new gadget can revolutionize home automation. The invention uses AI to learn user preferences."
    main(example_content)
```

### Explanation of the Code:

1. **Imports and Initialization**:
   - Import necessary libraries (`firestore` from `google.cloud` for database operations and `re` for regular expressions).
   - Initialize a Firestore client to interact with Google Cloud Firestore.

2. **Function: `process_invention`**:
   - Takes raw content as input.
   - Uses a regular expression to find potential inventions in the text.
   - Cleans up each match and creates a dictionary for each invention, including fields like name, description, status, and timestamp.
   - Returns a list of these dictionaries.

3. **Function: `store_inventions`**:
   - Takes a list of invention dictionaries as input.
   - Adds each invention to the 'inventions' collection in Firestore.

4. **Main Function**:
   - Processes raw content to extract inventions using `process_invention`.
   - Stores the extracted inventions in Firestore using `store_inventions`.

5. **Example Usage**:
   - Demonstrates how to use the main function with a sample text containing an invention description.