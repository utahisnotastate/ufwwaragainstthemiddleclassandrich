```python
# Cross-Reference Engine (LINK)
# This component processes categorized content and indexes it into a master index for retrieval.

from google.cloud import firestore
import logging

# Initialize Firestore client
db = firestore.Client()

class CrossReferenceEngine:
    def __init__(self):
        # Collection names in Firestore
        self.inventions_collection = db.collection('inventions')
        self.art_visuals_collection = db.collection('art_visuals')
        self.deep_lore_philosophy_collection = db.collection('deep_lore_philosophy')
        self.master_index_collection = db.collection('master_index')

    def index_content(self, category, content_id, metadata):
        """
        Indexes the content into the appropriate category collection and updates the master index.
        
        :param category: The category of the content (e.g., 'inventions', 'art_visuals', 'deep_lore_philosophy')
        :param content_id: Unique identifier for the content
        :param metadata: Metadata associated with the content
        """
        # Determine which collection to index based on category
        if category == 'inventions':
            collection = self.inventions_collection
        elif category == 'art_visuals':
            collection = self.art_visuals_collection
        elif category == 'deep_lore_philosophy':
            collection = self.deep_lore_philosophy_collection
        else:
            logging.error(f"Unknown category: {category}")
            return

        # Add content to the respective category collection
        doc_ref = collection.document(content_id)
        doc_ref.set(metadata)

        # Update master index with reference to the new document
        self.update_master_index(category, content_id, metadata)

    def update_master_index(self, category, content_id, metadata):
        """
        Updates the master index with a reference to the newly indexed content.
        
        :param category: The category of the content
        :param content_id: Unique identifier for the content
        :param metadata: Metadata associated with the content
        """
        # Create an entry in the master index
        master_index_entry = {
            'category': category,
            'content_id': content_id,
            'metadata': metadata
        }

        # Add or update the document in the master index collection
        self.master_index_collection.document(content_id).set(master_index_entry)

# Example usage
if __name__ == "__main__":
    engine = CrossReferenceEngine()
    
    # Sample data to be indexed
    sample_metadata_invention = {
        'title': 'Quantum Teleportation Device',
        'description': 'A device that can teleport matter over long distances using quantum entanglement.',
        'inventor': 'Dr. Alice Smith'
    }
    
    sample_metadata_art_visuals = {
        'title': 'Abstract Digital Painting',
        'description': 'An abstract digital painting created using AI algorithms.',
        'artist': 'AI-Artist-23'
    }
    
    sample_metadata_deep_lore_philosophy = {
        'title': 'The Philosophy of Virtual Existence',
        'description': 'A philosophical treatise on the nature of existence in virtual worlds.',
        'author': 'Dr. Bob Johnson'
    }

    # Indexing sample data
    engine.index_content('inventions', 'inv_001', sample_metadata_invention)
    engine.index_content('art_visuals', 'av_001', sample_metadata_art_visuals)
    engine.index_content('deep_lore_philosophy', 'dlp_001', sample_metadata_deep_lore_philosophy)

```

### Explanation:
- **Firestore Client Initialization**: The `CrossReferenceEngine` class initializes a Firestore client to interact with Google Cloud's NoSQL database.
- **Indexing Method**: The `index_content` method determines the appropriate Firestore collection based on the category and adds the content metadata to that collection. It then calls `update_master_index` to add an entry in the master index.
- **Master Index Update**: The `update_master_index` method creates a document in the `master_index` collection with references to all indexed contents, allowing for easy retrieval and cross-referencing.
- **Example Usage**: The script includes example usage where sample metadata is indexed into different categories.