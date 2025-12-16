```python
# Import necessary libraries
import os
from google.cloud import firestore
from transformers import pipeline

# Initialize Firestore client
db = firestore.Client()

# Load a pre-trained transformer model for text classification
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define the labels for deep lore and philosophy categories
labels = ["metaphysics", "epistemology", "ontology", "existentialism", "mysticism"]

class DeepLorePhilosophy:
    def __init__(self):
        # Initialize the collection in Firestore where data will be stored
        self.collection_ref = db.collection('Deep_Lore_Philosophy')

    def process_content(self, raw_content):
        """
        Process raw content to classify it into deep lore/philosophy categories.
        
        Args:
            raw_content (str): The raw text content to be processed.

        Returns:
            dict: A dictionary containing the classified category and confidence score.
        """
        # Perform zero-shot classification
        result = classifier(raw_content, labels)
        # Get the highest scoring label
        predicted_label = result['labels'][0]
        score = result['scores'][0]

        return {
            'category': predicted_label,
            'confidence_score': score
        }

    def store_data(self, content, classification_result):
        """
        Store the processed content and its classification result in Firestore.
        
        Args:
            content (str): The original raw text content.
            classification_result (dict): The result of the classification process.

        Returns:
            None
        """
        # Prepare document data to be stored
        doc_data = {
            'raw_content': content,
            'category': classification_result['category'],
            'confidence_score': classification_result['confidence_score']
        }
        
        # Add document to Firestore collection
        self.collection_ref.add(doc_data)

    def handle_incoming_content(self, raw_content):
        """
        Handle incoming raw content by processing and storing it.
        
        Args:
            raw_content (str): The raw text content to be processed.

        Returns:
            None
        """
        # Process the content to get classification result
        classification_result = self.process_content(raw_content)
        # Store the content and its classification result in Firestore
        self.store_data(raw_content, classification_result)

# Example usage
if __name__ == "__main__":
    # Initialize the DeepLorePhilosophy component
    deep_lore_philosophy = DeepLorePhilosophy()
    
    # Simulate incoming raw content
    raw_spinny_content = "The nature of reality is a profound mystery that has puzzled philosophers for centuries."
    
    # Handle the incoming content
    deep_lore_philosophy.handle_incoming_content(raw_spinny_content)
```

### Explanation:
- **Firestore Initialization**: The code initializes a Firestore client to interact with Google Cloud's NoSQL database.
- **Transformer Model**: A pre-trained transformer model (`facebook/bart-large-mnli`) is used for zero-shot classification, which allows the model to classify text into predefined categories without fine-tuning.
- **DeepLorePhilosophy Class**: This class encapsulates the logic for processing content and storing it in Firestore.
  - `process_content`: Uses the transformer model to classify raw content into one of the specified deep lore/philosophy categories.
  - `store_data`: Stores the classified content along with its confidence score in a Firestore collection.
  - `handle_incoming_content`: Orchestrates the processing and storage of incoming raw content.
- **Example Usage**: Demonstrates how to use the `DeepLorePhilosophy` class to handle a piece of raw content.