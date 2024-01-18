import requests
from colorama import Fore

ask = input("Enter the city Name you want to know weather? ")
response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={ask},IND&limit=2&appid=7cfa155d846b68092d142ae9a8f74534")

a = response.json()

while True:
    try:
        lat = a[0]['lat']
        lon = a[0]['lon']
        break
    except:
        print(f"{ask} City Not Found Please type the name correctly :)")
        ask = input("Enter the city Name you want to know weather? ")
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={ask},IND&limit=2&appid=7cfa155d846b68092d142ae9a8f74534")
        a = response.json()


weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid=7cfa155d846b68092d142ae9a8f74534")
weather_detail = weather.json()

print(f"\n{Fore.WHITE}Name : {Fore.GREEN}{ask}\t\t{Fore.WHITE}Weather : {Fore.GREEN}{weather_detail['weather'][0]['main']} , {Fore.GREEN}{weather_detail['weather'][0]['description']}\n{Fore.WHITE}Division  : {Fore.GREEN}{weather_detail['name']}\t\t{Fore.WHITE}Temp (°C) : {Fore.GREEN}{weather_detail['main']['temp']}\n{Fore.WHITE}Feels as if (°C): {Fore.GREEN}{weather_detail['main']['feels_like']}\t\t{Fore.WHITE}Humidity : {Fore.GREEN}{weather_detail['main']['humidity']}")
