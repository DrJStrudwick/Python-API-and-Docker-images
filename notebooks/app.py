from flask import Flask,request, jsonify
import traceback
import pickle as p
import pandas as pd
import json

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if reg:
        try:
            json_ = request.json
            query = pd.DataFrame(json_)
            prediction = reg.predict(query)
            return jsonify({'prediction': list(prediction)})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


if __name__ == '__main__':
    
    reg = p.load(open('../data/pipline.pickle', 'rb')) #if not in docker image use this line and comment out line below
    #reg = p.load(open('pipline.pickle', 'rb'))
    print('model loaded')
    app.run(host='0.0.0.0',port=5000)
