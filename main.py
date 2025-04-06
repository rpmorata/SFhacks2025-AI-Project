from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torchvision.transforms as transforms
from PIL import Image
import io
import os
import sys
import tempfile

# Import your inference module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from inference import load_model, preprocess_image, predict_image, get_class_names

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get class names and number of classes
class_names = get_class_names()
num_classes = len(class_names)

# Load the model at startup
model_path = 'best_model.pth'  # Update this to your model path
model, device = load_model(model_path, num_classes)
model.eval()  # Set to evaluation mode

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        # Check if image file is present in the request
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        # Get the image file
        image_file = request.files['image']
        
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            image_file.save(temp_file.name)
            temp_path = temp_file.name
        
        try:
            # Preprocess the image using the function from inference.py
            image_tensor = preprocess_image(temp_path)
            
            # Perform inference
            probabilities = predict_image(model, image_tensor, device)
            
            # Convert probabilities to a dictionary with class names
            results = {class_name: float(prob) for class_name, prob in zip(class_names, probabilities)}
            
            return jsonify({
                'success': True,
                'result': results
            })
        
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
