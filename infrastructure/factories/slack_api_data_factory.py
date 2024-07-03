from infrastructure.api.slack_api_request import SlackApiRequest
from infrastructure.factories.api_data_factory import ApiDataFactory
from infrastructure.mappers.weather_to_slack_data_mapper import WeatherToSlackDataMapper


class SlackApiDataFactory(ApiDataFactory):

    def create_request(self, api_response) -> SlackApiRequest:
        data = WeatherToSlackDataMapper.mapper(api_response)
        return SlackApiRequest(data)
