from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    try:
        age = int(request.form['0']) ## Age
        trestbps = int(request.form['5']) ## Resting Blood Pressure
        chol = int(request.form['6']) ## Cholestrol Level
        fbs = int(request.form['7']) ## Fast Blood Sugar Level
        thalach = int(request.form['8']) ## Max Heart Rate Achieved
        oldpeak = int(request.form['10']) ## oldpeak
        ca = int(request.form['11']) ## number of major vessels
        thal = request.form['12'] ## thalium stress result
        if thal == 'Normal':
            thal = 1
        elif thal == 'Fixed Defect':
            thal = 2
        else:
            thal = 3
        
        exang = request.form['9'] ## exercise induced angina
        if exang=='Yes':
            exang = 0
        else :
            exang = 1
        
        sex = request.form['1'] ## Sex
        if sex=='Male':
            sex=1
        else:
            sex=0
        cp = request.form['2'] ## Chest Pain
        if cp=='Typical angina':
            cp=0
        elif cp=='Atypical angina':
            cp=1
        elif cp=='Non-anginal pain':
            cp=3
        else:
            cp=4

        restecg = request.form['3'] ## resting electrocardiongraphic results
        if restecg=='Nothing to note':
            restecg=0
        elif restecg=='ST-T Wave abnormality':
            restecg=1
        else:
            restecg=2
        slope = request.form['4'] ## Slope
        if slope == 'Upslopping':
            slope = 0
        elif slope =='Flatslopping':
            slope = 1
        else:
            slope = 2
            
        entry = [age,int(sex),int(cp),trestbps,chol,fbs,int(restecg),thalach,int(exang),oldpeak,int(slope),ca,int(thal)]
        
        
        prediction = model.predict([entry])
        if prediction[0]==0:
            return render_template('result.html',pred='Low')
        else:
            return render_template('result.html',pred='High')
    except:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)

