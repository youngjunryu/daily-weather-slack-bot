from abc import ABC, abstractmethod


class ApiDataFactory(ABC):

    @abstractmethod
    def create_request(self):
        pass
