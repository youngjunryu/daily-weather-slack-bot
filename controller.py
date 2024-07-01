import sys

from dotenv import load_dotenv

from infrastructure.client.api_client import ApiClient
from infrastructure.parser.slack_api_parser_factory import SlackApiParserFactory

load_dotenv()


def forecast():
    api_parser_factory = SlackApiParserFactory()
    api_client = ApiClient()
    api_client.send_slack_message(api_parser_factory.generate_api_request())


def run():
    if len(sys.argv) < 2:
        print("Usage: python controller.py forecast")
        return

    if sys.argv[1] == "forecast":
        forecast()


if __name__ == "__main__":
    run()
