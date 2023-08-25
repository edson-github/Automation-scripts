from datetime import datetime, timedelta
from dateutil import tz
import requests


def get_datetime(utc_time):
    """
    Convert date string to datetime object
    """
    return datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')


def get_local_timestamp(utc, from_zone=None):
    """
    Convert 'naive' datetime object to timezone aware datetime object.
    """
    if not from_zone:
        from_zone = tz.tzutc()

    to_zone = tz.tzlocal()  # Auto-detect zone

    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)


def fetchContests():
    API_URL = "https://www.kontests.net/api/v1/all"

    req = requests.get(API_URL)
    return req.json()


def getContests(today=False):
    """
    Returns fetched contests in desired day-wise format
    """
    TOMORROW = get_local_timestamp(
        (datetime.now() + timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0
        ),
        from_zone=tz.tzlocal(),
    )
    contests = fetchContests()
    calendar = {}

    for contest in contests:
        local_start_time = get_local_timestamp(
            get_datetime(contest["start_time"]))
        local_end_time = get_local_timestamp(get_datetime(contest["end_time"]))

        contest["start_time"] = local_start_time.strftime(
            "%I:%M %p, %d %b '%y")
        contest["end_time"] = local_end_time.strftime(
            "%I:%M %p, %d %b '%y")

        if local_end_time <= TOMORROW:  # If contest has already ended, skip
            continue
        elif local_start_time <= TOMORROW:
            # If contest is open today
            key = f"""Today ({datetime.now().strftime("%d %b '%y")})"""
        elif today:
            return calendar
        else:
            key = local_start_time.strftime("%d %B, %Y")

        if key not in calendar:
            calendar[key] = [contest]
        else:
            calendar[key].append(contest)

    return calendar


def printCalendar(today):
    calendar = getContests(today)
    for day, contests in calendar.items():
        print(f"\n\n{day}:")
        for contest in contests:
            print()
            print(f"\t{contest['name']} [{contest['site']}]")
            print(f"\t{contest['start_time']}  -  {contest['end_time']}")
            print(f"\tContest URL: {contest['url']}")
