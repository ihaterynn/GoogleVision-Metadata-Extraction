import os
from google.cloud import vision

# Set up credentials (update with your file path or name)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fluid-fiber-447718-t4-ba2a4cdcd30b.json"

try:
    # Initialize Vision API Client
    client = vision.ImageAnnotatorClient()

    # Test by listing available features (does not consume credits)
    available_features = [
        "FACE_DETECTION",
        "LANDMARK_DETECTION",
        "LOGO_DETECTION",
        "LABEL_DETECTION",
        "TEXT_DETECTION",
        "DOCUMENT_TEXT_DETECTION",
        "SAFE_SEARCH_DETECTION",
        "IMAGE_PROPERTIES",
        "CROP_HINTS",
        "WEB_DETECTION",
        "PRODUCT_SEARCH",
        "OBJECT_LOCALIZATION",
    ]
    
    print("Google Vision API client initialized successfully!")
    print("Available features:")
    for feature in available_features:
        print(f"- {feature}")

except Exception as e:
    print("Error initializing Google Vision API client:")
    print(e)
