import requests
import json
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

url = 'http://127.0.0.1:5000/prediction/'


data =[[    26,     12,      4,      4,    235,     11,     14,     37,
        261306,     97,      0,      3,      1,      0,      0,      1,
            88,    172,     29]]

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r)
output = r.json()['Prediction'].value()
print(output)