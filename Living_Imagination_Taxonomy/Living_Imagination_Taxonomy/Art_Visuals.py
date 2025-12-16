```python
# Import necessary libraries
import os
from google.cloud import storage
from PIL import Image
import io
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

# Initialize Google Cloud Storage client
storage_client = storage.Client()

# Define the bucket name where images will be stored and retrieved
BUCKET_NAME = 'living_imagination_taxonomy_images'

def download_image_from_gcs(image_name):
    """
    Download an image from Google Cloud Storage.
    
    Args:
        image_name (str): The name of the image file to download.
        
    Returns:
        Image: A PIL Image object.
    """
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(image_name)
    image_data = blob.download_as_bytes()
    return Image.open(io.BytesIO(image_data))

def preprocess_image(image):
    """
    Preprocess the image for ResNet50 model input.
    
    Args:
        image (Image): A PIL Image object.
        
    Returns:
        np.array: Preprocessed image array.
    """
    image = image.resize((224, 224))
    image_array = np.array(image)
    image_array_expanded = np.expand_dims(image_array, axis=0)
    return preprocess_input(image_array_expanded)

def predict_image_category(image_array):
    """
    Predict the category of an image using ResNet50 model.
    
    Args:
        image_array (np.array): Preprocessed image array.
        
    Returns:
        list: List of predicted categories with probabilities.
    """
    model = ResNet50(weights='imagenet')
    predictions = model.predict(image_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    return decoded_predictions

def categorize_art_visuals(image_name):
    """
    Categorize an art/visual image based on its content.
    
    Args:
        image_name (str): The name of the image file to categorize.
        
    Returns:
        list: List of predicted categories with probabilities.
    """
    # Download and preprocess the image
    image = download_image_from_gcs(image_name)
    preprocessed_image = preprocess_image(image)
    
    # Predict the category of the image
    predictions = predict_image_category(preprocessed_image)
    
    return predictions

# Example usage
if __name__ == "__main__":
    image_name = 'example_artwork.jpg'
    categories = categorize_art_visuals(image_name)
    for (imagenet_id, label, score) in categories:
        print(f"Label: {label}, Score: {score:.2f}")
```

### Explanation of the Code:

1. **Imports**:
   - `os`: For environment variable management.
   - `google.cloud.storage`: To interact with Google Cloud Storage.
   - `PIL.Image`: For image processing.
   - `io.BytesIO`: To handle byte streams for images.
   - `numpy`: For numerical operations.
   - `tensorflow` and `resnet50`: For deep learning model predictions.

2. **Google Cloud Storage Client**:
   - Initializes the client to interact with GCS.

3. **Bucket Name**:
   - Specifies the bucket where images are stored.

4. **download_image_from_gcs**:
   - Downloads an image from GCS and returns it as a PIL Image object.

5. **preprocess_image**:
   - Resizes and preprocesses the image for input into the ResNet50 model.

6. **predict_image_category**:
   - Loads the ResNet50 model, makes predictions on the preprocessed image, and decodes the results.

7. **categorize_art_visuals**:
   - Orchestrates the process of downloading, preprocessing, and predicting the category of an art/visual image.

8. **Example Usage**:
   - Demonstrates how to use the `categorize_art_visuals` function with a sample image file.