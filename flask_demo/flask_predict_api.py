#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
import traceback

with open('/var/www/flask_predict_api/houseprices_reg_model_deployment.pkl', 'rb') as model_file:
    final_file = pickle.load(model_file)
    model = final_file['model']

app = Flask(__name__)

# Assuming the 'model' variable is defined elsewhere in your code

@app.route('/predict')
def predict_houseprices():
    try:
        my_id = float(request.args.get("Id"))
        my_qual = float(request.args.get("OverallQual"))
        my_total = float(request.args.get("TotalBsmtSF"))
        my_area = float(request.args.get("GrLivArea"))
        
        prediction = model.predict(np.array([[my_id, my_qual, my_total, my_area]]))
        return str(prediction)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return "Error during prediction"

@app.route('/predict_file', methods=["POST"])
def predict_houseprices_file():
    try:
        input_data = pd.read_csv(request.files.get("input_file"), header=None)
        prediction = model.predict(input_data)
        return str(list(prediction))
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return "Error during prediction from file"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)