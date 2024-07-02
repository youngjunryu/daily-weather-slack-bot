import os

from infrastructure.api.weather_api_request import WeatherApiRequest
from infrastructure.api.weather_api_response import WeatherApiResponse
from infrastructure.parser.api_data_factory import ApiDataFactory
from datetime import datetime, timezone, timedelta


class WeatherApiDataFactory(ApiDataFactory):

    def generate_request_data(self) -> WeatherApiRequest:
        url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
        service_key = os.environ.get("SERVICE_KEY")
        num_of_rows = 217
        page_no = 1
        base_time = "0500"
        nx = 59
        ny = 128
        data_type = "JSON"

        return WeatherApiRequest(
            url=url,
            params=self.generate_params(
                service_key, num_of_rows, page_no, base_time, nx, ny, data_type
            ),
        )

    def parse_response_data(self, raw_response) -> WeatherApiResponse:
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

    def generate_params(
        self, service_key, num_of_rows, page_no, base_time, nx, ny, data_type
    ):
        return {
            "serviceKey": service_key,
            "numOfRows": num_of_rows,
            "pageNo": page_no,
            "base_date": self.get_date(),
            "base_time": base_time,
            "nx": nx,
            "ny": ny,
            "dataType": data_type,
        }

    def get_date(self):
        kst = timezone(timedelta(hours=9))
        now_kst = datetime.now(kst)
        return now_kst.strftime("%Y%m%d")
