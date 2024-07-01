from infrastructure.api.api_request import ApiRequest


class WeatherApiRequest(ApiRequest):
    def __init__(
        self,
        url,
        service_key,
        num_of_rows,
        page_no,
        base_date,
        base_time,
        nx,
        ny,
        date_type,
    ):
        super().__init__(url)
        self.url = url
        self.service_key = service_key
        self.num_of_rows = num_of_rows
        self.page_no = page_no
        self.base_date = base_date
        self.base_time = base_time
        self.nx = nx
        self.ny = ny
        self.date_type = date_type

    def generate_params(self):
        return {
            "serviceKey": self.service_key,
            "numOfRows": self.num_of_rows,
            "pageNo": self.page_no,
            "base_date": self.base_date,
            "base_time": self.base_time,
            "nx": self.nx,
            "ny": self.ny,
            "dataType": self.date_type,
        }
