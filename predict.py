import pickle
from flask import Flask, request, jsonify
import pandas as pd

with open('model.bin', 'rb') as f_in:
    model = pickle.load(f_in)


app = Flask('gender_prediction')

@app.route('/predict', methods=['POST'])
def predict():
    customer=request.get_json()
    customer_df = pd.DataFrame([customer])
    gender_pred=model.predict(customer_df)
    gender=gender_pred[0]
    result=None 
    if gender==0:
        result='Male'
    else:
        result='Female'
    return {
        'gender':result
    }

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)