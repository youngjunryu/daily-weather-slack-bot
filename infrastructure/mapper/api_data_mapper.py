from abc import ABC, abstractmethod

from infrastructure.api.api_response import ApiResponse


class ApiDataMapper(ABC):

    def __init__(self, response: ApiResponse):
        self.response = response

    @abstractmethod
    def mapper(self) -> dict:
        pass
