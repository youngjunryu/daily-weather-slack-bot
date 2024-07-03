from abc import ABC, abstractmethod


class ApiRequest(ABC):

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_headers(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def parse_response(self, response):
        pass
