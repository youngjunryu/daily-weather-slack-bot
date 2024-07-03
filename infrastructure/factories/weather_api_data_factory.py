from infrastructure.api.weather_api_request import WeatherApiRequest
from infrastructure.factories.api_data_factory import ApiDataFactory


class WeatherApiDataFactory(ApiDataFactory):

    def create_request(self) -> WeatherApiRequest:
        return WeatherApiRequest()
