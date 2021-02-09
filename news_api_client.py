import requests
import conf


class NewsApiClient:

    def __init__(self, country):
        self.config = conf.con_top_news
        self.country = country
        self.news_data = {}

    def get_data(self):
        response = requests.get(f"{self.config['url']}?country={self.country}&apiKey={self.config['api_key']}")
        if 'status' not in response.json():
            return False
        else:
            self.news_data = response.json()
            print(self.news_data)
            return True

    def get_top_news(self):
        top_news = {
            "top_news": self.news_data['articles'][0:5]
        }
        return top_news
