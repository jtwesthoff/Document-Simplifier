# Legal Document Simplifier

This project is a web-based application built with Flask that simplifies legal documents. Users can upload legal documents in PDF format, which are then converted to text, simplified using the Facebook BART model, and displayed in a simplified form on a web page.

## Project Components

### 1. `flaskProject.py`

This Python file contains the Flask application responsible for handling the web interface and backend functionality. It allows users to upload PDF files, converts them to text, simplifies the text using the Facebook BART model, and renders the simplified text on a web page.

Key functionalities:
- Uploads PDF files
- Converts PDFs to text
- Simplifies text using the Facebook BART model
- Renders simplified text on a web page

### 2. `facebookCNNTextSimplifier.py`

This Python file provides a function `Simplify()` that utilizes the Facebook BART model for text simplification. It takes a filename as input, reads the text from the file, simplifies it using the BART model, and returns the simplified text.

### 3. `forms.py`

This Python file defines a FlaskForm class `UploadForm` using Flask-WTF. This form is used in the Flask application (`flaskProject.py`) to handle file uploads. It includes a FileField for uploading PDF files and a SubmitField for submitting the form.

### 4. `ConvertPDF.ipynb`

This Jupyter Notebook demonstrates how to convert a PDF file to text using the aspose.words library. It also provides a code snippet for converting the text into an array of lines and words.

Key functionalities:
- Converts PDF to text using Aspose.Words
- Demonstrates parsing text into arrays of lines and words

## Getting Started

To run the project locally, follow these steps:

1. Install Python 3.9.
2. Install the required dependencies listed in requirements.
3. Run `flaskProject.py` to start the Flask server.
4. Access the application in your web browser at `http://localhost:5000`.

## Requirements

- Python 3.9
- Flask
- Flask_wtf
- Aspose.words for Python
- Transformers library

## Contributors
- Alvin Thomson
- Sean O'Hara
