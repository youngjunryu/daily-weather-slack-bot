import requests


class ApiClient:

    def send_slack_message(self, api_request):
        requests.post(api_request.url, json=api_request.body)
