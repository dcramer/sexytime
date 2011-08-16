# TODO: now and utcnow should return timezone aware objects in UTC format
from __future__ import absolute_import

import pytz
from datetime import datetime

__all__ = ('astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year')

for n in __all__:
    locals()[n] = getattr(datetime, n)

_dt_utcnow = datetime.utcnow

def utcnow():
    dt = _dt_utcnow()
    dt = dt.replace(tzinfo=pytz.utc)
    return dt
now = utcnow
    