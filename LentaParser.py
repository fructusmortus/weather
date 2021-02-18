from bs4 import BeautifulSoup as bs
import requests
import time
from conf import con_lenta
from ParentNews import ParentNews


class LentaParser(ParentNews):

    def send_request(self):
        response = requests.get(f"{con_lenta['url']}").text
        soup = bs(response, 'lxml')
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
                self.news_data.append(news_output)
        return self.news_data
