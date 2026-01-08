import os
from flask import Flask, request, render_template
from predict import predict_image_class  
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,flash,redirect,url_for,session
import sqlite3


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}
val = None
confidence_score = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

app.secret_key="123"
con=sqlite3.connect("database.db")
con.execute("create table if not exists customer(pid integer primary key,name text,address text,contact integer,mail text)")
con.close()

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/about')
def about():
    return render_template('about.html')

#image process
@app.route('/customer',methods=["GET","POST"])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            n="No selected file"
            return render_template('upload.html',data=n)
        if file and allowed_file(file.filename):
            global filename, val, confidence_score
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            val, confidence_score = predict_image_class(filepath)
            return render_template('upload.html', data=val, confidence=confidence_score)           
    return render_template('upload.html')

#main
if __name__ == '__main__':
    app.run(debug=True)