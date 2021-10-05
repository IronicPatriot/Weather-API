import geocoder, requests, json
# geocoder is not standard library

geo = geocoder.ip('me')
# print(geo.latlng)
print(geo.lat)
print(geo.lng)

lat = geo.lat
lon = geo.lng
# lat = "34.0522"
# lon =  "118.2437"

api_key = '3847a48e04036c8633f36bdc73d3a89a'

api_request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&exclude=hourly,minutely,alerts&appid={}'.format(lat, lon, api_key))

results = api_request.text
# print(results)
# prints raw json

weather = json.loads(results)
# print(json.dumps(weather, indent = 4, sort_keys=True))
# print(weather)
# puts json data into python dictionary

# for x in weather['current']:
    # print(x)

local = weather['current']
# print(local.get('weather'))
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

# icons - https://openweathermap.org/weather-conditions






