from flask import Flask, request, render_template
# Import the pipeline class from the transformers library
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

app = Flask(__name__)

# Define the main route
@app.route('/', methods=['GET', 'POST'])
def main(): 
    return 'Hello, World!'