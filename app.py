from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from form
        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        floors = int(request.form["floors"])
        age = int(request.form["age"])

        # Convert to numpy array and reshape for prediction
        features = np.array([[area, bedrooms, bathrooms, floors, age]])
        prediction = model.predict(features)[0]

        return render_template("result.html", price=round(prediction, 2))

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
