import sqlite3
import os
import glob
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from train import SkinClassifier

# Function to load the filter model
def load_filter_model(model_path, num_classes=2):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = SkinClassifier(num_classes)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model, device

# Function to preprocess an image for the filter model
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
    ])
    
    image = Image.open(image_path).convert('RGB')
    image = transform(image)
    return image.unsqueeze(0)  # Add batch dimension

# Function to get class names for the filter model
def get_filter_class_names():
    # Define the classes for the skin color filter model
    return ['White', 'Not White']

# Function to check if an image is classified as "Not White"
def is_not_white(model, image_tensor, device, threshold=0.7):
    with torch.no_grad():
        image_tensor = image_tensor.to(device)
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        
        # Get the class names
        class_names = get_filter_class_names()
        
        # "Not White" is the second class (index 1)
        not_white_prob = probabilities[0][1].item()
        
        # If the probability of "Not White" is greater than the threshold, consider it "Not White"
        return not_white_prob > threshold

# Load the filter model
print("Loading filter model...")
filter_model_path = os.path.join(os.path.dirname(__file__), 'filter.pth')
filter_model, device = load_filter_model(filter_model_path)
print("Filter model loaded successfully.")

# Open database
conn = sqlite3.connect('../database.db')

# Function to process a folder of images and insert them into the database
def process_folder(folder_path, classification):
    print(f"Processing folder: {folder_path}")
    
    # Get all image files with extensions .jpg, .png, .jpeg
    image_files = glob.glob(os.path.join(folder_path, "*.jpg")) + \
                  glob.glob(os.path.join(folder_path, "*.png")) + \
                  glob.glob(os.path.join(folder_path, "*.jpeg"))
    
    inserted_count = 0
    filtered_count = 0
    
    # Loop through each image file
    for image_path in image_files:
        try:
            # Check if the image is classified as "Not White"
            image_tensor = preprocess_image(image_path)
            if is_not_white(filter_model, image_tensor, device):
                # If it's "Not White", insert it into the database
                with open(image_path, "rb") as image_file:
                    image_data = image_file.read()
                    conn.execute("INSERT INTO skinType (image_data, classification) VALUES (?, ?)", 
                                (image_data, classification))
                inserted_count += 1
            else:
                filtered_count += 1
                print(f"Filtered out: {image_path} (classified as White)")
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
    
    print(f"Folder {folder_path}: {inserted_count} images inserted, {filtered_count} images filtered out")
    return inserted_count, filtered_count

# Process all folders
total_inserted = 0
total_filtered = 0

# Define all the folders to process
folders = [
    ("../datasets/normal", "normal"),
    ("../datasets/acne", "acne"),
    ("../datasets/antopicdermatitis", "atopicdermatitis"),
    ("../datasets/bruise", "bruise"),
    ("../datasets/chickenpox", "chickenpox"),
    ("../datasets/eczema", "eczema"),
    ("../datasets/firstdegburn", "firstdegburns"),
    ("../datasets/herpes", "herpes"),
    ("../datasets/hives", "hives"),
    ("../datasets/impetigo", "impetigo"),
    ("../datasets/melanoma", "melanoma"),
    ("../datasets/monkeypox", "monkeypox"),
    ("../datasets/pimple", "pimple"),
    ("../datasets/psoriasis", "psoriasis"),
    ("../datasets/scabies", "scabies"),
    ("../datasets/seconddegburns", "seconddegburns"),
    ("../datasets/skincancer", "skincancer"),
    ("../datasets/thirddegburns", "thirddegburns"),
    ("../datasets/vitiligo", "vitiligo"),
    ("../datasets/warts", "warts")
]

# Process each folder
for folder_path, classification in folders:
    inserted, filtered = process_folder(folder_path, classification)
    total_inserted += inserted
    total_filtered += filtered

# Commit the changes
conn.commit()

# Close the connection when done
conn.close()

print(f"\nDatabase population complete!")
print(f"Total images inserted: {total_inserted}")
print(f"Total images filtered out: {total_filtered}") 