import datetime


def ensure_datetime_iso_is_valid(datetime_iso: str) -> datetime:
    try:
        return datetime.datetime.strptime(datetime_iso, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.datetime.strptime(datetime_iso, "%Y-%m-%dT%H:%M:%S")
