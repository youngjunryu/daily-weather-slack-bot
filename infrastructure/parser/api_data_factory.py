from abc import ABC, abstractmethod

from infrastructure.api.api_request import ApiRequest
from infrastructure.api.api_response import ApiResponse
from infrastructure.mapper.api_data_mapper import ApiDataMapper


class ApiDataFactory(ABC):

    def __init__(self, api_data_mapper: ApiDataMapper = None):
        self.api_data_mapper = api_data_mapper

    @abstractmethod
    def generate_request_data(self) -> ApiRequest:
        pass

    @abstractmethod
    def parse_response_data(self, raw_response) -> ApiResponse:
        pass
