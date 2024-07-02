import requests

from infrastructure.api.slack_api_request import SlackApiRequest
from infrastructure.api.weather_api_request import WeatherApiRequest


class ApiClient:

    def send_slack_message(self, api_request: SlackApiRequest):
        requests.post(api_request.url, json=api_request.body)

    def request_daily_weather(self, api_request: WeatherApiRequest):
        return requests.get(api_request.url, params=api_request.params)
