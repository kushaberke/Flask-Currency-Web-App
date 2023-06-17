from flask import Flask, render_template
from destek import googlefinance

app = Flask(__name__)

@app.route('/')
def home():
    dolar = googlefinance("USD")
    return render_template('index.html', dolar=dolar)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
