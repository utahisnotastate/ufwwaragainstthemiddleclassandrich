```python
# The Master Index (Auto-Updated)
# Component ID: DISPLAY
# Type: db
# Language: Python
# Description: This component is responsible for maintaining an auto-updated master index of categorized content.

from google.cloud import firestore
import json

# Initialize Firestore client
db = firestore.Client()

class MasterIndex:
    def __init__(self):
        # Reference to the 'master_index' collection in Firestore
        self.collection_ref = db.collection('master_index')

    def update_index(self, category, item_id, data):
        """
        Update or add an item to the master index.

        :param category: The category of the item (e.g., Inventions, Art/Visuals, Deep Lore/Philosophy)
        :param item_id: Unique identifier for the item
        :param data: Dictionary containing the item's data
        """
        # Create a document reference with the item_id in the specified category subcollection
        doc_ref = self.collection_ref.document(category).collection('items').document(item_id)

        # Set or update the document with the provided data
        doc_ref.set(data, merge=True)
        print(f"Updated index for {category}/{item_id}")

    def get_index(self, category=None):
        """
        Retrieve items from the master index.

        :param category: The category to retrieve (None retrieves all categories)
        :return: Dictionary of items in the specified category or all categories
        """
        if category:
            # Get documents from a specific category subcollection
            docs = self.collection_ref.document(category).collection('items').stream()
        else:
            # Get documents from all categories
            docs = []
            for cat_doc in self.collection_ref.stream():
                items = cat_doc.reference.collection('items').stream()
                docs.extend(items)

        # Convert Firestore documents to a dictionary
        index_data = {}
        for doc in docs:
            if category:
                index_data[doc.id] = doc.to_dict()
            else:
                cat_name = doc.reference.parent.parent.id
                if cat_name not in index_data:
                    index_data[cat_name] = {}
                index_data[cat_name][doc.id] = doc.to_dict()

        return index_data

    def delete_item(self, category, item_id):
        """
        Delete an item from the master index.

        :param category: The category of the item
        :param item_id: Unique identifier for the item
        """
        # Create a document reference and delete it
        doc_ref = self.collection_ref.document(category).collection('items').document(item_id)
        doc_ref.delete()
        print(f"Deleted {category}/{item_id} from index")

# Example usage
if __name__ == "__main__":
    master_index = MasterIndex()

    # Update the index with a new item in the 'Inventions' category
    master_index.update_index('Inventions', 'invention_001', {'name': 'Quantum Teleporter', 'description': 'A device for instantaneous transportation'})

    # Retrieve and print all items from the 'Inventions' category
    inventions = master_index.get_index('Inventions')
    print("Inventions:", json.dumps(inventions, indent=2))

    # Delete an item from the 'Inventions' category
    master_index.delete_item('Inventions', 'invention_001')

    # Retrieve and print all items from all categories
    full_index = master_index.get_index()
    print("Full Index:", json.dumps(full_index, indent=2))
```

### Explanation:
- **Firestore Client Initialization**: The `firestore.Client()` initializes a connection to Google Cloud Firestore.
- **MasterIndex Class**: This class manages the master index stored in Firestore.
  - **update_index**: Adds or updates an item in the specified category.
  - **get_index**: Retrieves items from the specified category or all categories if none is provided.
  - **delete_item**: Deletes a specific item from the specified category.
- **Example Usage**: Demonstrates how to use the `MasterIndex` class to update, retrieve, and delete items.