from flask import Flask, render_template
import requests

app = Flask(__name__)
app.secret_key = "\xbeE\xd6X\xc7\x9c\x85\x03\xad\x07\xed\xfa\xc6\xa1\xe1f\xf8\x0bn^\xce\x94\xff:"


def weather_data(val):
    param = {'q': val, 'units': 'metric',
             'APPID': '64ae36ec03b368c4e5b0754df2b7e733'}
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    json_data = requests.get(url, params=param).json()
    city = json_data['name']
    temp = int(json_data['main']['temp'])
    weather = json_data['weather'][0]['description']
    data_dict = {'city': city, 'temp': temp, 'weather': weather}
    return data_dict


city_list = ['Lviv', 'New York', 'Riyadh', 'Tokyo']

info = list(map(weather_data, city_list))


@app.route('/')
def index():
    return render_template('index.html', info=info)


if __name__ == '__main__':
    app.run()
