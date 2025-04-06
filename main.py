from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
import base64
from PIL import Image
import io
import torch
import json

# Import functions from inference.py
from inference import load_model, preprocess_image, get_class_names, predict_image

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)  # Enable CORS for all routes

# Global variables for model and device
model = None
device = None
class_names = None

def initialize_model():
    global model, device, class_names
    if model is None:
        print("Initializing model...")
        class_names = get_class_names()
        num_classes = len(class_names)
        model, device = load_model('best_model.pth', num_classes)
        print("Model initialized successfully")

# Initialize model when the app starts
initialize_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Check if the request has the image data
        if 'image' not in request.json:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Get the base64 encoded image
        image_data = request.json['image']
        
        # Remove the data URL prefix if present (e.g., "data:image/jpeg;base64,")
        if ',' in image_data:
            image_data = image_data.split(',')[1]
        
        # Decode the base64 image
        image_bytes = base64.b64decode(image_data)
        
        # Convert to PIL Image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Save the image temporarily
        temp_path = 'temp_image.jpg'
        image.save(temp_path)
        
        # Preprocess the image
        image_tensor = preprocess_image(temp_path)
        
        # Get predictions
        probabilities = predict_image(model, image_tensor, device)
        
        # Convert probabilities to a list of dictionaries with class names and probabilities
        results = []
        for class_name, prob in zip(class_names, probabilities):
            results.append({
                'class': class_name,
                'probability': float(prob.item() * 100)  # Convert to percentage
            })
        
        # Sort results by probability in descending order
        results.sort(key=lambda x: x['probability'], reverse=True)
        
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        return jsonify({
            'success': True,
            'results': results
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
