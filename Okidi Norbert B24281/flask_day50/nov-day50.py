from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def home():  
    return render_template('instagram.html')


if __name__ == 'main':
    app.run(debug=True)