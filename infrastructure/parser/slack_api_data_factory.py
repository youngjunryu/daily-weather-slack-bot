import os

from infrastructure.api.slack_api_request import SlackApiRequest
from infrastructure.parser.api_data_factory import ApiDataFactory


class SlackApiDataFactory(ApiDataFactory):
    def generate_request_data(self) -> SlackApiRequest:
        slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
        body = self.generate_body()
        return SlackApiRequest(url=slack_webhook_url, body=body)

    def parse_response_data(self, raw_response):
        pass

    def generate_body(self, message="Hello, world!"):
        return {"text": message}
