from flask import Flask, render_template, request
from werkzeug.urls import url_quote, url_quote_plus  
import requests
import werkzeug

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = 'your_openweathermap_api_key'  # Replace with your actual OpenWeatherMap API key

    # Choose the appropriate function based on your Werkzeug version
    if werkzeug.__version__ >= '1.0':
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={url_quote_plus(city)}&appid={api_key}'
    else:
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={url_quote(city)}&appid={api_key}'

    response = requests.get(weather_url)
    weather_data = response.json()
    
    if weather_data['cod'] == 200:
        weather_info = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
        return render_template('result.html', weather=weather_info)
    else:
        return render_template('index.html', error="City not found")

if __name__ == '__main__':
    app.run(debug=True)
