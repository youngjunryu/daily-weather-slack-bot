import os

from infrastructure.api.slack_api_request import SlackApiRequest
from infrastructure.parser.api_parser_factory import ApiParserFactory


class SlackApiParserFactory(ApiParserFactory):
    def generate_api_request(self):
        slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
        body = self.generate_body()
        return SlackApiRequest(url=slack_webhook_url, body=body)

    def generate_api_response(self):
        pass

    def generate_body(self, message="Hello, world!"):
        return {"text": message}
