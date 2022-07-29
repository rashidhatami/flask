import json
import numpy as np
import requests
from crypt import methods
import requests, json
from flask import Flask,request, url_for, redirect, render_template
import pandas as pd
from flask_cors import CORS


app = Flask(__name__) 
CORS(app)


@app.route('/')
def template_deploy():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    l = []
    for item in request.form.values():
        l.append(int(item))
    
    dataToPredict = [[120.87, 37.77, 9.0, 4838.0, 920.0, 2460.0, 923.0, 3.5959]]
    input_data = json.dumps({
    'signature_def': 'serving_default',
    'instances': dataToPredict
    })
                   
    url = 'http://localhost:8501/v1/models/my_model:predict'
    # url = 'http://localhost:8501/v1/models/my_model/versions/0004:predict'
    re = requests.post(url, data=input_data)
    pred = re.json()
    pred_list = pred['predictions'][0]

    max_value = 0
    index_list = None
    for item in range(0, len(pred_list)):
        if pred_list[item] > max_value:
            max_value = pred_list[item]
            index_list = item

    # print(max_value, index_list)  
    return render_template('index.html', prediction_text=pred_list)  