from flask import Flask, render_template
import requests

app = Flask(__name__)


def city_id(id_str):
    param = {'id': id_str, 'units': 'metric', 'APPID': '64ae36ec03b368c4e5b0754df2b7e733'}
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    req = requests.get(url, params=param)
    return req


# TODO add form when user can input their city

req_lv = city_id('702550')
req_new = city_id('5128581')
req_ry = city_id('108410')
req_to = city_id('1850147')


def weather_data(req):
    json_data = req.json()
    city = json_data['name']
    temp = int(json_data['main']['temp'])
    weather = json_data['weather'][0]['description']
    data_dict = {'city': city, 'temp': temp, 'weather': weather}
    return data_dict


info_lv = weather_data(req_lv)
info_new = weather_data(req_new)
info_ry = weather_data(req_ry)
info_to = weather_data(req_to)


@app.route('/')
def index():
    return render_template('index.html', info_lv=info_lv, info_new=info_new, info_ry=info_ry, info_to=info_to)


if __name__ == '__main__':
    app.run(debug=True)
