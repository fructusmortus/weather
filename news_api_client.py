import requests
import conf


class NewsApiClient:

    def __init__(self, country):
        self.config = conf.con_top_news
        self.country = country
        self.news_data = {}

    def get_data(self):
        response = requests.get(f"{self.config['url']}?country={self.country}&apiKey={self.config['api_key']}")
        if response.status_code != 200:
            print(response.status_code)
            return False
        else:
            self.news_data = response.json()
            print(self.news_data)
            return self.news_data

    def get_top_news(self):
        top_three_news = self.news_data['articles'][0:3]
        our_three = []
        for news in top_three_news:
            formatted_news = {
                "title": news['title'],
                "body": news['content']
            }
            our_three.append(formatted_news)
        return our_three
