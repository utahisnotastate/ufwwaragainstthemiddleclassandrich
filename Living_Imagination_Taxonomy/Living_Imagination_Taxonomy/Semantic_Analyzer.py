```python
# Import necessary libraries
from google.cloud import language_v1
from google.oauth2 import service_account

# Define the Semantic Analyzer class
class SemanticAnalyzer:
    def __init__(self, credentials_file):
        # Initialize the Google Cloud Natural Language client with credentials
        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self.client = language_v1.LanguageServiceClient(credentials=credentials)

    def analyze_content(self, text):
        """
        Analyzes the content of a given text to categorize it into Inventions, Art/Visuals, or Deep Lore/Philosophy.
        
        Args:
            text (str): The raw text input from THOUGHT node.
            
        Returns:
            str: Category of the text ('Inventions', 'Art/Visuals', 'Deep Lore/Philosophy').
        """
        # Create a document object with the provided text
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        
        # Perform sentiment analysis to understand the emotional tone of the text
        sentiment = self.client.analyze_sentiment(request={'document': document}).document_sentiment.score
        
        # Perform entity analysis to identify key entities in the text
        entities = self.client.analyze_entities(request={'document': document}).entities
        
        # Determine the category based on the content and entities
        if any(entity.type_ == language_v1.Entity.Type.TECHNOLOGY for entity in entities):
            return 'Inventions'
        elif any(entity.type_ == language_v1.Entity.Type.ARTWORK or entity.type_ == language_v1.Entity.Type.ORGANIZATION for entity in entities):
            return 'Art/Visuals'
        else:
            if sentiment < 0:  # Negative sentiment might indicate deep philosophical content
                return 'Deep Lore/Philosophy'
            else:
                return 'Deep Lore/Philosophy' if len(entities) == 0 or all(entity.salience < 0.1 for entity in entities) else 'Art/Visuals'

# Example usage
if __name__ == "__main__":
    # Initialize the Semantic Analyzer with your Google Cloud credentials file path
    analyzer = SemanticAnalyzer('path/to/your/service-account-file.json')
    
    # Sample text input from THOUGHT node
    sample_text = "The latest advancements in quantum computing are revolutionizing our understanding of reality."
    
    # Analyze the content and print the category
    category = analyzer.analyze_content(sample_text)
    print(f"Category: {category}")
```

### Explanation:
- **Google Cloud Natural Language API**: This component uses Google Cloud's Natural Language API for sentiment and entity analysis.
- **Sentiment Analysis**: Helps in understanding the emotional tone of the text, which can be indicative of philosophical content if negative.
- **Entity Analysis**: Identifies key entities in the text. The presence of technological entities categorizes the text as 'Inventions', while artistic or organizational entities suggest 'Art/Visuals'.
- **Category Determination**: Based on the analysis, the text is categorized into one of three categories: 'Inventions', 'Art/Visuals', or 'Deep Lore/Philosophy'.