import requests

api_key = "a6c117fe62dcc6ec6fd13a789033f3cb"
main_url = f"https://api.openweathermap.org/data/2.5/weather?"
city = "Tashkent"

url = main_url + 'appid=' + api_key + "&q=" + city + '&units=metric' 
response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temperature =  data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['description']
    print(f"""Weather in Tashkent:
Temperature: {temperature}°C
Humidity: {humidity}%
Condition: {condition}""")
else:
    print("Failed to get data.")    


