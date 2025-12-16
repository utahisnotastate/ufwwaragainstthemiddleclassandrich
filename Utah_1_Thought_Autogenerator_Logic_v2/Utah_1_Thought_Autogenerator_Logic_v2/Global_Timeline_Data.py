```python
# Global Timeline Data Component (CONTEXT)
# This component is responsible for fetching and managing global timeline data which serves as constraints for the thought generation process.

from google.cloud import bigquery
import pandas as pd

class GlobalTimelineData:
    def __init__(self, project_id='your-gcp-project-id', dataset_id='timeline_dataset', table_id='global_timeline'):
        """
        Initialize the Global Timeline Data component with GCP BigQuery credentials and dataset details.
        
        :param project_id: Google Cloud Project ID
        :param dataset_id: BigQuery Dataset ID containing timeline data
        :param table_id: BigQuery Table ID for global timeline data
        """
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.client = bigquery.Client(project=self.project_id)
    
    def fetch_timeline_data(self):
        """
        Fetches the latest global timeline data from BigQuery.
        
        :return: DataFrame containing global timeline data
        """
        query = f"""
        SELECT * 
        FROM `{self.project_id}.{self.dataset_id}.{self.table_id}`
        ORDER BY timestamp DESC
        LIMIT 1000;  -- Limiting to the latest 1000 entries for performance reasons
        """
        
        # Execute the query and convert results to a pandas DataFrame
        query_job = self.client.query(query)
        timeline_data = query_job.to_dataframe()
        
        return timeline_data
    
    def get_constraints(self):
        """
        Extracts constraints from the fetched global timeline data.
        
        :return: Dictionary of constraints for thought generation
        """
        # Fetch the latest timeline data
        timeline_data = self.fetch_timeline_data()
        
        # Example constraint extraction logic (can be customized based on actual data schema)
        # For demonstration, let's assume we extract recent significant events and global trends
        significant_events = timeline_data[timeline_data['event_type'] == 'significant_event']['description'].tolist()
        global_trends = timeline_data[timeline_data['event_type'] == 'global_trend']['description'].tolist()
        
        constraints = {
            'significant_events': significant_events,
            'global_trends': global_trends
        }
        
        return constraints

# Example usage:
if __name__ == "__main__":
    # Initialize the Global Timeline Data component
    context = GlobalTimelineData()
    
    # Get constraints for thought generation
    constraints = context.get_constraints()
    print(constraints)
```

### Explanation of the Code:

1. **Initialization (`__init__` method)**:
   - Sets up the connection to Google Cloud BigQuery using the provided project, dataset, and table IDs.
   
2. **Fetching Timeline Data (`fetch_timeline_data` method)**:
   - Constructs a SQL query to fetch the latest entries from the global timeline data table.
   - Executes the query and converts the results into a pandas DataFrame for easy manipulation.

3. **Extracting Constraints (`get_constraints` method)**:
   - Calls `fetch_timeline_data` to get the latest timeline data.
   - Extracts significant events and global trends based on predefined criteria (event types in this example).
   - Returns these constraints as a dictionary, which can be used by other components for thought generation.

### Notes:
- Ensure that the Google Cloud SDK is installed and authenticated on your environment.
- Replace `'your-gcp-project-id'` with your actual GCP project ID.
- Customize the SQL query and constraint extraction logic based on the actual schema of your BigQuery table.