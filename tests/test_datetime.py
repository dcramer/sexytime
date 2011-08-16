import pytz
import unittest2

from sexytime import datetime

class DateTimeTest(unittest2.TestCase):
    def test_utcnow_is_utc(self):
        dt = datetime.utcnow()
        self.assertEquals(dt.tzinfo, pytz.utc)
        
    def test_now_is_utc(self):
        dt = datetime.now()
        self.assertEquals(dt.tzinfo, pytz.utc)
        