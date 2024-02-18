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
            fileData = file.read()
            age = request.form.get('age')
            name = request.form.get('name')
            gender = request.form.get('gender')

            count = checkTelomereLength(inputString=fileData) # this return the count

            data =  {
                    "riskOfCancer":"No",
                    "telomereLength":count,
                    "gender":gender,
                    "name":name,
                    "age": age
                }
            
            if count > 0 and int(age) > 20  and gender == 'male':
                data['riskOfCancer'] = "Yes"
            else:
                 data['riskOfCancer'] = "No"
            
            return render_template('output.html',data=data)
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
