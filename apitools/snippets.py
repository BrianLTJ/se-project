from django.utils.timezone import localtime
import datetime

def lt_day_str(datetime_obj):
    try:
        return localtime(datetime_obj).strftime("%Y-%m-%d")
    except:
        return ""


def lt_time_str(datetime_obj):
    try:
        return localtime(datetime_obj).strftime("%Y-%m-%d %H:%M:%S")
    except:
        return ""

