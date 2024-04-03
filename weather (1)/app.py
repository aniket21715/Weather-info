import requests
from flask import Flask, request, render_template

app = Flask(__name__)

def get_weather(city):
    api_key = 'fdf605168792eb4ed6217669bb812b08'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'country': data['sys']['country']
            }
            return weather_info
    except Exception as e:
        print("Error:", e)
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_info = get_weather(city)
        if weather_info:
            return render_template('weather.html', weather_info=weather_info)
        else:
            return render_template('error.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)