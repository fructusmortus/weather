from bs4 import BeautifulSoup as bs
import requests
import time
from conf import con_lenta
from ParentNews import ParentNews
from api_not_available import ApiNotAvailableException


class LentaParser(ParentNews):

    def __send_request(self):
        response = requests.get(f"{con_lenta['url']}")
        if response.status_code != 200:
            raise ApiNotAvailableException("Error occurred in LentaParser")
        else:
            self.news_data = response.text

    def get_top_news(self):
        soup = bs(self.news_data, 'lxml')
        output_news = []
        for each in soup.select('div[class*="yellow-box__wrap"]'):
            children = each.findChildren(recursive=False)
            main_news = children[1:]
            for news in main_news:
                news_output = {}
                news_title = news.getText()
                news_title = news_title.replace(u'\xa0', u' ')
                news_output['title'] = news_title
                news_href = con_lenta['url'] + news.find('a', href=True).get('href')
                body = requests.get(news_href).text
                time.sleep(1)
                soup_article = bs(body, 'lxml')
                for element in soup_article.select('div[itemprop*="articleBody"]'):
                    paragraph = element.find_all('p')
                    all_paragraphs = (''.join(p.getText() for p in paragraph))
                    news_output['body'] = all_paragraphs
                output_news.append(news_output)
        return output_news
