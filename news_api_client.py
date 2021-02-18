import requests
from conf import con_api_news
from api_not_available import ApiNotAvailableException
from ParentNews import ParentNews
from pprint import pprint


class NewsApiClient(ParentNews):

    def __init__(self, country):
        self.country = country
        super().__init__()

    def send_request(self):
        response = requests.get(f"{con_api_news['url']}?country={self.country}&apiKey={con_api_news['api_key']}")
        if response.status_code != 200:
            error_message = response.json()['error']
            raise ApiNotAvailableException(f"{error_message} occurred in NewsApiClient")
        else:
            news_data = response.json()
            news_data = news_data['articles'][0:]
            pprint(news_data)
            for news in news_data:
                formatted_news = {
                    "title": news['title'],
                    "body": news['content']
                }
                self.news_data.append(formatted_news)
                pprint(self.news_data)
            return self.news_data
