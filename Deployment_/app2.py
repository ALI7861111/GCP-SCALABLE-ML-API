from flask import Flask, request, jsonify
import numpy as np
from catboost import CatBoostClassifier

app = Flask(__name__)

# Load CatBoost model
model = CatBoostClassifier()
model.load_model('catboost_model.bin')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.json
    
    # Convert input data to numpy array
    input_array = np.array(data['input_array']).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_array[0])[0]
    
    # Create response dictionary
    response = {'prediction': prediction}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)