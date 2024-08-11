import requests
import json
import schedule
import time

#Get the API key from the openweathermap profile
api_key = "9c13560a20a83cefc3195458d1fb6c62"

#Open weather API call
open_weather_map_url = "https://api.openweathermap.org/data/2.5/weather?"

#Latitue of Dhaka city
lat = "23.7873"

#Longitude of Dhaka city
lon = "90.3514"

weather_url = f"{open_weather_map_url}lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(weather_url)

weather_data = response.json()


#{"coord":{"lon":90.3514,"lat":23.7873},"weather":[{"id":721,
#"main":"Haze","description":"haze","icon":"50d"}],"base":"stations",
#"main":{"temp":308.16,"feels_like":315.16,"temp_min":308.16,"temp_max":308.16,
#"pressure":1004,"humidity":63},"visibility":5000,"wind":{"speed":4.12,"deg":200},
#"clouds":{"all":75},"dt":1717317302,"sys":{"type":1,"id":9145,"country":"BD",
#"sunrise":1717283478,"sunset":1717332134},"timezone":21600,"id":1337178,"name":"Dhaka District","cod":200}


def get_weather_result():

    if weather_data["cod"] == 200:
        kelvin = 273.15
        temperature = int(weather_data["main"]["temp"] - kelvin)
        feels_like = int(weather_data["main"]["feels_like"] - kelvin)
        humidity = weather_data["main"]["humidity"]

        weather_report = (f"=====WEATHER REPORT OF DHAKA CITY=====\n"
              f"Weather temperature: {temperature}°C\n"
              f"Temperature feels like: {feels_like}°C\n"
              f"Humidity: {humidity}%\n")

        return weather_report
    
    else:
        return (f"Failed to get the weather data. HTTP status code {response.status_code}")
        
def send_weather_report_to_telegram():
    #Sending message to the telegram bot
    telegram_url = "https://api.telegram.org/bot7283569342:AAHOGFyAm5xYMzq0GE0KyKdmQ9mV5qty8f0/sendMessage"

    parameter = {
        "chat_id" : -4215943504, 
        "text" : get_weather_result()
        }

    
    resp = requests.get(telegram_url, data = parameter)

    print(resp.text)

#Scheduling the program to sent the message
schedule.every(9).hours.do(send_weather_report_to_telegram)

#send an initial message for sharing the weather report every 9 hours
print("Your program is scheduled to send the weather update every 9 hours")
send_weather_report_to_telegram()

#running while loop to share the report every 9 hours
while True:
    schedule.run_pending()
    time.sleep(10)
