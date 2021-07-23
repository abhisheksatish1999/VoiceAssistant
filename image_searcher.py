from bs4 import BeautifulSoup
import requests
import urllib
from fake_useragent import UserAgent
import re



class image_search:
    def __init__(self,inp):
        self.search_string=inp.lower()
        self.image_urls=[]


    def search_now(self):
        query = self.search_string
        query = urllib.parse.quote_plus(query)  # Format into URL encoding
        number_result = 20

        ua = UserAgent()

        google_url = "https://www.google.com/search?q=images+of" + query + "&num=" + str(number_result)
        print(google_url)
        response = requests.get(google_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.content, "html.parser")
        #print(soup.prettify())
        img_elems = soup.find_all('a', class_='BVG0Nb',href=True)
        #print(img_elems)

        for i in range(4):
            img=img_elems[i]
            src_link=img["href"]
            #print(src_link)
            src_link=re.findall("=(.*)\&imgrefurl",src_link)
            #print(src_link)

            self.image_urls.append(src_link[0])

        return '#'.join(self.image_urls)



