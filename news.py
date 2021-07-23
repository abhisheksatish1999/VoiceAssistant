import requests

class News:
    def __init__(self):
        self.api_key = "1ce668fb8a3246e5b7324314d923bfdd"
        self.news_list = []
        self.newspaper_company = ["NDTV News", "91mobiles", "Hindustan Times", "The Times of India", "India Today",
                             "Bollywood Hungama", "Citytoday.news", "The Indian Express"]

    def gettop5(self):
        url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+self.api_key
        news_request = requests.get(url)
        news_data = news_request.json()
        news=news_data['articles']
        for each in news:
            if(each['source']['name'] in self.newspaper_company):
                news_message=each['title']+"||"+each['url']
                self.news_list.append(news_message)
            if(len(self.news_list) == 5):
                break
        return "#".join(self.news_list)



