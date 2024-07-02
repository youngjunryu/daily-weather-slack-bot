from infrastructure.api.api_response import ApiResponse


class WeatherApiResponse(ApiResponse):
    class WeatherDataDTO:
        def __init__(
            self, temperature, base_date, precipitation_type, precipitation_probability
        ):
            self.temperature = temperature
            self.sky_status = base_date
            self.precipitation_type = precipitation_type
            self.precipitation_probability = precipitation_probability

    def __init__(self, status_code):
        super().__init__(status_code)
        self.max_temperature = None
        self.hourly_weather_data = []

    def set_max_temperature(self, max_temperature):
        self.max_temperature = max_temperature

    def add_hourly_weather_data(
        self,
        hour,
        temperature,
        sky_status,
        precipitation_type,
        precipitation_probability,
    ):
        self.hourly_weather_data.append(
            {
                "hour": hour,
                "temperature": temperature,
                "sky_status": sky_status,
                "precipitation_type": precipitation_type,
                "precipitation_probability": precipitation_probability,
            }
        )
