import os
import sys

import requests
from dotenv import load_dotenv


def send_slack_message(slack_webhook_url):
    requests.post(slack_webhook_url, json={"text": "Forecasting..."})


def forecast():
    print("Forecasting...")

    load_dotenv()
    service_key = os.environ.get("SERVICE_KEY")
    slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

    send_slack_message(slack_webhook_url)


def run():
    if len(sys.argv) < 2:
        print("Usage: python controller.py forecast")
        return

    if sys.argv[1] == "forecast":
        forecast()


if __name__ == "__main__":
    run()
