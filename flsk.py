from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Hml.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    Age = int(request.form['Age'])
    Gender = request.form['Gender']
    Class = request.form['Class']
    Seat_Type = request.form['Seat_Type']
    Fare_Paid = int(request.form['Fare_Paid'])

    input_Data = pd.DataFrame([{
        'Age': Age,
        'Gender': Gender,
        'Class': Class,
        'Seat_Type': Seat_Type,
        'Fare_Paid': Fare_Paid
    }])

    # Encoding mappings
    Genco = {'Female': 0, 'Male': 1}
    Cenco = {'Economy': 0, 'First': 1, 'Business': 2}
    Senco = {'Window': 2, 'Middle': 1, 'Aisle': 0}

    # Map categorical values
    input_Data['Gender'] = input_Data['Gender'].map(Genco)
    input_Data['Class'] = input_Data['Class'].map(Cenco)
    input_Data['Seat_Type'] = input_Data['Seat_Type'].map(Senco)

    # Predict using the model
    prediction = model.predict(input_Data)[0]
    if prediction==1:
        p='Thank God, Survived'
    else:
        p='Sory, We lost them'

    return render_template('Hml.html', prediction_text=f'Predicted Output: {p}')

if __name__ == '__main__':
    app.run(debug=True)
