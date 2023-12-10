from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = joblib.load('best_model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Retrieve input values from the form
        gender = request.form['gender']
        married = request.form['married']
        # Add other input fields
        
        # Create a DataFrame with the input values
        input_data = pd.DataFrame({
            'gender': [gender],
            'married': [married],
            # Add other input fields
        })

        # Preprocess the input data (similar to the training data preprocessing)
        # ...

        # Use the saved model to make predictions
        prediction = model.predict(input_data)

        return render_template('predict.html', prediction=prediction[0])

    return render_template('predict.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
