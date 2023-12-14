# from flask import Flask, render_template, request, url_for


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         # Retrieve input values from the form
#         gender = request.form['gender']
#         married = request.form['married']
#         dependents = request.form['dependents']
#         education = request.form['education']
#         self_employed = request.form['self_employed']
#         applicant_income = request.form['applicant_income']
#         coapplicant_income = request.form['coapplicant_income']
#         loan_amount = request.form['loan_amount']
#         loan_amount_term = request.form['loan_amount_term']
#         credit_history = request.form['credit_history']
#         property_area = request.form['property_area']

#         # Replace this with your actual machine learning prediction logic
#         # For now, use a simple random prediction
#         import random
#         loan_status = random.choice(["Approved", "Rejected"])

#         return render_template('result.html', loan_status=loan_status)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the pre-trained KNN model
with open('knn_model.pkl', 'rb') as model_file:
    knn_model = pickle.load(model_file)

# Load the pre-trained StandardScaler
with open('standard_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve input values from the form
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicant_income = float(request.form['applicant_income'])
        coapplicant_income = float(request.form['coapplicant_income'])
        loan_amount = float(request.form['loan_amount'])
        loan_amount_term = float(request.form['loan_amount_term'])
        credit_history = float(request.form['credit_history'])
        property_area = request.form['property_area']

        # Prepare the input features for prediction
        input_features = [[gender, married, dependents, education, self_employed,
                           applicant_income, coapplicant_income, loan_amount,
                           loan_amount_term, credit_history, property_area]]

        # Assuming indices for numeric features
        numeric_feature_indices = [5, 6, 7, 8, 9]
        # Extract numeric features
        input_features_numeric = [float(input_features[0][i]) for i in numeric_feature_indices]

        # Standardize numeric features using the loaded StandardScaler
        input_features_numeric_standardized = scaler.transform([input_features_numeric])

        # Replace the numeric features with the standardized values
        for i, index in enumerate(numeric_feature_indices):
            input_features[0][index] = input_features_numeric_standardized[0][i]

        # Use the loaded model for prediction
        model_output = knn_model.predict(input_features)

        # Map model output to "Approved" or "Not Approved"
        loan_status = "Approved" if model_output[0] == '1' else "Not Approved"

        return render_template('result.html', loan_status=loan_status)

if __name__ == '__main__':
    app.run(debug=True)



