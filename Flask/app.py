from flask import Flask, render_template, request, url_for


app = Flask(__name__)

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
        applicant_income = request.form['applicant_income']
        coapplicant_income = request.form['coapplicant_income']
        loan_amount = request.form['loan_amount']
        loan_amount_term = request.form['loan_amount_term']
        credit_history = request.form['credit_history']
        property_area = request.form['property_area']

        # Replace this with your actual machine learning prediction logic
        # For now, use a simple random prediction
        import random
        loan_status = random.choice(["Approved", "Rejected"])

        return render_template('result.html', loan_status=loan_status)

if __name__ == '__main__':
    app.run(debug=True)



