from infrastructure.mapper.api_data_mapper import ApiDataMapper


class WeatherToSlackDataMapper(ApiDataMapper):

    def mapper(self) -> dict:
        return {1: 1}
