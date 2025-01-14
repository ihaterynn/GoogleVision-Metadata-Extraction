import os
import random
import json
from google.cloud import vision

# Set the credentials for Google Vision API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fluid-fiber-447718-t4-ba2a4cdcd30b.json"

# Initialize Vision API Client
client = vision.ImageAnnotatorClient()

# Test the client
print("Google Vision API client initialized successfully.")

# Define Input Dataset and Otput JSON Paths 
input_folder = "./Rezised Wallpapers/"  
output_file = "./results/output.json"

# Function to Select 50% of Images Randomly
def select_images(folder_path, percentage=0.5):
    all_images = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png"))]
    selected_images = random.sample(all_images, int(len(all_images) * percentage))
    return selected_images

# Function to Process Images
def process_images(folder_path, selected_images, output_file):
    results = []
    for file_name in selected_images:
        image_path = os.path.join(folder_path, file_name)

        # Read the image
        with open(image_path, "rb") as image_file:
            content = image_file.read()

        # Create Vision API request
        image = vision.Image(content=content)
        response = client.annotate_image({
            "image": {"content": content},
            "features": [
                {"type": "LABEL_DETECTION"},
                {"type": "IMAGE_PROPERTIES"}
            ],
        })

        # Extract labels
        labels = [
            {"description": label.description, "score": label.score}
            for label in response.label_annotations
        ]

        # Extract dominant colors
        if response.image_properties_annotation.dominant_colors:
            colors = [
                {
                    "color": {
                        "red": color.color.red,
                        "green": color.color.green,
                        "blue": color.color.blue,
                    },
                    "score": color.score,
                }
                for color in response.image_properties_annotation.dominant_colors.colors
            ]
        else:
            colors = []

        # Append results
        results.append({"file_name": file_name, "labels": labels, "colors": colors})

    # Save results to JSON
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Processing complete. Results saved to {output_file}")

# Select 50% of Images
selected_images = select_images(input_folder)

# Process and Extract Metadata
process_images(input_folder, selected_images, output_file)
