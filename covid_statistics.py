import requests


class COVID:
    def __init__(self):
        self.total_statistics = "https://api.covid19india.org/data.json"
        self.state_statistics = "https://api.covidindiatracker.com/state_data.json"
        covid_request = requests.get(self.total_statistics)
        self.covid_data = covid_request.json()

    def gettotal(self):
        #print(json.dumps(self.covid_data, indent=1))
        todays_data=self.covid_data['statewise'][0]
        stats=[todays_data['recovered'],todays_data['confirmed'],todays_data['deaths']]
        return "#".join(stats)
    def getstate(self):
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        ipAdd = ip_request.json()['ip']
        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
        #print(url)
        geo_request = requests.get(url)
        geo_data = geo_request.json()
        self.city = geo_data['region']
        #print(self.city)
        todays_data=self.covid_data['statewise']
        for each in todays_data:
            if(each["state"] == (self.city)):
                stats=[each['recovered'],each['confirmed'],each['deaths']]
        return "#".join(stats)




if __name__=="__main__":
    cov=COVID()
    print(cov.gettotal())
    print(cov.getstate())


