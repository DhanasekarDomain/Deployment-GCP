from flask import Flask, render_template, request
import pickle
import warnings

app = Flask(__name__)

with open("Best_HousePrice_Model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

condition_map = {'Excellent': 1, 'Fair': 2, 'Good': 3, 'Poor': 4}
location_map = {'Downtown': 1, 'Rural': 2, 'Suburban': 3, 'Urban': 4}
garage_map = {'Yes': 1, 'No': 0}

def encode_input(user_input):
    return {
        "Area": float(user_input["Area"]),
        "Bedrooms": int(user_input["Bedrooms"]),
        "Bathrooms": int(user_input["Bathrooms"]),
        "Floors": int(user_input["Floors"]),
        "YearBuilt": int(user_input["YearBuilt"]),
        "Location": location_map[user_input["Location"]],
        "Condition": condition_map[user_input["Condition"]],
        "Garage": garage_map[user_input["Garage"]],
        "Location_ratio": float(user_input["Location_ratio"])
    }

warnings.filterwarnings("ignore", message="X does not have valid feature names, but RandomForestRegressor was fitted with feature names")

@app.route("/")
def home():
    return render_template("input.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = {
        "Area": request.form["Area"],
        "Bedrooms": request.form["Bedrooms"],
        "Bathrooms": request.form["Bathrooms"],
        "Floors": request.form["Floors"],
        "YearBuilt": request.form["YearBuilt"],
        "Location": request.form["Location"],
        "Condition": request.form["Condition"],
        "Garage": request.form["Garage"],
        "Location_ratio": request.form["Location_ratio"]
    }

    processed = encode_input(user_input)
    prediction = loaded_model.predict([list(processed.values())])
    price = round(prediction[0], 2)

    return render_template("output.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)


