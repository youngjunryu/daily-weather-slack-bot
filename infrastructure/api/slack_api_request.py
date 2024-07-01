from infrastructure.api.api_request import ApiRequest


class SlackApiRequest(ApiRequest):
    def __init__(self, url, body):
        super().__init__(url)
        self.body = body
