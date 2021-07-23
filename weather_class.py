import requests,json
import webbrowser

class weather:
    def __init__(self):
        # store url string on instance
        self.api_key = "caf5d7ac40106530ae91207572ef2609"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.complete_url = ''
        self.response =0
        self.city=''

    def Temperature(self):
        # make a request to get the url and save the response on the instance
        x=self.response.json()
        y=x['main']
        current_temperature=y['temp']
        return(str(int(current_temperature-273)))

    def get_city(self):
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        ipAdd = ip_request.json()['ip']
        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
        geo_request = requests.get(url)
        geo_data = geo_request.json()
        self.city = geo_data['city']
        self.complete_url = self.base_url + "q=" + self.city + "&appid=" + self.api_key
        self.response = requests.get(self.complete_url)


    def Weather_desc(self):
        x=self.response.json()
        z=x['weather']
        weather_description=z[0]['description']
        return(weather_description)
    def city_print(self):
        place=self.city
        return(place)
    def weathermain(self):
        x=self.response.json()
        y=x['weather']
        current_weather=y[0]['main']
        return(current_weather)


if __name__ == "__main__":
    api_key="caf5d7ac40106530ae91207572ef2609"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    #city_name=input('Enter city name :')
    r=requests.get('https://get.geojs.io/')

    ip_request= requests.get('https://get.geojs.io/v1/ip.json')
    ipAdd = ip_request.json()['ip']
    #print(ipAdd)

    url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    city=geo_data['city']
    complete_url=base_url+"q="+city+"&appid="+api_key
    response=requests.get(complete_url)
    obj1=weather(complete_url,city,response)
    current_temperature=obj1.Temperature()
    weather_description=obj1.Weather_desc()
    Location = obj1.city_print()
    Weather = obj1.weathermain()
    print("Location = "+str(Location)+"\nTemperature (in degree Celsius)="+str(int(current_temperature-273))+"\nDescription = " +str(weather_description)+"\nWeather = "+str(Weather))
