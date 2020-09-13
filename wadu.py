# -*- coding: utf-8 -*-

#                      __
#   .--.--.--.---.-.--|  |.--.--.
#   |  |  |  |  _  |  _  ||  |  |
#   |________|___._|_____||_____|
#

"""Recurrence rules for calendar events."""

from bisect import bisect_left
from collections import namedtuple
from datetime import datetime
from operator import attrgetter
from sys import version_info


__title__   = 'wadu'
__version__ = '0.0.1'
__summary__ = "Recurrence rules for calendar events"
__url__     = 'https://github.com/christophercrouzet/wadu'
__author__  = "Christopher Crouzet"
__contact__ = 'christopher.crouzet@gmail.com'
__license__ = "Unlicense"


if version_info[0] == 2:
    _range = xrange
else:
    _range = range


_MAX_YEAR = 9999
_MAX_DTTM = (9999, 12, 31, 23, 59, 59)


_WEEK_DAYS = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)


class WeekDay(int):
    """Day of the week with optional occurence number."""

    def __new__(cls, week_day, n=None):
        # type: (type, int, Optional[int]) -> WeekDay
        assert 1 <= week_day <= 7
        inst = super(WeekDay, cls).__new__(cls, week_day)
        inst.n = n
        return inst

    def __call__(self, n):
        # type: (int) -> WeekDay
        return self.__class__(self, n)

    def __repr__(self):
        # type: () -> str
        return (_WEEK_DAYS[self - 1] if self.n is None
                else '{:+d} {}'.format(self.n, _WEEK_DAYS[self - 1]))

    __str__ = __repr__

    def __hash__(self):
        # type: () -> int
        return hash((int(self), self.n))


#   Public Constants
# ------------------------------------------------------------------------------

YEARLY   = 0
MONTHLY  = 1
WEEKLY   = 2
DAILY    = 3
HOURLY   = 4
MINUTELY = 5
SECONDLY = 6

JANUARY   = 1
FEBRUARY  = 2
MARCH     = 3
APRIL     = 4
MAY       = 5
JUNE      = 6
JULY      = 7
AUGUST    = 8
SEPTEMBER = 9
OCTOBER   = 10
NOVEMBER  = 11
DECEMBER  = 12

MONDAY    = WeekDay(1)
TUESDAY   = WeekDay(2)
WEDNESDAY = WeekDay(3)
THURSDAY  = WeekDay(4)
FRIDAY    = WeekDay(5)
SATURDAY  = WeekDay(6)
SUNDAY    = WeekDay(7)


#   Helpers
# ------------------------------------------------------------------------------

_DOW_IDXS = (0, 1, 2, 3, 4, 5, 6)

# Number of days for each month.
_DOM_COUNT = (
    # Non-leap year.
    (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
    # Leap year.
    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
)

# Number of days elapsed in the year at the beginning of each month.
_DOY_COUNT = (
    # Non-leap year.
    (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365),
    # Leap year.
    (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366),
)

# Information about the calendar day for each day in a year.
# It returns a tuple containing the year's offset, the month, and the day.
_DT_INFO = (
    # Non-leap year.
    (
        (-1, 12, 25), (-1, 12, 26), (-1, 12, 27), (-1, 12, 28), (-1, 12, 29),
        (-1, 12, 30), (-1, 12, 31),

        (+0,  1,  1), (+0,  1,  2), (+0,  1,  3), (+0,  1,  4), (+0,  1,  5),
        (+0,  1,  6), (+0,  1,  7), (+0,  1,  8), (+0,  1,  9), (+0,  1, 10),
        (+0,  1, 11), (+0,  1, 12), (+0,  1, 13), (+0,  1, 14), (+0,  1, 15),
        (+0,  1, 16), (+0,  1, 17), (+0,  1, 18), (+0,  1, 19), (+0,  1, 20),
        (+0,  1, 21), (+0,  1, 22), (+0,  1, 23), (+0,  1, 24), (+0,  1, 25),
        (+0,  1, 26), (+0,  1, 27), (+0,  1, 28), (+0,  1, 29), (+0,  1, 30),
        (+0,  1, 31), (+0,  2,  1), (+0,  2,  2), (+0,  2,  3), (+0,  2,  4),
        (+0,  2,  5), (+0,  2,  6), (+0,  2,  7), (+0,  2,  8), (+0,  2,  9),
        (+0,  2, 10), (+0,  2, 11), (+0,  2, 12), (+0,  2, 13), (+0,  2, 14),
        (+0,  2, 15), (+0,  2, 16), (+0,  2, 17), (+0,  2, 18), (+0,  2, 19),
        (+0,  2, 20), (+0,  2, 21), (+0,  2, 22), (+0,  2, 23), (+0,  2, 24),
        (+0,  2, 25), (+0,  2, 26), (+0,  2, 27), (+0,  2, 28), (+0,  3,  1),
        (+0,  3,  2), (+0,  3,  3), (+0,  3,  4), (+0,  3,  5), (+0,  3,  6),
        (+0,  3,  7), (+0,  3,  8), (+0,  3,  9), (+0,  3, 10), (+0,  3, 11),
        (+0,  3, 12), (+0,  3, 13), (+0,  3, 14), (+0,  3, 15), (+0,  3, 16),
        (+0,  3, 17), (+0,  3, 18), (+0,  3, 19), (+0,  3, 20), (+0,  3, 21),
        (+0,  3, 22), (+0,  3, 23), (+0,  3, 24), (+0,  3, 25), (+0,  3, 26),
        (+0,  3, 27), (+0,  3, 28), (+0,  3, 29), (+0,  3, 30), (+0,  3, 31),
        (+0,  4,  1), (+0,  4,  2), (+0,  4,  3), (+0,  4,  4), (+0,  4,  5),
        (+0,  4,  6), (+0,  4,  7), (+0,  4,  8), (+0,  4,  9), (+0,  4, 10),
        (+0,  4, 11), (+0,  4, 12), (+0,  4, 13), (+0,  4, 14), (+0,  4, 15),
        (+0,  4, 16), (+0,  4, 17), (+0,  4, 18), (+0,  4, 19), (+0,  4, 20),
        (+0,  4, 21), (+0,  4, 22), (+0,  4, 23), (+0,  4, 24), (+0,  4, 25),
        (+0,  4, 26), (+0,  4, 27), (+0,  4, 28), (+0,  4, 29), (+0,  4, 30),
        (+0,  5,  1), (+0,  5,  2), (+0,  5,  3), (+0,  5,  4), (+0,  5,  5),
        (+0,  5,  6), (+0,  5,  7), (+0,  5,  8), (+0,  5,  9), (+0,  5, 10),
        (+0,  5, 11), (+0,  5, 12), (+0,  5, 13), (+0,  5, 14), (+0,  5, 15),
        (+0,  5, 16), (+0,  5, 17), (+0,  5, 18), (+0,  5, 19), (+0,  5, 20),
        (+0,  5, 21), (+0,  5, 22), (+0,  5, 23), (+0,  5, 24), (+0,  5, 25),
        (+0,  5, 26), (+0,  5, 27), (+0,  5, 28), (+0,  5, 29), (+0,  5, 30),
        (+0,  5, 31), (+0,  6,  1), (+0,  6,  2), (+0,  6,  3), (+0,  6,  4),
        (+0,  6,  5), (+0,  6,  6), (+0,  6,  7), (+0,  6,  8), (+0,  6,  9),
        (+0,  6, 10), (+0,  6, 11), (+0,  6, 12), (+0,  6, 13), (+0,  6, 14),
        (+0,  6, 15), (+0,  6, 16), (+0,  6, 17), (+0,  6, 18), (+0,  6, 19),
        (+0,  6, 20), (+0,  6, 21), (+0,  6, 22), (+0,  6, 23), (+0,  6, 24),
        (+0,  6, 25), (+0,  6, 26), (+0,  6, 27), (+0,  6, 28), (+0,  6, 29),
        (+0,  6, 30), (+0,  7,  1), (+0,  7,  2), (+0,  7,  3), (+0,  7,  4),
        (+0,  7,  5), (+0,  7,  6), (+0,  7,  7), (+0,  7,  8), (+0,  7,  9),
        (+0,  7, 10), (+0,  7, 11), (+0,  7, 12), (+0,  7, 13), (+0,  7, 14),
        (+0,  7, 15), (+0,  7, 16), (+0,  7, 17), (+0,  7, 18), (+0,  7, 19),
        (+0,  7, 20), (+0,  7, 21), (+0,  7, 22), (+0,  7, 23), (+0,  7, 24),
        (+0,  7, 25), (+0,  7, 26), (+0,  7, 27), (+0,  7, 28), (+0,  7, 29),
        (+0,  7, 30), (+0,  7, 31), (+0,  8,  1), (+0,  8,  2), (+0,  8,  3),
        (+0,  8,  4), (+0,  8,  5), (+0,  8,  6), (+0,  8,  7), (+0,  8,  8),
        (+0,  8,  9), (+0,  8, 10), (+0,  8, 11), (+0,  8, 12), (+0,  8, 13),
        (+0,  8, 14), (+0,  8, 15), (+0,  8, 16), (+0,  8, 17), (+0,  8, 18),
        (+0,  8, 19), (+0,  8, 20), (+0,  8, 21), (+0,  8, 22), (+0,  8, 23),
        (+0,  8, 24), (+0,  8, 25), (+0,  8, 26), (+0,  8, 27), (+0,  8, 28),
        (+0,  8, 29), (+0,  8, 30), (+0,  8, 31), (+0,  9,  1), (+0,  9,  2),
        (+0,  9,  3), (+0,  9,  4), (+0,  9,  5), (+0,  9,  6), (+0,  9,  7),
        (+0,  9,  8), (+0,  9,  9), (+0,  9, 10), (+0,  9, 11), (+0,  9, 12),
        (+0,  9, 13), (+0,  9, 14), (+0,  9, 15), (+0,  9, 16), (+0,  9, 17),
        (+0,  9, 18), (+0,  9, 19), (+0,  9, 20), (+0,  9, 21), (+0,  9, 22),
        (+0,  9, 23), (+0,  9, 24), (+0,  9, 25), (+0,  9, 26), (+0,  9, 27),
        (+0,  9, 28), (+0,  9, 29), (+0,  9, 30), (+0, 10,  1), (+0, 10,  2),
        (+0, 10,  3), (+0, 10,  4), (+0, 10,  5), (+0, 10,  6), (+0, 10,  7),
        (+0, 10,  8), (+0, 10,  9), (+0, 10, 10), (+0, 10, 11), (+0, 10, 12),
        (+0, 10, 13), (+0, 10, 14), (+0, 10, 15), (+0, 10, 16), (+0, 10, 17),
        (+0, 10, 18), (+0, 10, 19), (+0, 10, 20), (+0, 10, 21), (+0, 10, 22),
        (+0, 10, 23), (+0, 10, 24), (+0, 10, 25), (+0, 10, 26), (+0, 10, 27),
        (+0, 10, 28), (+0, 10, 29), (+0, 10, 30), (+0, 10, 31), (+0, 11,  1),
        (+0, 11,  2), (+0, 11,  3), (+0, 11,  4), (+0, 11,  5), (+0, 11,  6),
        (+0, 11,  7), (+0, 11,  8), (+0, 11,  9), (+0, 11, 10), (+0, 11, 11),
        (+0, 11, 12), (+0, 11, 13), (+0, 11, 14), (+0, 11, 15), (+0, 11, 16),
        (+0, 11, 17), (+0, 11, 18), (+0, 11, 19), (+0, 11, 20), (+0, 11, 21),
        (+0, 11, 22), (+0, 11, 23), (+0, 11, 24), (+0, 11, 25), (+0, 11, 26),
        (+0, 11, 27), (+0, 11, 28), (+0, 11, 29), (+0, 11, 30), (+0, 12,  1),
        (+0, 12,  2), (+0, 12,  3), (+0, 12,  4), (+0, 12,  5), (+0, 12,  6),
        (+0, 12,  7), (+0, 12,  8), (+0, 12,  9), (+0, 12, 10), (+0, 12, 11),
        (+0, 12, 12), (+0, 12, 13), (+0, 12, 14), (+0, 12, 15), (+0, 12, 16),
        (+0, 12, 17), (+0, 12, 18), (+0, 12, 19), (+0, 12, 20), (+0, 12, 21),
        (+0, 12, 22), (+0, 12, 23), (+0, 12, 24), (+0, 12, 25), (+0, 12, 26),
        (+0, 12, 27), (+0, 12, 28), (+0, 12, 29), (+0, 12, 30), (+0, 12, 31),

        (+1,  1,  1), (+1,  1,  2), (+1,  1,  3), (+1,  1,  4), (+1,  1,  5),
        (+1,  1,  6), (+1,  1,  7),
    ),
    # Leap year.
    (
        (-1, 12, 25), (-1, 12, 26), (-1, 12, 27), (-1, 12, 28), (-1, 12, 29),
        (-1, 12, 30), (-1, 12, 31),

        (+0,  1,  1), (+0,  1,  2), (+0,  1,  3), (+0,  1,  4), (+0,  1,  5),
        (+0,  1,  6), (+0,  1,  7), (+0,  1,  8), (+0,  1,  9), (+0,  1, 10),
        (+0,  1, 11), (+0,  1, 12), (+0,  1, 13), (+0,  1, 14), (+0,  1, 15),
        (+0,  1, 16), (+0,  1, 17), (+0,  1, 18), (+0,  1, 19), (+0,  1, 20),
        (+0,  1, 21), (+0,  1, 22), (+0,  1, 23), (+0,  1, 24), (+0,  1, 25),
        (+0,  1, 26), (+0,  1, 27), (+0,  1, 28), (+0,  1, 29), (+0,  1, 30),
        (+0,  1, 31), (+0,  2,  1), (+0,  2,  2), (+0,  2,  3), (+0,  2,  4),
        (+0,  2,  5), (+0,  2,  6), (+0,  2,  7), (+0,  2,  8), (+0,  2,  9),
        (+0,  2, 10), (+0,  2, 11), (+0,  2, 12), (+0,  2, 13), (+0,  2, 14),
        (+0,  2, 15), (+0,  2, 16), (+0,  2, 17), (+0,  2, 18), (+0,  2, 19),
        (+0,  2, 20), (+0,  2, 21), (+0,  2, 22), (+0,  2, 23), (+0,  2, 24),
        (+0,  2, 25), (+0,  2, 26), (+0,  2, 27), (+0,  2, 28), (+0,  2, 29),
        (+0,  3,  1), (+0,  3,  2), (+0,  3,  3), (+0,  3,  4), (+0,  3,  5),
        (+0,  3,  6), (+0,  3,  7), (+0,  3,  8), (+0,  3,  9), (+0,  3, 10),
        (+0,  3, 11), (+0,  3, 12), (+0,  3, 13), (+0,  3, 14), (+0,  3, 15),
        (+0,  3, 16), (+0,  3, 17), (+0,  3, 18), (+0,  3, 19), (+0,  3, 20),
        (+0,  3, 21), (+0,  3, 22), (+0,  3, 23), (+0,  3, 24), (+0,  3, 25),
        (+0,  3, 26), (+0,  3, 27), (+0,  3, 28), (+0,  3, 29), (+0,  3, 30),
        (+0,  3, 31), (+0,  4,  1), (+0,  4,  2), (+0,  4,  3), (+0,  4,  4),
        (+0,  4,  5), (+0,  4,  6), (+0,  4,  7), (+0,  4,  8), (+0,  4,  9),
        (+0,  4, 10), (+0,  4, 11), (+0,  4, 12), (+0,  4, 13), (+0,  4, 14),
        (+0,  4, 15), (+0,  4, 16), (+0,  4, 17), (+0,  4, 18), (+0,  4, 19),
        (+0,  4, 20), (+0,  4, 21), (+0,  4, 22), (+0,  4, 23), (+0,  4, 24),
        (+0,  4, 25), (+0,  4, 26), (+0,  4, 27), (+0,  4, 28), (+0,  4, 29),
        (+0,  4, 30), (+0,  5,  1), (+0,  5,  2), (+0,  5,  3), (+0,  5,  4),
        (+0,  5,  5), (+0,  5,  6), (+0,  5,  7), (+0,  5,  8), (+0,  5,  9),
        (+0,  5, 10), (+0,  5, 11), (+0,  5, 12), (+0,  5, 13), (+0,  5, 14),
        (+0,  5, 15), (+0,  5, 16), (+0,  5, 17), (+0,  5, 18), (+0,  5, 19),
        (+0,  5, 20), (+0,  5, 21), (+0,  5, 22), (+0,  5, 23), (+0,  5, 24),
        (+0,  5, 25), (+0,  5, 26), (+0,  5, 27), (+0,  5, 28), (+0,  5, 29),
        (+0,  5, 30), (+0,  5, 31), (+0,  6,  1), (+0,  6,  2), (+0,  6,  3),
        (+0,  6,  4), (+0,  6,  5), (+0,  6,  6), (+0,  6,  7), (+0,  6,  8),
        (+0,  6,  9), (+0,  6, 10), (+0,  6, 11), (+0,  6, 12), (+0,  6, 13),
        (+0,  6, 14), (+0,  6, 15), (+0,  6, 16), (+0,  6, 17), (+0,  6, 18),
        (+0,  6, 19), (+0,  6, 20), (+0,  6, 21), (+0,  6, 22), (+0,  6, 23),
        (+0,  6, 24), (+0,  6, 25), (+0,  6, 26), (+0,  6, 27), (+0,  6, 28),
        (+0,  6, 29), (+0,  6, 30), (+0,  7,  1), (+0,  7,  2), (+0,  7,  3),
        (+0,  7,  4), (+0,  7,  5), (+0,  7,  6), (+0,  7,  7), (+0,  7,  8),
        (+0,  7,  9), (+0,  7, 10), (+0,  7, 11), (+0,  7, 12), (+0,  7, 13),
        (+0,  7, 14), (+0,  7, 15), (+0,  7, 16), (+0,  7, 17), (+0,  7, 18),
        (+0,  7, 19), (+0,  7, 20), (+0,  7, 21), (+0,  7, 22), (+0,  7, 23),
        (+0,  7, 24), (+0,  7, 25), (+0,  7, 26), (+0,  7, 27), (+0,  7, 28),
        (+0,  7, 29), (+0,  7, 30), (+0,  7, 31), (+0,  8,  1), (+0,  8,  2),
        (+0,  8,  3), (+0,  8,  4), (+0,  8,  5), (+0,  8,  6), (+0,  8,  7),
        (+0,  8,  8), (+0,  8,  9), (+0,  8, 10), (+0,  8, 11), (+0,  8, 12),
        (+0,  8, 13), (+0,  8, 14), (+0,  8, 15), (+0,  8, 16), (+0,  8, 17),
        (+0,  8, 18), (+0,  8, 19), (+0,  8, 20), (+0,  8, 21), (+0,  8, 22),
        (+0,  8, 23), (+0,  8, 24), (+0,  8, 25), (+0,  8, 26), (+0,  8, 27),
        (+0,  8, 28), (+0,  8, 29), (+0,  8, 30), (+0,  8, 31), (+0,  9,  1),
        (+0,  9,  2), (+0,  9,  3), (+0,  9,  4), (+0,  9,  5), (+0,  9,  6),
        (+0,  9,  7), (+0,  9,  8), (+0,  9,  9), (+0,  9, 10), (+0,  9, 11),
        (+0,  9, 12), (+0,  9, 13), (+0,  9, 14), (+0,  9, 15), (+0,  9, 16),
        (+0,  9, 17), (+0,  9, 18), (+0,  9, 19), (+0,  9, 20), (+0,  9, 21),
        (+0,  9, 22), (+0,  9, 23), (+0,  9, 24), (+0,  9, 25), (+0,  9, 26),
        (+0,  9, 27), (+0,  9, 28), (+0,  9, 29), (+0,  9, 30), (+0, 10,  1),
        (+0, 10,  2), (+0, 10,  3), (+0, 10,  4), (+0, 10,  5), (+0, 10,  6),
        (+0, 10,  7), (+0, 10,  8), (+0, 10,  9), (+0, 10, 10), (+0, 10, 11),
        (+0, 10, 12), (+0, 10, 13), (+0, 10, 14), (+0, 10, 15), (+0, 10, 16),
        (+0, 10, 17), (+0, 10, 18), (+0, 10, 19), (+0, 10, 20), (+0, 10, 21),
        (+0, 10, 22), (+0, 10, 23), (+0, 10, 24), (+0, 10, 25), (+0, 10, 26),
        (+0, 10, 27), (+0, 10, 28), (+0, 10, 29), (+0, 10, 30), (+0, 10, 31),
        (+0, 11,  1), (+0, 11,  2), (+0, 11,  3), (+0, 11,  4), (+0, 11,  5),
        (+0, 11,  6), (+0, 11,  7), (+0, 11,  8), (+0, 11,  9), (+0, 11, 10),
        (+0, 11, 11), (+0, 11, 12), (+0, 11, 13), (+0, 11, 14), (+0, 11, 15),
        (+0, 11, 16), (+0, 11, 17), (+0, 11, 18), (+0, 11, 19), (+0, 11, 20),
        (+0, 11, 21), (+0, 11, 22), (+0, 11, 23), (+0, 11, 24), (+0, 11, 25),
        (+0, 11, 26), (+0, 11, 27), (+0, 11, 28), (+0, 11, 29), (+0, 11, 30),
        (+0, 12,  1), (+0, 12,  2), (+0, 12,  3), (+0, 12,  4), (+0, 12,  5),
        (+0, 12,  6), (+0, 12,  7), (+0, 12,  8), (+0, 12,  9), (+0, 12, 10),
        (+0, 12, 11), (+0, 12, 12), (+0, 12, 13), (+0, 12, 14), (+0, 12, 15),
        (+0, 12, 16), (+0, 12, 17), (+0, 12, 18), (+0, 12, 19), (+0, 12, 20),
        (+0, 12, 21), (+0, 12, 22), (+0, 12, 23), (+0, 12, 24), (+0, 12, 25),
        (+0, 12, 26), (+0, 12, 27), (+0, 12, 28), (+0, 12, 29), (+0, 12, 30),
        (+0, 12, 31),

        (+1,  1,  1), (+1,  1,  2), (+1,  1,  3), (+1,  1,  4), (+1,  1,  5),
        (+1,  1,  6), (+1,  1,  7),
    ),
)

# Location of the first day of the year in the table ‘_DT_INFO’.
_DT_INFO_OFFSET = 7


def _is_leap_year(year):
    # type: (int) -> int
    """Checks whether the given year is a leap year."""
    return int(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def _get_day_count_before_year(year):
    # type: (int) -> int
    """Retrieves the number of days elapsed before a given year."""
    year -= 1
    return (year * 365) + (year // 4) - (year // 100) + (year // 400)


def _get_ord_dt(year, month, day):
    # type: (int, int, int) -> int
    """Retrieves an ordinal date."""
    return (_get_day_count_before_year(year)
            + _DOY_COUNT[_is_leap_year(year)][month - 1]
            + day)


def _get_dt_from_doy(year, is_leap, doy):
    # type: (int, int, int) -> Tuple[int, int, int]
    """Retrieves a date from a day of year."""
    dt_info = _DT_INFO[is_leap][doy + _DT_INFO_OFFSET]
    return (year + dt_info[0], dt_info[1], dt_info[2])


def _get_week_count_in_year(first_doy, is_leap, sow_offset):
    # type: (int, int, int) -> int
    """Retrieves the number of weeks for a given year."""
    dow = (first_doy - sow_offset) % 7
    return 52 + (dow == THURSDAY or (dow == WEDNESDAY and is_leap))


def _get_first_iso_doy(first_doy, sow_offset):
    # type: (int, int) -> int
    """Retrieves the first day of the first ISO week for a year."""
    dow = (first_doy - sow_offset - 1) % 7
    return (first_doy - dow) + (dow >= THURSDAY) * 7


def _normalize_dt(year, month, day):
    # type: (int, int, int) -> Tuple[int, int, int]
    """Normalizes a date by making it valid."""
    while True:
        is_leap = _is_leap_year(year)
        dom_count = _DOM_COUNT[is_leap]
        while month <= DECEMBER:
            last_dom = dom_count[month - 1]
            if day <= last_dom:
                return year, month, day

            month += 1
            day -= last_dom

        year += 1
        month -= 12


def _normalize_tm(hour, minute, second):
    # type: (int, int, int) -> Tuple[int, int, int]
    """Normalizes a time by making it valid."""
    carry, second = divmod(second, 60)
    minute += carry

    carry, minute = divmod(minute, 60)
    hour += carry

    carry, hour = divmod(hour, 24)
    return (carry, hour, minute, second)


def _normalize_dttm(year,    # type: int
                    month,   # type: int
                    day,     # type: int
                    hour,    # type: int
                    minute,  # type: int
                    second   # type: int
                    ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Normalizes a date time by making it valid."""
    day_carry, hour, minute, second = _normalize_tm(hour, minute, second)
    year, month, day = _normalize_dt(year, month, day + day_carry)
    return (year, month, day, hour, minute, second)


#   Start Date Adjustment
# ------------------------------------------------------------------------------

def _adjust_yearly_start_date(year, month, day):
    # type: (int, int, int) -> Tuple[int, int, int]
    """Adjusts the yearly frequency's starting date."""
    return (year, 1, 1)


def _adjust_monthly_start_date(year, month, day):
    # type: (int, int, int) -> Tuple[int, int, int]
    """Adjusts the monthly frequency's starting date."""
    return (year, month, 1)


def _adjust_weekly_start_date(year, month, day):
    # type: (int, int, int) -> Tuple[int, int, int]
    """Adjusts the weekly frequency's starting date."""
    is_leap = _is_leap_year(year)
    first_doy = _get_day_count_before_year(year) + 1

    dt = first_doy + _DOY_COUNT[is_leap][month - 1] + day - 1
    doy = dt - (dt - 1) % 7 - first_doy
    return _get_dt_from_doy(year, is_leap, doy)


def _adjust_daily_start_date(year, month, day):
    # type: (int, int, int) -> Tuple[int, int, int]
    """Adjusts the daily frequency's starting date."""
    return (year, month, day)


_ADJUST_START_DATE_FNS = (
    _adjust_yearly_start_date,
    _adjust_monthly_start_date,
    _adjust_weekly_start_date,
    _adjust_daily_start_date,
)


#   Logical Year
# ------------------------------------------------------------------------------

def _get_yearly_logical_year(year, month, day):
    # type: (int, int, int) -> int
    """Retrieves the logical year for a yearly frequency."""
    return year


def _get_monthly_logical_year(year, month, day):
    # type: (int, int, int) -> int
    """Retrieves the logical year for a monthly frequency."""
    return year


def _get_weekly_logical_year(year, month, day):
    # type: (int, int, int) -> int
    """Retrieves the logical year for a weekly frequency."""
    is_leap = _is_leap_year(year)

    # The logical year depends on the 4th day of the week.
    doy = _DOY_COUNT[is_leap][month - 1] + day - 1
    doy += 3
    return year + _DT_INFO[is_leap][doy + _DT_INFO_OFFSET][0]


def _get_daily_logical_year(year, month, day):
    # type: (int, int, int) -> int
    """Retrieves the logical year for a daily frequency."""
    return year


_GET_LOGICAL_YEAR_FNS = (
    _get_yearly_logical_year,
    _get_monthly_logical_year,
    _get_weekly_logical_year,
    _get_daily_logical_year,
)


#   Days of Year Range
# ------------------------------------------------------------------------------

def _get_yearly_doys_range(year, month, day, is_leap, iso_offset):
    # type: (int, int, int, int, int) -> Tuple[int, ...]
    """Retrieves the day of year's range for a yearly frequency."""
    # return tuple(_range(0, 365 + is_leap))
    doy_count = _DOY_COUNT[is_leap]

    first_doy = _get_day_count_before_year(year) + 1
    first_iso_doy = _get_first_iso_doy(first_doy, 0)
    begin = max(min(first_doy, first_iso_doy), doy_count[month - 1] + day)
    begin -= first_doy

    next_first_doy = first_doy + 365 + is_leap
    next_first_iso_doy = _get_first_iso_doy(next_first_doy, 0)
    end = max(next_first_doy, next_first_iso_doy)
    end -= first_doy

    return tuple(_range(begin, end))


def _get_monthly_doys_range(year, month, day, is_leap, iso_offset):
    # type: (int, int, int, int, int) -> Tuple[int, ...]
    """Retrieves the day of year's range for a monthly frequency."""
    doy_count = _DOY_COUNT[is_leap]
    return tuple(_range(doy_count[month - 1], doy_count[month]))


def _get_weekly_doys_range(year, month, day, is_leap, iso_offset):
    # type: (int, int, int, int, int) -> Tuple[int, ...]
    """Retrieves the day of year's range for a weekly frequency."""
    doy = _DOY_COUNT[is_leap][month - 1] + day - 1
    week = (doy - iso_offset) // 7
    begin = week * 7 + iso_offset
    return tuple(_range(begin, begin + 7))


def _get_daily_doys_range(year, month, day, is_leap, iso_offset):
    # type: (int, int, int, int, int) -> Tuple[int, ...]
    """Retrieves the day of year's range for a daily frequency."""
    doy = _DOY_COUNT[is_leap][month - 1] + day - 1
    return (doy,)


_GET_DOYS_RANGE_FNS = (
    _get_yearly_doys_range,
    _get_monthly_doys_range,
    _get_weekly_doys_range,
    _get_daily_doys_range,
)


#   Stepping
# ------------------------------------------------------------------------------

def _advance_yearly_dttm(year,     # type: int
                         month,    # type: int
                         day,      # type: int
                         hour,     # type: int
                         minute,   # type: int
                         second,   # type: int
                         interval  # type: int
                         ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Advances the date time by the given yearly interval."""
    return (year + interval, month, day, hour, minute, second)


def _advance_monthly_dttm(year,     # type: int
                          month,    # type: int
                          day,      # type: int
                          hour,     # type: int
                          minute,   # type: int
                          second,   # type: int
                          interval  # type: int
                          ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Advances the date time by the given monthly interval."""
    month += interval
    year_offset, month = divmod(month - 1, 12)
    year += year_offset
    month += 1
    return (year, month, day, hour, minute, second)


def _advance_weekly_dttm(year,     # type: int
                         month,    # type: int
                         day,      # type: int
                         hour,     # type: int
                         minute,   # type: int
                         second,   # type: int
                         interval  # type: int
                         ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Advances the date time by the given weekly interval."""
    day += interval * 7
    year, month, day = _normalize_dt(year, month, day)
    return (year, month, day, hour, minute, second)


def _advance_daily_dttm(year,     # type: int
                        month,    # type: int
                        day,      # type: int
                        hour,     # type: int
                        minute,   # type: int
                        second,   # type: int
                        interval  # type: int
                        ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Advances the date time by the given daily interval."""
    day += interval
    year, month, day = _normalize_dt(year, month, day)
    return (year, month, day, hour, minute, second)


def _advance_hourly_dttm(year,     # type: int
                         month,    # type: int
                         day,      # type: int
                         hour,     # type: int
                         minute,   # type: int
                         second,   # type: int
                         interval  # type: int
                         ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Advances the date time by the given hourly interval."""
    hour += interval
    return _normalize_dttm(year, month, day, hour, minute, second)


def _advance_minutely_dttm(year,     # type: int
                           month,    # type: int
                           day,      # type: int
                           hour,     # type: int
                           minute,   # type: int
                           second,   # type: int
                           interval  # type: int
                           ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Advances the date time by the given hourly interval."""
    minute += interval
    return _normalize_dttm(year, month, day, hour, minute, second)


def _advance_secondly_dttm(year,     # type: int
                           month,    # type: int
                           day,      # type: int
                           hour,     # type: int
                           minute,   # type: int
                           second,   # type: int
                           interval  # type: int
                           ):
    # type: (...) -> Tuple[int, int, int, int, int, int]
    """Advances the date time by the given hourly interval."""
    second += interval
    return _normalize_dttm(year, month, day, hour, minute, second)


_ADVANCE_DTTM_FNS = (
    _advance_yearly_dttm,
    _advance_monthly_dttm,
    _advance_weekly_dttm,
    _advance_daily_dttm,
    _advance_hourly_dttm,
    _advance_minutely_dttm,
    _advance_secondly_dttm,
)


#   Weeks of Year
#
# Exclusively used by the ‘on months’ property, this retrieves all the weeks
# in a year matching the given week day.
# ------------------------------------------------------------------------------

def _get_week_for_nth_week_day_in_year(week_day,   # type: WeekDay
                                       is_leap,    # type: int
                                       first_doy,  # type: int
                                       sow_offset  # type: int
                                       ):
    # type: (...) -> Optional[int]
    """Retrieves the week for the n-th week day in the year."""
    first_dow = first_doy % 7
    week_offset = int(week_day < first_dow and first_dow <= THURSDAY)

    week_count = (
        _get_week_count_in_year(first_doy, is_leap, sow_offset)
        - week_offset)

    if not -week_count < week_day.n < week_count:
        return None

    # Retrieve the n-th week in the year as a 0-based index.
    return week_day.n % (week_count + 1) - 1 + week_offset


def _get_week_for_nth_week_day_in_month(week_day,   # type: WeekDay
                                        month,      # type: int
                                        is_leap,    # type: int
                                        first_doy,  # type: int
                                        iso_offset  # type: int
                                        ):
    # type: (...) -> int
    """Retrieves the week for the n-th week day in the month."""
    doy_count = _DOY_COUNT[is_leap]

    doy = first_doy + doy_count[month - 1]
    dow = doy % 7
    first_week_day_dom = doy + (week_day - dow) % 7

    doy = first_doy + doy_count[month] - 1
    dow = doy % 7
    last_week_day_dom = doy - (dow - week_day) % 7

    week_day_count = (last_week_day_dom - first_week_day_dom) // 7 + 1

    if week_day.n < -week_day_count or week_day.n > week_day_count:
        return None

    # Retrieve the n-th week in the year as a 0-based index.
    n = week_day.n % (week_day_count + 1) - 1
    return ((first_week_day_dom + n * 7) - first_doy - iso_offset) // 7


def _get_yearly_woys(week_day,    # type: WeekDay
                     lo_week,     # type: int
                     hi_week,     # type: int
                     is_leap,     # type: int
                     first_doy,   # type: int
                     iso_offset,  # type: int
                     sow_offset   # type: int
                     ):
    # type: (...) -> Iterable[int]
    """Retrieves the week days in the year for a yearly frequency."""
    if week_day.n is None:
        return _range(lo_week, hi_week)

    week = _get_week_for_nth_week_day_in_year(
        week_day, is_leap, first_doy, sow_offset)
    if not lo_week <= week < hi_week:
        return ()

    return () if week is None else (week,)


def _get_monthly_woys(week_day,    # type: WeekDay
                      lo_week,     # type: int
                      hi_week,     # type: int
                      is_leap,     # type: int
                      first_doy,   # type: int
                      iso_offset,  # type: int
                      sow_offset   # type: int
                      ):
    # type: (...) -> Iterable[int]
    """Retrieves the week days in the year for a monthly frequency."""
    if week_day.n is None:
        return _range(lo_week, hi_week)

    dt_info = _DT_INFO[is_leap]

    lo_month = dt_info[lo_week * 7 + iso_offset][1]
    hi_month = dt_info[(hi_week - 1) * 7 + iso_offset][1] + 1
    weeks = (
        _get_week_for_nth_week_day_in_month(
            week_day, x, is_leap, first_doy, iso_offset)
        for x in _range(lo_month, hi_month))
    weeks = tuple(weeks)
    return tuple(x for x in weeks if x is not None and lo_week <= x < hi_week)


def _get_weekly_woys(week_day,    # type: WeekDay
                     lo_week,     # type: int
                     hi_week,     # type: int
                     is_leap,     # type: int
                     first_doy,   # type: int
                     iso_offset,  # type: int
                     sow_offset   # type: int
                     ):
    # type: (...) -> Iterable[int]
    """Retrieves the week days in the year for a weekly frequency."""
    return _range(lo_week, hi_week)


def _get_daily_woys(week_day,    # type: WeekDay
                    lo_week,     # type: int
                    hi_week,     # type: int
                    is_leap,     # type: int
                    first_doy,   # type: int
                    iso_offset,  # type: int
                    sow_offset   # type: int
                    ):
    # type: (...) -> Iterable[int]
    """Retrieves the week days in the year for a daily frequency."""
    return _range(lo_week, hi_week)


_GET_WOYS_FNS = (
    _get_yearly_woys,
    _get_monthly_woys,
    _get_weekly_woys,
    _get_daily_woys,
)


#   Properties
# ------------------------------------------------------------------------------

_PROP_ON_MONTHS     = 0
_PROP_ON_WEEKS      = 1
_PROP_ON_YEAR_DAYS  = 2
_PROP_ON_MONTH_DAYS = 3
_PROP_ON_WEEK_DAYS  = 4
_PROP_ON_HOURS      = 5
_PROP_ON_MINUTES    = 6
_PROP_ON_SECONDS    = 7


_PROPS = (
    'on_months',
    'on_weeks',
    'on_year_days',
    'on_month_days',
    'on_week_days',
    'on_hours',
    'on_minutes',
    'on_seconds',
)


class _Property(object):

    def __init__(self, kind, handler, values):
        # type: (int, Callable, Sequence[int]) -> None
        self.kind = kind
        self.handler = handler
        self.values = values

    def __repr__(self):
        # type: () -> str
        return '_Property(kind=\'{}\', values={})'.format(_PROPS[self.kind],
                                                          self.values)


_MONTHS_EXPAND = 1 << 0


_Bounds = namedtuple(
    'Bounds', (
        'lo',
        'hi',
    ))


_DateContext = namedtuple(
    'DateContext', (
        'freq',                   # int
        'start',                  # int
        'first_doy',              # int
        'is_leap',                # int
        'iso_offset',             # int
        'sow_offset',             # int
        'on_months_behaviour',    # int
        'on_week_days_woy_freq',  # int
        'bounds',                 # _Bounds
    ))


_TimeContext = namedtuple(
    'TimeContext', (
        'freq',  # int
    ))


def _handle_months_prop(values,  # type: Sequence[int]
                        months,  # type: Sequence[int]
                        context  # type: _DateContext
                        ):
    # type: (...) -> Sequence[int]
    """Processes the given months."""
    freq = context.freq
    start = context.start
    is_leap = context.is_leap
    behaviour = context.on_months_behaviour
    bounds = context.bounds

    assert all(JANUARY <= x <= DECEMBER for x in months)

    dom_count = _DOM_COUNT[is_leap]
    doy_count = _DOY_COUNT[is_leap]
    dt_info = _DT_INFO[is_leap]

    if freq >= MONTHLY:
        return tuple(x for x in values
                     if dt_info[x + _DT_INFO_OFFSET][1] in months)

    # Restrict the bounds to the current year.
    bounds = _Bounds(lo=max(bounds.lo, 0), hi=min(bounds.hi, 365 + is_leap))

    # Convert the bounds in terms of months.
    lo_info = dt_info[bounds.lo + _DT_INFO_OFFSET]
    hi_info = dt_info[bounds.hi + _DT_INFO_OFFSET - 1]
    lo_month = max(lo_info[0] * 12 + lo_info[1], 1)
    hi_month = min(hi_info[0] * 12 + hi_info[1], 12)

    # Retrieve the values for this property.
    if behaviour & _MONTHS_EXPAND:
        it = (doy_count[x - 1] + y
              for x in months
              for y in _range(
                  lo_info[2] - 1 if x == lo_month else 0,
                  hi_info[2] - 1 if (x - 1) == hi_month else dom_count[x - 1]))
    else:
        it = (doy_count[x - 1] + start[2] - 1
              for x in months
              if start[2] <= dom_count[x - 1])

    return tuple(x for x in it if x in values)


def _handle_weeks_prop(values,  # type: Sequence[int]
                       weeks,   # type: Sequence[int]
                       context  # type: _DateContext
                       ):
    # type: (...) -> Sequence[int]
    """Processes all the days for the given weeks."""
    freq = context.freq
    is_leap = context.is_leap
    first_doy = context.first_doy
    iso_offset = context.iso_offset
    sow_offset = context.sow_offset
    bounds = context.bounds

    assert all(-53 <= x <= 53 and x != 0 for x in weeks)

    week_count = _get_week_count_in_year(first_doy, is_leap, sow_offset)

    # Wrap around negative weeks. Also convert them into 0-based indices.
    begin = bisect_left(weeks, -week_count)
    end = bisect_left(weeks, week_count + 1)
    weeks = weeks[begin:end]
    weeks = sorted(x % (week_count + 1) - 1 for x in weeks)

    if freq >= WEEKLY:
        return tuple(x for x in values
                     if ((x - iso_offset) // 7) % week_count in weeks)

    # Convert the bounds in terms of weeks and week days as 0-based indices.
    lo_week, lo_dow = divmod(bounds.lo - iso_offset, 7)
    hi_week, hi_dow = divmod(bounds.hi - iso_offset + 6, 7)

    # Retrieve the values for this prop.
    begin = bisect_left(_DOW_IDXS, lo_dow)
    end = bisect_left(_DOW_IDXS, hi_dow)
    it = (x * 7 + y + iso_offset
          for x in weeks
          for y in _DOW_IDXS[begin if x == lo_week else None:
                             end if (x - 1) == hi_week else None])
    return tuple(x for x in it if x in values)


def _handle_year_days_prop(values,     # type: Sequence[int]
                           year_days,  # type: Sequence[int]
                           context     # type: _DateContext
                           ):
    # type: (...) -> Sequence[int]
    """Processes the given year days."""
    freq = context.freq
    is_leap = context.is_leap
    bounds = context.bounds

    assert all(-366 <= x <= 366 and x != 0 for x in year_days)

    doy_count = 365 + is_leap

    # Wrap around negative year days. Also convert them into 0-based indices.
    begin = bisect_left(year_days, -doy_count)
    end = bisect_left(year_days, doy_count + 1)
    year_days = year_days[begin:end]
    year_days = sorted(x % (doy_count + 1) - 1 for x in year_days)

    # Retrieve the values for this property.
    return tuple(x for x in year_days if x in values)


def _handle_month_days_prop(values,      # type: Sequence[int]
                            month_days,  # type: Sequence[int]
                            context      # type: _DateContext
                            ):
    # type: (...) -> Sequence[int]
    """Processes the given days for each month."""
    is_leap = context.is_leap
    bounds = context.bounds

    assert all(-31 <= x <= 31 and x != 0 for x in month_days)

    dom_count = _DOM_COUNT[is_leap]
    doy_count = _DOY_COUNT[is_leap]
    dt_info = _DT_INFO[is_leap]

    # Convert the bounds in terms of months and days as 0-based indices.
    _, lo_month, lo_dom = dt_info[bounds.lo + _DT_INFO_OFFSET]
    _, hi_month, hi_dom = dt_info[bounds.hi + _DT_INFO_OFFSET - 1]
    lo_month -= 1
    lo_dom -= 1

    doys_per_month = []
    for month in _range(lo_month, hi_month):
        doms = month_days
        day_count = dom_count[month]

        # Wrap around negative days. Also convert them into 0-based indices.
        begin = bisect_left(doms, -day_count)
        end = bisect_left(doms, day_count + 1)
        doms = doms[begin:end]
        doms = sorted(x % (day_count + 1) - 1 for x in doms)

        # Retrieve the values for the current month.
        doys_per_month.append(tuple(doy_count[month] + x for x in doms))

    return tuple(y for x in doys_per_month for y in x if y in values)


def _handle_week_days_prop(values,     # type: Sequence[int]
                           week_days,  # type: Sequence[WeekDay]
                           context     # type: _DateContext
                           ):
    # type: (...) -> Sequence[int]
    """Processes the given days for each week."""
    freq = context.freq
    is_leap = context.is_leap
    first_doy = context.first_doy
    iso_offset = context.iso_offset
    sow_offset = context.sow_offset
    bounds = context.bounds
    woy_freq = context.on_week_days_woy_freq

    get_woys = _GET_WOYS_FNS[woy_freq]

    assert all(MONDAY <= x <= SUNDAY for x in week_days)
    assert all(x.n is None or -53 <= x.n <= 53 for x in week_days)

    # Convert the bounds in terms of weeks as 0-based indices.
    lo_week = (bounds.lo - iso_offset) // 7
    hi_week = (bounds.hi - iso_offset) // 7 + 1

    # Build a list of all the year days as 0-based indices.
    doys = sorted(y * 7 + (x - 1) + iso_offset - sow_offset
                  for x in week_days
                  for y in get_woys(x,
                                    lo_week,
                                    hi_week,
                                    is_leap,
                                    first_doy,
                                    iso_offset,
                                    sow_offset))

    # Retrieve the values for this property.
    return tuple(x for x in doys if x in values)


def _handle_hours_prop(values,  # type: Sequence[Tuple[int, int, int]]
                       hours,   # type: Sequence[int]
                       context  # type: _TimeContext
                       ):
    # type: (...) -> Sequence[int, int, int]
    """Processes the given hours."""
    freq = context.freq

    if freq >= HOURLY:
        return tuple(x for x in values if x[0] in hours)

    return tuple((y, x[1], x[2]) for x in values for y in hours)


def _handle_minutes_prop(values,   # type: Sequence[Tuple[int, int, int]]
                         minutes,  # type: Sequence[int]
                         context   # type: _TimeContext
                         ):
    # type: (...) -> Sequence[int, int, int]
    """Processes the given minutes."""
    freq = context.freq

    if freq >= MINUTELY:
        return tuple(x for x in values if x[1] in minutes)

    return tuple((x[0], y, x[2]) for x in values for y in minutes)


def _handle_seconds_prop(values,   # type: Sequence[Tuple[int, int, int]]
                         seconds,  # type: Sequence[int]
                         context   # type: _TimeContext
                         ):
    # type: (...) -> Sequence[int, int, int]
    """Processes the given seconds."""
    freq = context.freq

    if freq >= SECONDLY:
        return tuple(x for x in values if x[2] in seconds)

    return tuple((x[0], x[1], y) for x in values for y in seconds)


def _create_dt_props(on_months=None,      # type: Optional[Sequence[int]]
                     on_weeks=None,       # type: Optional[Sequence[int]]
                     on_year_days=None,   # type: Optional[Sequence[int]]
                     on_month_days=None,  # type: Optional[Sequence[int]]
                     on_week_days=None    # type: Optional[Sequence[WeekDay]]
                     ):
    # type: (...) -> Tuple[_Property, ...]
    """Creates the date properties."""
    props = []

    if on_months is not None:
        props.append(_Property(_PROP_ON_MONTHS,
                     _handle_months_prop,
                     tuple(sorted(set(on_months)))))

    if on_weeks is not None:
        props.append(_Property(_PROP_ON_WEEKS,
                     _handle_weeks_prop,
                     tuple(sorted(set(on_weeks)))))

    if on_year_days is not None:
        props.append(_Property(_PROP_ON_YEAR_DAYS,
                     _handle_year_days_prop,
                     tuple(sorted(set(on_year_days)))))

    if on_month_days is not None:
        props.append(_Property(_PROP_ON_MONTH_DAYS,
                     _handle_month_days_prop,
                     tuple(sorted(set(on_month_days)))))

    if on_week_days is not None:
        props.append(_Property(_PROP_ON_WEEK_DAYS,
                     _handle_week_days_prop,
                     tuple(sorted(set(on_week_days)))))

    return tuple(props)


def _create_tm_props(on_hours=None,    # type: Optional[Sequence[int]]
                     on_minutes=None,  # type: Optional[Sequence[int]]
                     on_seconds=None   # type: Optional[Sequence[int]]
                     ):
    # type: (...) -> Tuple[_Property, ...]
    """Creates the time properties."""
    props = []

    if on_hours is not None:
        props.append(_Property(_PROP_ON_HOURS,
                     _handle_hours_prop,
                     tuple(sorted(set(on_hours)))))

    if on_minutes is not None:
        props.append(_Property(_PROP_ON_MINUTES,
                     _handle_minutes_prop,
                     tuple(sorted(set(on_minutes)))))

    if on_seconds is not None:
        props.append(_Property(_PROP_ON_SECONDS,
                     _handle_seconds_prop,
                     tuple(sorted(set(on_seconds)))))

    return tuple(props)


def _add_implicit_dt_props(props,      # type: Tuple[_Property, ...]
                           freq,       # type: int
                           year,       # type: int
                           month,      # type: int
                           day,        # type: int
                           sow_offset  # type: int
                           ):
    # type: (...) -> Tuple[_Property, ...]
    """Adds any implicit date properties."""
    dow = WeekDay((_get_ord_dt(year, month, day) - sow_offset - 1) % 7 + 1)
    kinds = tuple(x.kind for x in props)

    if freq == YEARLY:
        if _PROP_ON_YEAR_DAYS in kinds:
            return props

        if ((_PROP_ON_MONTHS not in kinds
             and _PROP_ON_WEEKS not in kinds)
                and (_PROP_ON_MONTH_DAYS in kinds
                     or _PROP_ON_WEEK_DAYS not in kinds)
                ):
            extras = (
                _Property(_PROP_ON_MONTHS,
                          _handle_months_prop,
                          (month,)),
            )
        elif (_PROP_ON_MONTH_DAYS not in kinds
                and _PROP_ON_WEEKS not in kinds
                and _PROP_ON_WEEK_DAYS not in kinds
                ):
            extras = (
                _Property(_PROP_ON_MONTH_DAYS,
                          _handle_month_days_prop,
                          (day,)),
            )
        elif (_PROP_ON_WEEKS in kinds
                and _PROP_ON_MONTH_DAYS not in kinds
                and _PROP_ON_WEEK_DAYS not in kinds
                ):
            extras = (
                _Property(_PROP_ON_WEEK_DAYS,
                          _handle_week_days_prop,
                          (dow,)),
            )
        else:
            return props
    elif freq == MONTHLY:
        if (_PROP_ON_MONTH_DAYS in kinds
                or _PROP_ON_WEEK_DAYS in kinds
                ):
            return props

        extras = (
            _Property(_PROP_ON_MONTH_DAYS,
                      _handle_month_days_prop,
                      (day,)),
        )
    elif freq == WEEKLY:
        if _PROP_ON_WEEK_DAYS in kinds:
            return props

        extras = (
            _Property(_PROP_ON_WEEK_DAYS,
                      _handle_week_days_prop,
                      (dow,)),
        )
    else:
        return props

    return tuple(sorted(props + extras, key=attrgetter('kind')))


#   Sets
# ------------------------------------------------------------------------------

def _get_dt_set(
        year,                   # type: int
        month,                  # type: int
        day,                    # type: int
        freq,                   # type: int
        start,                  # type: Tuple[int, int, int, int, int, int]
        sow_offset,             # type: int
        on_months_behaviour,    # type: int
        on_week_days_woy_freq,  # type: int
        props                   # type: Sequence[_Property]
        ):
    # type: (...) -> Tuple[int, int, int]
    """Retrieves the date sets."""
    # When the frequency is weekly, the first day of the week might
    # belong to a year when the week belongs to another year.
    # The logical year represents the actual year for the current
    # range of dates to process.
    logical_year = _GET_LOGICAL_YEAR_FNS[freq](year, month, day)

    # Retrieve the first day of the logical year as an ordinal date.
    first_doy = _get_day_count_before_year(logical_year) + 1

    # Retrieve whether the logical year is a leap year.
    is_leap = _is_leap_year(logical_year)

    # Retrieve the number of days between the first day of the year and
    # the first day of the first ISO week for that same year.
    iso_offset = _get_first_iso_doy(first_doy, sow_offset) - first_doy

    # Retrieve all the year days over the frequency's range.
    doys = _GET_DOYS_RANGE_FNS[freq](year, month, day, is_leap, iso_offset)

    # Apply the date properties.
    for prop in props:
        bounds = _Bounds(lo=min(doys), hi=max(doys) + 1)
        context = _DateContext(freq,
                               start,
                               first_doy,
                               is_leap,
                               iso_offset,
                               sow_offset,
                               on_months_behaviour,
                               on_week_days_woy_freq,
                               bounds)
        doys = prop.handler(doys, prop.values, context)
        if not doys:
            return None

    return tuple(_get_dt_from_doy(logical_year, is_leap, x) for x in doys)


def _get_tm_set(hour, minute, second, freq, props):
    # type: (int, int, int, int, Sequence[_Property]) -> Tuple[int, int, int]
    """Retrieves the time sets."""
    out = ((hour, minute, second),)
    context = _TimeContext(freq)
    for prop in props:
        out = prop.handler(out, prop.values, context)
        if not out:
            return None

    return out


#   Public API
# ------------------------------------------------------------------------------

class RecurrenceRule(object):
    """Recurrence rule iterator."""

    def __init__(self,
                 freq,                # type: int
                 interval=1,          # type: int
                 week_start=MONDAY,   # type: WeekDay
                 on_months=None,      # type: Optional[Sequence[int]]
                 on_weeks=None,       # type: Optional[Sequence[int]]
                 on_year_days=None,   # type: Optional[Sequence[int]]
                 on_month_days=None,  # type: Optional[Sequence[WeekDay]]
                 on_week_days=None,   # type: Optional[Sequence[int]]
                 on_hours=None,       # type: Optional[Sequence[int]]
                 on_minutes=None,     # type: Optional[Sequence[int]]
                 on_seconds=None,     # type: Optional[Sequence[int]]
                 on_set_pos=None,     # type: Optional[Sequence[int]]
                 count=None,          # type: Optional[int]
                 until=None           # type: Optional[datetime]
                 ):
        # type: (...) -> None
        if (on_week_days is not None
                and any(x.n is not None for x in on_week_days)
                and freq not in (YEARLY, MONTHLY)
                ):
            raise ValueError("N-th week day occurrences can only be set when "
                             "the frequency is either yearly or monthly.")

        dt_props = _create_dt_props(on_months=on_months,
                                    on_weeks=on_weeks,
                                    on_year_days=on_year_days,
                                    on_month_days=on_month_days,
                                    on_week_days=on_week_days)
        tm_props = _create_tm_props(on_hours=on_hours,
                                    on_minutes=on_minutes,
                                    on_seconds=on_seconds)

        until = _MAX_DTTM if until is None else until.timetuple()[:6]

        self._freq = freq
        self._interval = interval
        self._week_start = week_start
        self._dt_props = dt_props
        self._tm_props = tm_props
        self._on_set_pos = on_set_pos
        self._count = count
        self._until = until

    def __iter__(self):
        # type: () -> Iterator[datetime]
        return self.iterate_from(datetime.now())

    def iterate_from(self, start):
        # type: (datetime) -> Iterator[datetime]
        start = start.timetuple()[:6]

        advance_dttm = _ADVANCE_DTTM_FNS[self._freq]

        # Retrieve the start of the week relatively to Monday.
        sow_offset = self._week_start - MONDAY

        # The ‘on months’ property, if any, outputs a single day for each given
        # month when it is the one and only property of the recurrence rule.
        # Otherwise, it outputs the days for the whole given months.
        on_months_behaviour = _MONTHS_EXPAND if len(self._dt_props) > 1 else 0

        on_week_days_woy_freq = (
            MONTHLY if (self._freq == YEARLY
                        and any(x.kind == _PROP_ON_MONTHS
                                for x in self._dt_props))
            else self._freq)

        if self._dt_props:
            get_dt_set = _get_dt_set
        else:
            get_dt_set = lambda y, m, d, *args, **kwargs: ((y, m, d),)

        if self._tm_props:
            get_tm_set = _get_tm_set
        else:
            get_tm_set = lambda h, m, s, *args, **kwargs: ((h, m, s),)

        year, month, day, hour, minute, second = start

        dt_props = _add_implicit_dt_props(
            self._dt_props, self._freq, year, month, day, sow_offset)

        count = 0
        while True:

            # Retrieve the date and time sets.
            dt_set = get_dt_set(year,
                                month,
                                day,
                                self._freq,
                                start,
                                sow_offset,
                                on_months_behaviour,
                                on_week_days_woy_freq,
                                dt_props)
            tm_set = get_tm_set(
                hour, minute, second, self._freq, self._tm_props)

            if dt_set is not None and tm_set is not None:
                # Combine the date and time sets.
                dttm_set = tuple(x + y for x in dt_set for y in tm_set)

                if self._on_set_pos is not None:
                    # Wrap around negative set positions. Also convert them
                    # into 0-based indices.
                    on_set_pos = self._on_set_pos
                    begin = bisect_left(self._on_set_pos, -len(dttm_set))
                    end = bisect_left(self._on_set_pos, len(dttm_set) + 1)
                    on_set_pos = on_set_pos[begin:end]
                    on_set_pos = sorted(x % (len(dttm_set) + 1) - 1
                                        for x in on_set_pos)

                    # Filter the date and time set based on the set positions.
                    dttm_set = tuple(dttm_set[i] for i in on_set_pos)

                # Output the resulting values as date objects.
                for dttm in dttm_set:
                    # Exit whenever a date is beyond the given until date.
                    if dttm > self._until:
                        return

                    # Skip any date before the given start date.
                    if dttm < start:
                        continue

                    try:
                        dttm = datetime(*dttm)
                    except ValueError:
                        # Skip any date that falls on an invalid date,
                        # such as leap days.
                        continue

                    if dttm.year > _MAX_YEAR:
                        raise RuntimeError("The date is out of range")

                    yield dttm

                    count += 1
                    if self._count is not None and count >= self._count:
                        return

            year, month, day, hour, minute, second = advance_dttm(
                year, month, day, hour, minute, second, self._interval)
