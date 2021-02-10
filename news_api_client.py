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
            return self.news_data

    def get_title(self):
        top_three_news = self.news_data['articles'][0:3]
        news = []
        i = 0
        for k in top_three_news:
            i += 1
            news.append('title' + str(i))
            news.append(k['title'])
            news.append('body' + str(i))
            news.append(k['content'])
        print(news)
        return [news[i::3] for i in range(3)]
