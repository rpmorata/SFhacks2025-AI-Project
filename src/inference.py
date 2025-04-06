import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import argparse
from train import SkinClassifier
import sqlite3
import os

def load_model(model_path, num_classes):
    # Check if model file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model file '{model_path}' not found. "
            f"Please train the model first by running 'python src/train.py'"
        )
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = SkinClassifier(num_classes)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model, device

def preprocess_image(image_path):
    # Check if image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' not found.")
    
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
    ])
    
    image = Image.open(image_path).convert('RGB')
    image = transform(image)
    return image.unsqueeze(0)  # Add batch dimension

def get_class_names():
    # Define all possible classifications from the database schema
    # This matches the ENUM in the database creation script
    return ['White', 'Not White']

def predict_image(model, image_tensor, device):
    with torch.no_grad():
        image_tensor = image_tensor.to(device)
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
    return probabilities[0]  # Remove batch dimension

def main():
    parser = argparse.ArgumentParser(description='Skin Condition Classification')
    parser.add_argument('--image', type=str, required=True, help='Path to the input image')
    parser.add_argument('--model', type=str, default='src/best_model.pth', help='Path to the trained model')
    args = parser.parse_args()

    try:
        # Get class names from database schema
        class_names = get_class_names()
        num_classes = len(class_names)

        # Load model and preprocess image
        print(f"Loading model from {args.model}...")
        model, device = load_model(args.model, num_classes)
        
        print(f"Processing image: {args.image}")
        image_tensor = preprocess_image(args.image)
        
        # Get predictions
        probabilities = predict_image(model, image_tensor, device)
        
        # Print results
        print("\nClassification Results:")
        print("-" * 40)
        for class_name, prob in zip(class_names, probabilities):
            print(f"{class_name}: {prob.item()*100:.2f}%")
        print("-" * 40)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        if "Model file" in str(e):
            print("\nTo train the model, run:")
            print("python src/train.py")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
