import os
from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def checkTelomereLength(inputString):
    inputString = str(inputString)
    count=inputString.count("xyz") #TODO Please replace with your string patten 
    return count

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            fileData = file.read()
            age = request.form.get('name')
            name = request.form.get('name')
            gender = request.form.get('name')

            count = checkTelomereLength(inputString=fileData)
            data =  {
                    "riskOfCancer":"No",
                    "telomereLength":count,
                    "gender":gender,
                    "name":name,
                    "age": age
                }
            
            if count > 0:
                data['riskOfCancer'] = "Yes"
            else:
                 data['riskOfCancer'] = "No"
           
            return render_template('output.html',data=data)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
