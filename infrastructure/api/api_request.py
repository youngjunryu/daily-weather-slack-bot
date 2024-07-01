from abc import ABC, abstractmethod


class ApiRequest(ABC):

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def generate_params(self):
        pass
