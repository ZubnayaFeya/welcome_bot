import datetime


def prepare_datetime(dt: datetime.timedelta):
    dt = dt.total_seconds()
    d = int(dt // (3600 * 24))
    h = int(dt // 3600) - d * 24
    m = int(dt // 60 - d * 24 * 60 - h * 60)
    return f'{d} дней, {h} часов, {m} минут'
