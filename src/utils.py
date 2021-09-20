import pytz
import dateutil.parser
from datetime import datetime, timedelta

def get_datetime_tz():
    return datetime.now(pytz.timezone('Asia/Singapore'))

def get_datetime_from_str(datetime_str : str):
    return dateutil.parser.parse(datetime_str)

def get_nearest_hour():
    t = datetime.now(pytz.timezone('Asia/Singapore'))
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour) + timedelta(hours=t.minute//30))

def get_nearest_hour_add_10mins():
    t = datetime.now(pytz.timezone('Asia/Singapore'))
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=10, hour=t.hour) + timedelta(hours=t.minute//30))