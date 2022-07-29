import pickle

newModel = pickle.load(open('abs.pickle', 'rb'))
result= newModel.predict([[26,     12,      4,      4,    235,     11,     14,     37,
        261306,     97,      0,      3,      1,      0,      0,      1,
            88,    172,     29]])

print(result)