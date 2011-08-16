``sexytime`` is a replacement for stdlib's ``datetime`` module. It replaces datetime.datetime.{now,utcnow} with functions that are guaranteed to return UTC timezone aware datetime objects.

Usage
=====

The module behaves identical to stdlib's ``datetime``::

    >>> from sexytime import datetime
    >>> datetime.utcnow()
    datetime.datetime(2011, 8, 16, 22, 24, 26, 116079, tzinfo=<UTC>)


You can also completely replace the datetime by monkey patching it. This requires you to execute it before you import datetime submodules elsewhere::

    import sexytime.monkey
    sexytime.monkey.patch()