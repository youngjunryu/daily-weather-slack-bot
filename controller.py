import sys

from dotenv import load_dotenv

from infrastructure.client.api_client import ApiClient
from infrastructure.parser.slack_api_data_factory import SlackApiDataFactory
from infrastructure.parser.weather_api_data_factory import WeatherApiDataFactory

load_dotenv()


def forecast():
    api_client = ApiClient()

    weather_api_data_factory = WeatherApiDataFactory()
    weather_raw_response = api_client.request_daily_weather(
        weather_api_data_factory.generate_request_data()
    )
    weather_api_response = weather_api_data_factory.parse_response_data(
        weather_raw_response
    )
    weather_api_response.print()

    slack_api_data_factory = SlackApiDataFactory()
    api_client.send_slack_message(slack_api_data_factory.generate_request_data())


def run():
    forecast()
    if len(sys.argv) < 2:
        print("Usage: python controller.py forecast")
        return

    if sys.argv[1] == "forecast":
        forecast()


if __name__ == "__main__":
    run()
