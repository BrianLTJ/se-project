from django.utils.timezone import localtime
import datetime

class tolocaltime():
    def day_str(datetime_obj):
        return localtime(datetime_obj).strftime("%Y-%m-%d")


    def time_str(datetime_obj):
        return localtime(datetime_obj).strftime("%Y-%m-%d")

