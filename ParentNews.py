from abc import ABC, abstractmethod


class ParentNews(ABC):

    def __init__(self):
        self.news_data = []
        self.__send_request()

    @abstractmethod
    def __send_request(self):
        raise NotImplementedError
