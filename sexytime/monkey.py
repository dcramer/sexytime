"""
sexytime.monkey
~~~~~~~~~~~~~~~

:copyright: (c) 2011 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

import datetime
import imp
import sexytime
import sys

_state = {
    'datetime': datetime.datetime,
}

def patch():
    # ensure we've imported all modules
    import sexytime.datetime

    imp.acquire_lock()
    try:
        module = sys.modules['datetime']
        module.datetime = sexytime.datetime
    finally:
        imp.release_lock()
    
def unpatch():
    imp.acquire_lock()
    try:
        module = sys.modules['datetime']
        module.datetime = _state['datetime']
    finally:
        imp.release_lock()
