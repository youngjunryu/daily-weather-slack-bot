import os

from infrastructure.api.weather_api_request import WeatherApiRequest
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

    def parse_response_data(self, raw_response):
        pass

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
