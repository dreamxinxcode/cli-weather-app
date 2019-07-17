import configparser
import requests
import pprint

global api_key, city, city_name, country, latitude, longitude, weather_type, temp, temp_min, temp_max, wind_speed, humidity

config = configparser.ConfigParser()
config.read("config.ini")
api_key = config.get("api", "key")

def main():
    city = input("\033[1mEnter a city:\033[0m ")
    print(f"[\033[95m*\033[0m] Fetching weather data for \"{city}\"...")
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    r = requests.get(url)
    weather_data = r.json()
    city_name = weather_data["name"]
    country = weather_data["sys"]["country"] 
    temp = weather_data["main"]["temp"]
    temp_min = weather_data["main"]["temp_min"]
    temp_max = weather_data["main"]["temp_max"]
    weather_type = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]
    latitude = weather_data["coord"]["lat"]
    longitude = weather_data["coord"]["lon"]
    humidity = weather_data["main"]["humidity"]
    TEMPLATE = """ 
    \033[1mCity:\033[0m        {}
    \033[1mCountry:\033[0m     {}
    \033[1mLatitude:\033[0m    {}
    \033[1mLongitude:\033[0m   {}
    \033[1mWeather:\033[0m     {}
    \033[1mTemperature:\033[0m {}C
    \033[1mTemp Min:\033[0m    {}C
    \033[1mTemp Max:\033[0m    {}C
    \033[1mWind Speed:\033[0m  {}
    \033[1mHumidity:\033[0m    {}
    """
    print(TEMPLATE.format(city_name, country, latitude, longitude, weather_type.capitalize(), temp, temp_min, temp_max, wind_speed, humidity))
    print("[\033[95m*\033[0m] Done")

if __name__ == "__main__":
    main()
