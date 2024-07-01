from abc import ABC


class ApiRequest(ABC):

    def __init__(self, url):
        self.url = url
