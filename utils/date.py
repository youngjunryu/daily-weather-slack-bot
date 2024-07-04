from datetime import datetime, timezone, timedelta


def get_date_for_forecasting():
    kst = timezone(timedelta(hours=9))
    now_kst = datetime.now(kst)
    return now_kst.strftime("%Y%m%d")


def get_date():
    kst = timezone(timedelta(hours=9))
    now_kst = datetime.now(kst)
    return now_kst.strftime("%Y년 %m월 %d일")
