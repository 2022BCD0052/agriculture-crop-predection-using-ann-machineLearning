from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML form

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input values from the form
    nitrogen = float(request.form['nitrogen'])
    phosphorous = float(request.form['phosphorous'])
    potassium = float(request.form['potassium'])
    avg_temp = float(request.form['avg_temp'])
    humidity = float(request.form['humidity'])
    soil_ph = float(request.form['soil_ph'])
    rainfall = float(request.form['rainfall'])

    # Prepare input for the model (order matters)
    features = np.array([[nitrogen, phosphorous, potassium, avg_temp, humidity, soil_ph, rainfall]])

    # Make prediction
    prediction = model.predict(features)

    # Return prediction as JSON response
    return render_template('index.html', prediction=prediction[0])

    # return jsonify({'Suggested Crop': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
