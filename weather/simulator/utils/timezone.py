import pytz
from datetime import datetime


class TimeZone:
    # For every timezone say 'Australia/Sydney' create a key:value pair of City and Timezone.
    timezone_map = {timezone.split('/').pop(): timezone for timezone in pytz.all_timezones}

    @classmethod
    def current_local_time(cls, city):
        """
        Return Local time or UTC timezone if not a standard one.

        :param city: city name
        :return: Local Time or UTC
        """
        city_timezone = cls.timezone_map.get(city) or 'UTC'
        timezone = pytz.timezone(city_timezone)

        return datetime.now(tz=timezone).isoformat(timespec='seconds')






