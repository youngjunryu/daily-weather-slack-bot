# 소개
[공공데이터포털 기상청 단기예보서비스 OPEN API](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15084084#/tab_layer_detail_function)를 활용하여 매일 06:00 AM KST에 시간대별 날씨 정보를 Slack 메세지로 자동으로 전송하는 Bot 서비스입니다.   
현재는 MVP 수준으로 구현되어 있어 예상하지 못한 오류가 발생할 수 있습니다.

# 사용법
1. To get started, clone the repository and install the required libraries.
```angular2html
$ git clone https://github.com/youngjunryu/daily-weather-bot.git
$ pip install -r requirements.txt
```

2. Set up `SERVICE KEY` and `SLACK WEBHOOK URL` as GitHub Secrets.
3. To run the bot service locally, set the environmeny variables in the `.env` file as follows:
```angular2html
SERVICE_KEY=YOUR_SERVICE_KEY
SLACK_WEBHOOK_URL=YOUR_SLACK_WEBHOOK_URL
```

# 기능
- 매일 06:00 AM KST(GitHub Actions에 따라 약간 몇 분 후 Workflow가 동작될 수 있음)에 날씨 정보를 받을 수 있습니다.
- 날씨 정보는 일 최고 기온, 06:00 ~ 23:00 사이 시간별 기온, 강수 형태, 강수 확률, 하늘 상태를 포함합니다.

# 추가될 기능
- 사용자는 날씨 정보를 받고싶은 위도, 경도를 직접 설정할 수 있다.
- 사용자는 날씨 정보를 받고싶은 시간대를 직접 설정할 수 있다.