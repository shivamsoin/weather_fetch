import requests
api_key='YOUR_API'
city=input('Enter City: ')
weather=requests.get(url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}')
data=weather.json()
weather=data['weather'][0]['description']
temp=data['main']['temp']-273.15
formatted_temp="{:.2f}".format(temp)
hum=data['main']['humidity']
print(f"{city} weather\n{weather}\nTemperature: {formatted_temp}\nHumidity: {hum}")

