import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'

def weather(city):

    full_url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(full_url)
    r_data = response.json()
    def result():

        if r_data["cod"] != "404":
            y = r_data['main']
            current_t = y['temp']
            current_p = y["pressure"]
            z = r_data["weather"]
            weather_description = z[0]["description"]
            print(str((round(current_t - 273.15))), str(current_p))
        else:
            print(f'{city} not found')
        return "thanks for using our app"
    return result()

if __name__ == '__main__':
    print(weather("Dnipro"))