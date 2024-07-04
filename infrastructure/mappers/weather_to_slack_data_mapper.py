class WeatherToSlackDataMapper:

    def mapper(self, api_response):
        blocks = []
        blocks.append(self.generate_max_temperature(api_response.max_temperature))
        blocks.append(self.generate_divider())
        for hourly_weather in api_response.hourly_weather_data:
            if hourly_weather["hour"] % 2 != 0:
                continue
            blocks.append(self.generate_time(hourly_weather["hour"]))
            blocks.append(
                self.generate_temperature_and_sky_status(
                    hourly_weather["temperature"], hourly_weather["sky_status"]
                )
            )
            blocks.append(
                self.generate_precipitation(
                    hourly_weather["precipitation_type"],
                    hourly_weather["precipitation_probability"],
                )
            )
            blocks.append(self.generate_divider())
        return {"blocks": blocks}

    def generate_divider(self):
        return {"type": "divider"}

    def generate_max_temperature(self, max_temperature):
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":tada: *오늘의 날씨* :tada: \n\n *최고 기온: {max_temperature} ℃*",
            },
        }

    def generate_time(self, hour):
        return {"type": "section", "text": {"type": "mrkdwn", "text": f"`{hour}시`"}}

    def generate_temperature_and_sky_status(self, temperature, sky_status):
        sky_status_emojis = {
            "맑음": ":sunny:",
            "구름 많음": ":barely_sunny:",
            "흐림": ":cloud:",
        }

        sky_status_emoji = sky_status_emojis.get(sky_status, "")

        return {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": f"기온: {temperature} ℃        |   하늘 상태: {sky_status_emoji}",
                "emoji": True,
            },
        }

    def generate_precipitation(self, precipitation_type, precipitation_probability):
        precipitation_emojis = {
            "없음": ":heavy_multiplication_x:",
            "비": ":umbrella_with_rain_drops:",
            "비/눈": ":snow_cloud:",
            "눈": ":snowflake:",
            "소나기": ":droplet:",
        }

        precipitation_emoji = precipitation_emojis.get(precipitation_type, "")

        return {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": f"강수 형태: {precipitation_emoji}   |   강수 확률: {precipitation_probability}%",
                "emoji": True,
            },
        }
