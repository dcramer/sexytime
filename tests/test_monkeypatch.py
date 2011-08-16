import unittest2

import datetime
from datetime import datetime as org_datetime
import sexytime
import sexytime.monkey

class MonkeyPatchTest(unittest2.TestCase):
    def test_patch(self):
        sexytime.monkey.patch()
        
        self.assertEquals(datetime.datetime, sexytime.datetime)
        
        sexytime.monkey.unpatch()
        
        self.assertNotEquals(datetime.datetime, sexytime.datetime)

        self.assertEquals(datetime.datetime, org_datetime)
