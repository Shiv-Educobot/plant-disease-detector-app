from flask import Flask, request, jsonify
from flask_cors import CORS
from generatePlantDiseaseInformation import generatePlantDiseaseInformation
import logging
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load configuration from environment variables or default to development
app.config.from_mapping(
    DEBUG=os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1', 't'],
    ENV=os.getenv('FLASK_ENV', 'production')
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/analyse_plant_image', methods=['POST'])
def analyse_plant_image():
    try:
        data = request.get_json()
        if 'base64_image' not in data:
            return jsonify({'error': 'No base64_image key in JSON'}), 400
        
        base64_image = data['base64_image']
        response = generatePlantDiseaseInformation(base64_image)
        # Process the base64_image as needed
        return jsonify({'response': response}), 200
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=int(os.getenv('PORT', 8080)))


