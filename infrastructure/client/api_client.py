import requests

from infrastructure.api.slack_api_request import SlackApiRequest
from infrastructure.api.weather_api_request import WeatherApiRequest


class ApiClient:

    def send_slack_message(self, api_request: SlackApiRequest):
        requests.post(api_request.get_url(), json=api_request.get_body())

    def request_daily_weather(self, api_request: WeatherApiRequest):
        return requests.get(api_request.get_url(), params=api_request.get_params())
