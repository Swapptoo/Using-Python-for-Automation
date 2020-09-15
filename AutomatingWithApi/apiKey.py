import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '8ab5878a4f5e49028a2136d8145bdc42', 'q': 'Kuala Lumpur, MY'}

response = requests.get(baseUrl, params=parameters)
print(response.content)