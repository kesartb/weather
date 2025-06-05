import requests
from datetime import datetime

def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def generate_html(weather_data):
    if weather_data:
        city = weather_data['name']
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Weather Forecast</title>
            <meta http-equiv="refresh" content="1800">
        </head>
        <body>
            <h1>Weather Forecast for {city}</h1>
            <p>As of: {date_time}</p>
            <p>Temperature: {temp}°C</p>
            <p>Condition: {description}</p>
            <p>Wind Speed: {wind_speed} m/s</p>
        </body>
        </html>
        """
        return html_content
    else:
        return "<html><body><h1>Error fetching weather data</h1></body></html>"

def save_html(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

def update_weather_forecast():
    api_key = '80066c3f9fc1cc035a019af7c86a0e56'  # Replace with your OpenWeatherMap API key
    city = 'Albacete,ES'
    weather_data = fetch_weather(api_key, city)
    html_content = generate_html(weather_data)
    save_html(html_content, 'weather_forecast.html')

update_weather_forecast()
