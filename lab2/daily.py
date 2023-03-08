import requests

city = "Moscow,RU"
appid = "c3c5a807c9980bdaa523c46a2a71a273"


res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'appid': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("Видимость:", i['visibility'], "метров")
    print("Скорость ветра:", i['wind']['speed'], "м/сек")
    print("____________________________")
