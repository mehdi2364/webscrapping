from flask import Flask, render_template, request
from api import get_quality_air  # Assuming api.py is in the same directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_aqi():
    city = request.form['city']
    aqi = get_quality_air(city)
    return render_template('index.html', city=city, aqi=aqi)

if __name__ == '__main__':
    app.run(debug=True)
