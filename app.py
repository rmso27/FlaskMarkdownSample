from flask import Flask, render_template
from flaskext.markdown import Markdown

# Initialize the Flask application
app = Flask(__name__)
# Initialize Flask-Markdown extension
Markdown(app)

@app.route('/')
def index():
    # Read the Markdown file content
    with open("temp.md") as md_file:
        data=md_file.read()
        # Render the template with the Markdown content
        return render_template('index.html', md_content=data)

if __name__=='__main__':
    app.run(debug=True)