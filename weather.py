import requests
import json
from pprint import pprint
import datetime
API = 'fu4y7wy8imdfdjsn039eq90'  # your api


def weather(city, API):

    try:
        req = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        date = req.json()
        # pprint(date)
        city = date['name']
        current_temp = date['main']['temp']
        speed_of_wind = date['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(date['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(date['sys']['sunset'])
        print(f'Погода в городе {city} 🏙.\nТемпература: 🌡 {current_temp}°С .\nСкорость ветра: {speed_of_wind} м/c.\nВремя восхода солнца: 🌅 {sunrise_time}.\nВремя заката: 🌇 {sunset_time}.\nХорошего дня! 😸')

    except Exception as ex:
        print(ex)
        print('Проверьте город')


def main():
    city = input('введите город: ')
    weather(city, API)


if __name__ == '__main__':
    main()
