import os

from infrastructure.api.api_request import ApiRequest


class SlackApiRequest(ApiRequest):

    def __init__(self, data):
        self.data = data

    def get_url(self):
        slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
        return slack_webhook_url

    def get_headers(self):
        return {}

    def get_params(self):
        return {}

    def get_body(self):
        return self.data

    def get_method(self):
        return "POST"

    def parse_response(self, response):
        return response
