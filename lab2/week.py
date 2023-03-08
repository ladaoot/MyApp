import requests

city = "Moscow,RU"
appid = "c3c5a807c9980bdaa523c46a2a71a273"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'appid': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])

print("Видимость:", data['visibility'], "метров")
print("Скорость ветра:", data['wind']['speed'], "м/сек")
