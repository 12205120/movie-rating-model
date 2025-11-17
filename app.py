from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Movie Rating Prediction Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Placeholder for actual prediction logic
    return jsonify({
        "status": "success",
        "prediction": "7.5 stars"
    })

if __name__ == '__main__':
    app.run(debug=True)
