import requests
import json

try:
    city=input("Enter a city:")

    url=f"https://api.weatherapi.com/v1/current.json?key=73a24c2509fa47ed9b984612231004&q={city}"
    r=requests.get(url)

    a=json.loads(r.text)

    print(f'{city} is located in state of {a["location"]["region"]} in {a["location"]["country"]}.\nThe current time is {a["location"]["localtime"]}.\nThe wind in {city} is flowing at a speed of {a["current"]["wind_kph"]} kilometres per hour.\n'
      f'The weather here is {a["current"]["condition"]["text"]} and the air pressure is {a["current"]["pressure_mb"]} Pascal.\nThe temperature is {a["current"]["temp_c"]} Celsuis.')

except KeyError:
    print("City Name Invalid!")