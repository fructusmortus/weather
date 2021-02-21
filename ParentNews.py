from abc import ABC, abstractmethod


class ParentNews(ABC):

    def __init__(self):
        self.news_data = []
        self._send_request()

    @abstractmethod
    def _send_request(self):
        raise NotImplementedError
