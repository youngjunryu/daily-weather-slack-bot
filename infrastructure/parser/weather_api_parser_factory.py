from controller import SLACK_WEBHOOK_URL, SERVICE_KEY
from infrastructure.api.weather_api_request import WeatherApiRequest
from infrastructure.parser.api_parser_factory import ApiParserFactory
from datetime import datetime, timezone, timedelta


class WeatherApiParserFactory(ApiParserFactory):

    def generate_api_request(self):
        num_of_rows = 217
        page_no = 1
        base_time = "0500"
        nx = 59
        ny = 128
        data_type = "JSON"

        return WeatherApiRequest(
            url=SLACK_WEBHOOK_URL,
            service_key=SERVICE_KEY,
            num_of_rows=num_of_rows,
            page_no=page_no,
            base_date=self.get_date(),
            base_time=base_time,
            nx=nx,
            ny=ny,
            date_type=data_type,
        )

    def generate_api_response(self):
        pass

    def get_date(self):
        kst = timezone(timedelta(hours=9))
        now_kst = datetime.now(kst)
        return now_kst.strftime("%Y%m%d")
