from flask import Flask, request, render_template
# Import the pipeline class from the transformers library
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

app = Flask(__name__)

# Define the main route
@app.route('/', methods=['GET', 'POST'])
def main(): 
    if request.method == 'GET':
        # Render the index.html template
        return render_template('index.html')
    else:
        # Get the text from the form input 
        text = request.form['text']
        # Check if the text is at least 50 characters
        if len(text) < 50:
            return "Please enter a text with at least 50 characters"
        # Generate the summary
        summary = summarizer(text, max_length=250, min_length=50, do_sample=False)
        # Return the summary
        #return summary[0]['summary_text']

        # Render the index.html template with the text and the summary
        return render_template('index.html',text = text, summary = summary[0]['summary_text'] )