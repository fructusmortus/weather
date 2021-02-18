from abc import ABC, abstractmethod


class ParentNews(ABC):

    def __init__(self):
        self.news_data = []
        self.send_request()

    @abstractmethod
    def send_request(self):
        raise NotImplementedError
