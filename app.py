from flask import Flask, render_template, request
from mlmodel import predict_crop

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(request.form.get(field)) for field in ['Nitrogen', 'Phosphorus', 'Potassium', 'temperature', 'humidity', 'pH', 'rainfall']]
    result = predict_crop(data)
    return render_template('index.html', prediction_text=f"Predicted Crop: {result}")

if __name__ == '__main__':
    app.run(debug=True)