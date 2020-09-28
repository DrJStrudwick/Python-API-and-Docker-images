from flask import Flask,request, jsonify         #imports the core functionalities for running the APIs
import traceback                                 #will handle the formatting of any erros coming from functions (OPTIONAL)
import pickle as p                               #needed for the loading of any files i.e our pipline we wish to operate
import pandas as pd                              #needed for giving the data to our pipline
import json                                      #needed for handeling the json data in the request/curl

app = Flask(__name__)                            #This initialises the app. Do not change the __name__

@app.route('/predict', methods=['POST'])         #This sets up the route to activate the following function and the method that it will recieve 
def predict():
    if reg:                                                     #If the pipline exists
        try:                                                    #try to
            json_ = request.json                                #extract the json data from the request
            query = pd.DataFrame(json_)                         #load it into a pandas data frame
            prediction = reg.predict(query)                     #give the data to our pipline to predict on
            return jsonify({'prediction': list(prediction)})    #return the resulting prediction in a json formatt
        except:                                                 #if it failed to predict
            return jsonify({'trace': traceback.format_exc()})   #return the traceback error in json format
    else:                                                       #if the pipline does not exist
        print ('Train the model first')
        return ('No model here to use')                         #return the information


if __name__ == '__main__':                           #when the app first launches it will run the "__main__" body first to set anything up.
    reg = p.load(open('data/pipline.pickle', 'rb'))  #load in our pipline otherwise nothing will happen
    print('model loaded')
    app.run(host='0.0.0.0',port=5000)                #tell the app to run setting the host and the port number
