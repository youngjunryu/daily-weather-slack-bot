import os

from infrastructure.api.api_request import ApiRequest
from infrastructure.api.weather_api_response import WeatherApiResponse
from utils.date import get_date_for_forecasting


class WeatherApiRequest(ApiRequest):

    def get_url(self):
        return "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

    def get_headers(self):
        return {}

    def get_params(self):
        service_key = os.environ.get("SERVICE_KEY")
        num_of_rows = 217
        page_no = 1
        base_time = "0500"
        nx = 59
        ny = 128
        data_type = "JSON"

        return {
            "serviceKey": service_key,
            "numOfRows": num_of_rows,
            "pageNo": page_no,
            "base_date": get_date_for_forecasting(),
            "base_time": base_time,
            "nx": nx,
            "ny": ny,
            "dataType": data_type,
        }

    def get_body(self):
        return {}

    def parse_response(self, raw_response) -> WeatherApiResponse:
        status_code = raw_response.status_code
        json_response = raw_response.json()
        weather_api_response = WeatherApiResponse(status_code)

        items = json_response["response"]["body"]["items"]["item"]
        max_temperature = None
        hourly_data = {}

        for item in items:
            fcst_time = item["fcstTime"]
            hour = int(fcst_time[:2])  # 0200 -> 02
            fcst_value = item["fcstValue"]

            if hour not in hourly_data:
                hourly_data[hour] = {
                    "temperature": None,
                    "sky_status": None,
                    "precipitation_type": None,
                    "precipitation_probability": None,
                }

            if item["category"] == "TMP":
                hourly_data[hour]["temperature"] = fcst_value
            elif item["category"] == "SKY":
                hourly_data[hour]["sky_status"] = {
                    "1": "맑음",
                    "3": "구름 많음",
                    "4": "흐림",
                }.get(fcst_value, "")
            elif item["category"] == "PTY":
                hourly_data[hour]["precipitation_type"] = {
                    "0": "없음",
                    "1": "비",
                    "2": "비/눈",
                    "3": "눈",
                    "4": "소나기",
                }.get(fcst_value, "")
            elif item["category"] == "POP":
                hourly_data[hour]["precipitation_probability"] = fcst_value
            elif item["category"] == "TMX":
                max_temperature = fcst_value

        for hour, data in hourly_data.items():
            weather_api_response.add_hourly_weather_data(
                hour,
                data["temperature"],
                data["sky_status"],
                data["precipitation_type"],
                data["precipitation_probability"],
            )

        weather_api_response.set_max_temperature(max_temperature)

        return weather_api_response
