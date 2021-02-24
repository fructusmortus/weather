import requests
from conf import con_api_news
from api_not_available import ApiNotAvailableException
from ParentNews import ParentNews


class NewsApiClient(ParentNews):

    def __init__(self, country):
        self.country = country
        super().__init__()

    def _send_request(self):
        response = requests.get(f"{con_api_news['url']}?country={self.country}&apiKey={con_api_news['api_key']}")
        if response.status_code != 200:
            error_message = response.json()['message']
            raise ApiNotAvailableException(f"{error_message} occurred in NewsApiClient")
        else:
            self.news_data = response.json()

    def get_top_news(self):
        output_news = []
        for news in self.news_data['articles'][0:3]:
            if news['title'] and news['content']:
                formatted_news = {
                    "title": news['title'],
                    "body": news['content']
                }
                output_news.append(formatted_news)
        return output_news
