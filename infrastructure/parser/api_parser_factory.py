from abc import ABC, abstractmethod


class ApiParserFactory(ABC):

    @abstractmethod
    def generate_api_request(self):
        pass

    @abstractmethod
    def generate_api_response(self):
        pass
