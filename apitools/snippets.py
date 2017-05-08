from django.utils.timezone import localtime
import datetime

def lt_day_str(datetime_obj):
    if type(datetime_obj) == datetime:
        return localtime(datetime_obj).strftime("%Y-%m-%d")
    else:
        return ""


def lt_time_str(datetime_obj):
    if type(datetime_obj) == datetime:
        return localtime(datetime_obj).strftime("%Y-%m-%d %H:%M:%S")
    else:
        return ""

