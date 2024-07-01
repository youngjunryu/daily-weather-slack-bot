from infrastructure.api.api_request import ApiRequest


class WeatherApiRequest(ApiRequest):

    def __init__(self, url, params):
        super().__init__(url)
        self.params = params
