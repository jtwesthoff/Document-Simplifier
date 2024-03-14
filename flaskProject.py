from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import aspose.words as aw
from forms import UploadForm
from facebookCNNTextSimplifier import Simplify
from flask import current_app

app = Flask(__name__)

app.config['SECRET_KEY'] = 'DSHFKJSDHFKJSDHFKJHSDFKJHSDFSKLFHSDLKFHLSDFHLSKHDF'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}  #only allows PDF files

@app.route("/", methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) #santizes file
            upload_folder = os.path.join(current_app.root_path, 'static', 'uploads') #constructs path
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            #Converts the uploaded PDF to text
            input_pdf = os.path.abspath(file_path) #absolute path to the uploaded PDF
            output_text_folder = os.path.join(current_app.root_path, 'static', 'textOutput') #output path
            output_text_path = os.path.join(output_text_folder, os.path.splitext(filename)[0] + '.txt')
            #output_text_path = os.path.splitext(input_pdf)[0] + '.txt'
           
            #Conversion from PDF to TXT
            doc = aw.Document(input_pdf)
            doc.save(output_text_path)
            simplified_text = Simplify(output_text_path)  # Get simplified text
           
            return render_template('output.html', simplified_text=simplified_text)  # Pass simplified_text to output.html

    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
