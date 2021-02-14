from bs4 import BeautifulSoup as bs
import requests
import time
from conf import con_lenta


class LentaParser:

    def __init__(self):
        self.top_news = []

    def get_news(self):
        response = requests.get(f"{con_lenta['url']}").text
        soup = bs(response, 'lxml')
        all_paragraphs = []
        for each in soup.select('div[class*="yellow-box__wrap"]'):
            children = each.findChildren(recursive=False)
            main_news = children[1:]
            for news in main_news:
                news_data = {}
                news_title = news.getText()
                news_title = news_title.replace(u'\xa0', u' ')
                news_data['title'] = news_title
                news_href = con_lenta['url'] + news.find('a', href=True).get('href')
                body = requests.get(news_href).text
                time.sleep(1)
                soup_article = bs(body, 'lxml')
                for element in soup_article.select('div[itemprop*="articleBody"]'):
                    paragraph = element.find_all('p')
                    for p in paragraph:
                        all_paragraphs = p.getText()
                news_data['body'] = all_paragraphs
                self.top_news.append(news_data)
        return self.top_news
