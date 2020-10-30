from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import matplotlib.dates as mdates
import datetime
import numpy as np


class DatetimeSuite:

    @staticmethod
    def _datetime_range(startDate, endDate, deltaDate):
        current = startDate
        while current < endDate:
            yield current
            current += deltaDate
        return

    def setup(self):
        self.listOfDates = [date for date in self._datetime_range(
                              datetime.datetime(2020, 1, 1, 0, 1),
                              datetime.datetime(2020, 12, 31, 23, 59),
                              datetime.timedelta(minutes=5))]

    def time_conversion(self):
        self.datenum = mdates.date2num(self.listOfDates)


class Datetime64Suite:

    def setup(self):
        self.listOfDates = np.arange('2010-01-01', '2011-01-01',
                                     np.timedelta64(1200, 's'),
                                     dtype='datetime64[s]')

    def time_conversion(self):
        self.datenum = mdates.date2num(self.listOfDates)
