from flask import Flask, jsonify, render_template, request

from werkzeug.utils import secure_filename

import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload',methods=[ "GET",'POST'])
def upload():
    print("上船中....")
    uploaded_file=request.files['inputFile']
    # uploaded_file = request.files.getlist("inputFile")    
    
    if uploaded_file.filename == '':
        print('No selected file')    
        return ("",204)

    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        print (filename)
        uploaded_file.save(os.path.join("./", filename))
       
        

        return ("",204)

@app.route('/')
def index():
    return render_template('index.html')
	
	

if __name__ == "__main__":
    app.run(debug=True)	