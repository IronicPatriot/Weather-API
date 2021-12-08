import requests, json

ipstack_api_key = 'd2b531dedb5ba133cf538ec6fb4556ec'

IP = input("Please enter any valid IP: ")

#IP = '108.160.244.165' #Toronoto Canada IP for demonstration purposes. Replace with any valid IP.

api_request = requests.get('http://api.ipstack.com/{}?access_key={}'.format(IP, ipstack_api_key))

response = api_request.text
print(response)

response = json.loads(response)

lat = response['latitude']
lon = response['longitude']

print(lat)
print(lon)


openweather_api_key = '3847a48e04036c8633f36bdc73d3a89a'

api_request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&exclude=hourly,minutely,alerts&appid={}'.format(lat, lon, openweather_api_key))

results = api_request.text
# print(results)

weather = json.loads(results)


local = weather['current']
test = local['weather']
print(test[0])
dict = test[0]
forecast = dict["main"]
desc = dict["description"]
temp = local["temp"]
location_a = weather["lat"]
location_b = weather["lon"]
print(forecast)
print(desc)
print("The temperature is:", temp)
print("Your location is:", location_a, location_b)
