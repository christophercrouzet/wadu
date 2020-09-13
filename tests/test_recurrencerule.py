#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

_ROOT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(_ROOT_PATH))
del _ROOT_PATH
del os
del sys

# ------------------------------------------------------------------------------

from datetime import datetime
from unittest import (
    TestCase,
    main as unittest_main,
)

from wadu import *


class TestRecurrenceRule(TestCase):
    """Runs tests for the reccurence rule class.

    A majority of the tests are based on Libical
    (https://github.com/libical/libical).
    """

    def test_yearly_on_month_and_week_days(self):
        """Yearly, every day in January.

        RRULE:FREQ=YEARLY;UNTIL=20000131T140000;BYMONTH=1;BYDAY=SU,MO,TU,WE,TH,FR,SA
        DTSTART:19980101T090000
        """
        rule = RecurrenceRule(YEARLY,
                              on_months=(JANUARY,),
                              on_week_days=(
                                  SUNDAY,
                                  MONDAY,
                                  TUESDAY,
                                  WEDNESDAY,
                                  THURSDAY,
                                  FRIDAY,
                                  SATURDAY,
                              ),
                              until=datetime(2000, 1, 31, hour=14))
        start = datetime(1998, 1, 1, hour=9)
        expected = (
            datetime(1998, 1,  1, hour=9),
            datetime(1998, 1,  2, hour=9),
            datetime(1998, 1,  3, hour=9),
            datetime(1998, 1,  4, hour=9),
            datetime(1998, 1,  5, hour=9),
            datetime(1998, 1,  6, hour=9),
            datetime(1998, 1,  7, hour=9),
            datetime(1998, 1,  8, hour=9),
            datetime(1998, 1,  9, hour=9),
            datetime(1998, 1, 10, hour=9),
            datetime(1998, 1, 11, hour=9),
            datetime(1998, 1, 12, hour=9),
            datetime(1998, 1, 13, hour=9),
            datetime(1998, 1, 14, hour=9),
            datetime(1998, 1, 15, hour=9),
            datetime(1998, 1, 16, hour=9),
            datetime(1998, 1, 17, hour=9),
            datetime(1998, 1, 18, hour=9),
            datetime(1998, 1, 19, hour=9),
            datetime(1998, 1, 20, hour=9),
            datetime(1998, 1, 21, hour=9),
            datetime(1998, 1, 22, hour=9),
            datetime(1998, 1, 23, hour=9),
            datetime(1998, 1, 24, hour=9),
            datetime(1998, 1, 25, hour=9),
            datetime(1998, 1, 26, hour=9),
            datetime(1998, 1, 27, hour=9),
            datetime(1998, 1, 28, hour=9),
            datetime(1998, 1, 29, hour=9),
            datetime(1998, 1, 30, hour=9),
            datetime(1998, 1, 31, hour=9),
            datetime(1999, 1,  1, hour=9),
            datetime(1999, 1,  2, hour=9),
            datetime(1999, 1,  3, hour=9),
            datetime(1999, 1,  4, hour=9),
            datetime(1999, 1,  5, hour=9),
            datetime(1999, 1,  6, hour=9),
            datetime(1999, 1,  7, hour=9),
            datetime(1999, 1,  8, hour=9),
            datetime(1999, 1,  9, hour=9),
            datetime(1999, 1, 10, hour=9),
            datetime(1999, 1, 11, hour=9),
            datetime(1999, 1, 12, hour=9),
            datetime(1999, 1, 13, hour=9),
            datetime(1999, 1, 14, hour=9),
            datetime(1999, 1, 15, hour=9),
            datetime(1999, 1, 16, hour=9),
            datetime(1999, 1, 17, hour=9),
            datetime(1999, 1, 18, hour=9),
            datetime(1999, 1, 19, hour=9),
            datetime(1999, 1, 20, hour=9),
            datetime(1999, 1, 21, hour=9),
            datetime(1999, 1, 22, hour=9),
            datetime(1999, 1, 23, hour=9),
            datetime(1999, 1, 24, hour=9),
            datetime(1999, 1, 25, hour=9),
            datetime(1999, 1, 26, hour=9),
            datetime(1999, 1, 27, hour=9),
            datetime(1999, 1, 28, hour=9),
            datetime(1999, 1, 29, hour=9),
            datetime(1999, 1, 30, hour=9),
            datetime(1999, 1, 31, hour=9),
            datetime(2000, 1,  1, hour=9),
            datetime(2000, 1,  2, hour=9),
            datetime(2000, 1,  3, hour=9),
            datetime(2000, 1,  4, hour=9),
            datetime(2000, 1,  5, hour=9),
            datetime(2000, 1,  6, hour=9),
            datetime(2000, 1,  7, hour=9),
            datetime(2000, 1,  8, hour=9),
            datetime(2000, 1,  9, hour=9),
            datetime(2000, 1, 10, hour=9),
            datetime(2000, 1, 11, hour=9),
            datetime(2000, 1, 12, hour=9),
            datetime(2000, 1, 13, hour=9),
            datetime(2000, 1, 14, hour=9),
            datetime(2000, 1, 15, hour=9),
            datetime(2000, 1, 16, hour=9),
            datetime(2000, 1, 17, hour=9),
            datetime(2000, 1, 18, hour=9),
            datetime(2000, 1, 19, hour=9),
            datetime(2000, 1, 20, hour=9),
            datetime(2000, 1, 21, hour=9),
            datetime(2000, 1, 22, hour=9),
            datetime(2000, 1, 23, hour=9),
            datetime(2000, 1, 24, hour=9),
            datetime(2000, 1, 25, hour=9),
            datetime(2000, 1, 26, hour=9),
            datetime(2000, 1, 27, hour=9),
            datetime(2000, 1, 28, hour=9),
            datetime(2000, 1, 29, hour=9),
            datetime(2000, 1, 30, hour=9),
            datetime(2000, 1, 31, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_months(self):
        """Yearly in June and July.

        RRULE:FREQ=YEARLY;COUNT=10;BYMONTH=6,7
        DTSTART:19970610T090000
        """
        rule = RecurrenceRule(YEARLY,
                              on_months=(JUNE, JULY),
                              count=10)
        start = datetime(1997, 6, 10, hour=9)
        expected = (
            datetime(1997, 6, 10, hour=9),
            datetime(1997, 7, 10, hour=9),
            datetime(1998, 6, 10, hour=9),
            datetime(1998, 7, 10, hour=9),
            datetime(1999, 6, 10, hour=9),
            datetime(1999, 7, 10, hour=9),
            datetime(2000, 6, 10, hour=9),
            datetime(2000, 7, 10, hour=9),
            datetime(2001, 6, 10, hour=9),
            datetime(2001, 7, 10, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_years_on_months(self):
        """Every other year on January, February, and March.

        RRULE:FREQ=YEARLY;INTERVAL=2;COUNT=10;BYMONTH=1,2,3
        DTSTART:19970310T090000
        """
        rule = RecurrenceRule(YEARLY,
                              interval=2,
                              on_months=(JANUARY, FEBRUARY, MARCH),
                              count=10)
        start = datetime(1997, 3, 10, hour=9)
        expected = (
            datetime(1997, 3, 10, hour=9),
            datetime(1999, 1, 10, hour=9),
            datetime(1999, 2, 10, hour=9),
            datetime(1999, 3, 10, hour=9),
            datetime(2001, 1, 10, hour=9),
            datetime(2001, 2, 10, hour=9),
            datetime(2001, 3, 10, hour=9),
            datetime(2003, 1, 10, hour=9),
            datetime(2003, 2, 10, hour=9),
            datetime(2003, 3, 10, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_3_years_on_year_days(self):
        """Every third year on the 1st, 100th, and 200th days.

        RRULE:FREQ=YEARLY;INTERVAL=3;COUNT=10;BYYEARDAY=1,100,200
        DTSTART:19970101T090000
        """
        rule = RecurrenceRule(YEARLY,
                              interval=3,
                              on_year_days=(1, 100, 200),
                              count=10)
        start = datetime(1997, 1, 1, hour=9)
        expected = (
            datetime(1997, 1,  1, hour=9),
            datetime(1997, 4, 10, hour=9),
            datetime(1997, 7, 19, hour=9),
            datetime(2000, 1,  1, hour=9),
            datetime(2000, 4,  9, hour=9),
            datetime(2000, 7, 18, hour=9),
            datetime(2003, 1,  1, hour=9),
            datetime(2003, 4, 10, hour=9),
            datetime(2003, 7, 19, hour=9),
            datetime(2006, 1,  1, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_nth_week_day(self):
        """Yearly on the 20th Monday.

        RRULE:FREQ=YEARLY;BYDAY=20MO;COUNT=3
        DTSTART:19970519T090000
        """
        rule = RecurrenceRule(YEARLY,
                              on_week_days=(MONDAY(20),),
                              count=3)
        start = datetime(1997, 5, 19, hour=9)
        expected = (
            datetime(1997, 5, 19, hour=9),
            datetime(1998, 5, 18, hour=9),
            datetime(1999, 5, 17, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_week_and_week_day_1(self):
        """Yearly on Monday of 20th week.

        RRULE:FREQ=YEARLY;BYWEEKNO=20;BYDAY=MO;COUNT=3
        DTSTART:19970512T090000
        """
        rule = RecurrenceRule(YEARLY,
                              on_weeks=(20,),
                              on_week_days=(MONDAY,),
                              count=3)
        start = datetime(1997, 5, 12, hour=9)
        expected = (
            datetime(1997, 5, 12, hour=9),
            datetime(1998, 5, 11, hour=9),
            datetime(1999, 5, 17, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_week_and_week_day_2(self):
        """Yearly on Monday of 20th week.

        With Sunday as the week start.

        RRULE:FREQ=YEARLY;BYWEEKNO=20;BYDAY=MO;WKST=SU;COUNT=3
        DTSTART:19970512T090000
        """
        rule = RecurrenceRule(YEARLY,
                              week_start=SUNDAY,
                              on_weeks=(20,),
                              on_week_days=(MONDAY,),
                              count=3)
        start = datetime(1997, 5, 12, hour=9)
        expected = (
            datetime(1997, 5, 12, hour=9),
            datetime(1998, 5, 18, hour=9),
            datetime(1999, 5, 17, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_week_and_week_day_3(self):
        """Yearly on Monday of 20th week.

        With Friday as the week start.

        RRULE:FREQ=YEARLY;BYWEEKNO=20;BYDAY=MO;WKST=FR;COUNT=3
        DTSTART:19970512T090000
        """
        rule = RecurrenceRule(YEARLY,
                              week_start=FRIDAY,
                              on_weeks=(20,),
                              on_week_days=(MONDAY,),
                              count=3)
        start = datetime(1997, 5, 12, hour=9)
        expected = (
            datetime(1997, 5, 19, hour=9),
            datetime(1998, 5, 18, hour=9),
            datetime(1999, 5, 17, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_month_and_week_day(self):
        """Yearly on every Thursday in March.

        RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=TH;COUNT=11
        DTSTART:19970313T090000
        """
        rule = RecurrenceRule(YEARLY,
                              on_months=(MARCH,),
                              on_week_days=(THURSDAY,),
                              count=11)
        start = datetime(1997, 3, 13, hour=9)
        expected = (
            datetime(1997, 3, 13, hour=9),
            datetime(1997, 3, 20, hour=9),
            datetime(1997, 3, 27, hour=9),
            datetime(1998, 3,  5, hour=9),
            datetime(1998, 3, 12, hour=9),
            datetime(1998, 3, 19, hour=9),
            datetime(1998, 3, 26, hour=9),
            datetime(1999, 3,  4, hour=9),
            datetime(1999, 3, 11, hour=9),
            datetime(1999, 3, 18, hour=9),
            datetime(1999, 3, 25, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_months_and_week_day(self):
        """Yearly on every Thursday of June, July, and August.

        RRULE:FREQ=YEARLY;BYDAY=TH;BYMONTH=6,7,8;COUNT=39
        DTSTART:19970605T090000
        """
        rule = RecurrenceRule(YEARLY,
                              on_months=(JUNE, JULY, AUGUST),
                              on_week_days=(THURSDAY,),
                              count=39)
        start = datetime(1997, 6, 5, hour=9)
        expected = (
            datetime(1997, 6,  5, hour=9),
            datetime(1997, 6, 12, hour=9),
            datetime(1997, 6, 19, hour=9),
            datetime(1997, 6, 26, hour=9),
            datetime(1997, 7,  3, hour=9),
            datetime(1997, 7, 10, hour=9),
            datetime(1997, 7, 17, hour=9),
            datetime(1997, 7, 24, hour=9),
            datetime(1997, 7, 31, hour=9),
            datetime(1997, 8,  7, hour=9),
            datetime(1997, 8, 14, hour=9),
            datetime(1997, 8, 21, hour=9),
            datetime(1997, 8, 28, hour=9),
            datetime(1998, 6,  4, hour=9),
            datetime(1998, 6, 11, hour=9),
            datetime(1998, 6, 18, hour=9),
            datetime(1998, 6, 25, hour=9),
            datetime(1998, 7,  2, hour=9),
            datetime(1998, 7,  9, hour=9),
            datetime(1998, 7, 16, hour=9),
            datetime(1998, 7, 23, hour=9),
            datetime(1998, 7, 30, hour=9),
            datetime(1998, 8,  6, hour=9),
            datetime(1998, 8, 13, hour=9),
            datetime(1998, 8, 20, hour=9),
            datetime(1998, 8, 27, hour=9),
            datetime(1999, 6,  3, hour=9),
            datetime(1999, 6, 10, hour=9),
            datetime(1999, 6, 17, hour=9),
            datetime(1999, 6, 24, hour=9),
            datetime(1999, 7,  1, hour=9),
            datetime(1999, 7,  8, hour=9),
            datetime(1999, 7, 15, hour=9),
            datetime(1999, 7, 22, hour=9),
            datetime(1999, 7, 29, hour=9),
            datetime(1999, 8,  5, hour=9),
            datetime(1999, 8, 12, hour=9),
            datetime(1999, 8, 19, hour=9),
            datetime(1999, 8, 26, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_4_years_on_month_and_week_day_and_month_days(self):
        """Every 4 years on the first Tuesday after a Monday in November.

        RRULE:FREQ=YEARLY;INTERVAL=4;BYMONTH=11;BYDAY=TU;BYMONTHDAY=2,3,4,5,6,7,8;COUNT=3
        DTSTART:19961105T090000
        """
        rule = RecurrenceRule(YEARLY,
                              interval=4,
                              on_months=(NOVEMBER,),
                              on_month_days=(2, 3, 4, 5, 6, 7, 8),
                              on_week_days=(TUESDAY,),
                              count=3)
        start = datetime(1996, 11, 5, hour=9)
        expected = (
            datetime(1996, 11, 5, hour=9),
            datetime(2000, 11, 7, hour=9),
            datetime(2004, 11, 2, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_week_day_and_year_days(self):
        """Yearly, on the Friday in March occurring on or after the 26th.

        RRULE:FREQ=YEARLY;UNTIL=20100326T000000;BYDAY=FR;BYYEARDAY=-275,-276,-277,-278,-279,-280,-281
        DTSTART:20060331T020000
        """
        rule = RecurrenceRule(YEARLY,
                              on_year_days=(
                                  -275,
                                  -276,
                                  -277,
                                  -278,
                                  -279,
                                  -280,
                                  -281,
                              ),
                              on_week_days=(FRIDAY,),
                              until=datetime(2010, 3, 26))
        start = datetime(2006, 3, 31, hour=2)
        expected = (
            datetime(2006, 3, 31, hour=2),
            datetime(2007, 3, 30, hour=2),
            datetime(2008, 3, 28, hour=2),
            datetime(2009, 3, 27, hour=2),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_with_leap_days(self):
        """Yearly, with leap days getting skipped.

        RRULE:FREQ=YEARLY;UNTIL=20140301T115959
        DTSTART:20120229T120000
        """
        rule = RecurrenceRule(YEARLY,
                              until=datetime(
                                  2014, 3, 1, hour=11, minute=59, second=59))
        start = datetime(2012, 2, 29, hour=12)
        expected = (
            datetime(2012, 2, 29, hour=12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_nth_week_day_1(self):
        """Monthly on the first Friday.

        RRULE:FREQ=MONTHLY;COUNT=10;BYDAY=1FR
        DTSTART:19970905T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_week_days=(FRIDAY(1),),
                              count=10)
        start = datetime(1997, 9, 5, hour=9)
        expected = (
            datetime(1997,  9, 5, hour=9),
            datetime(1997, 10, 3, hour=9),
            datetime(1997, 11, 7, hour=9),
            datetime(1997, 12, 5, hour=9),
            datetime(1998,  1, 2, hour=9),
            datetime(1998,  2, 6, hour=9),
            datetime(1998,  3, 6, hour=9),
            datetime(1998,  4, 3, hour=9),
            datetime(1998,  5, 1, hour=9),
            datetime(1998,  6, 5, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_nth_week_day_2(self):
        """Monthly on the first Friday.

        RRULE:FREQ=MONTHLY;UNTIL=19971224T000000;BYDAY=1FR
        DTSTART:19970905T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_week_days=(FRIDAY(1),),
                              until=datetime(1997, 12, 24))
        start = datetime(1997, 9, 5, hour=9)
        expected = (
            datetime(1997,  9, 5, hour=9),
            datetime(1997, 10, 3, hour=9),
            datetime(1997, 11, 7, hour=9),
            datetime(1997, 12, 5, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_nth_week_day_3(self):
        """Monthly on the second to last Monday.

        RRULE:FREQ=MONTHLY;COUNT=6;BYDAY=-2MO
        DTSTART:19970922T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_week_days=(MONDAY(-2),),
                              count=6)
        start = datetime(1997, 9, 22, hour=9)
        expected = (
            datetime(1997,  9, 22, hour=9),
            datetime(1997, 10, 20, hour=9),
            datetime(1997, 11, 17, hour=9),
            datetime(1997, 12, 22, hour=9),
            datetime(1998,  1, 19, hour=9),
            datetime(1998,  2, 16, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_months_on_nth_week_days(self):
        """Every other month on the first and last Sunday.

        RRULE:FREQ=MONTHLY;INTERVAL=2;COUNT=10;BYDAY=1SU,-1SU
        DTSTART:19970907T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              interval=2,
                              on_week_days=(SUNDAY(1), SUNDAY(-1)),
                              count=10)
        start = datetime(1997, 9, 7, hour=9)
        expected = (
            datetime(1997,  9,  7, hour=9),
            datetime(1997,  9, 28, hour=9),
            datetime(1997, 11,  2, hour=9),
            datetime(1997, 11, 30, hour=9),
            datetime(1998,  1,  4, hour=9),
            datetime(1998,  1, 25, hour=9),
            datetime(1998,  3,  1, hour=9),
            datetime(1998,  3, 29, hour=9),
            datetime(1998,  5,  3, hour=9),
            datetime(1998,  5, 31, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_month_day_1(self):
        """Monthly on the third to last day.

        RRULE:FREQ=MONTHLY;BYMONTHDAY=-3;COUNT=6
        DTSTART:19970928T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(-3,),
                              count=6)
        start = datetime(1997, 9, 28, hour=9)
        expected = (
            datetime(1997,  9, 28, hour=9),
            datetime(1997, 10, 29, hour=9),
            datetime(1997, 11, 28, hour=9),
            datetime(1997, 12, 29, hour=9),
            datetime(1998,  1, 29, hour=9),
            datetime(1998,  2, 26, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_month_days_1(self):
        """Monthly on the 2nd and 15th days.

        RRULE:FREQ=MONTHLY;COUNT=10;BYMONTHDAY=2,15
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(2, 15),
                              count=10)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9, 15, hour=9),
            datetime(1997, 10,  2, hour=9),
            datetime(1997, 10, 15, hour=9),
            datetime(1997, 11,  2, hour=9),
            datetime(1997, 11, 15, hour=9),
            datetime(1997, 12,  2, hour=9),
            datetime(1997, 12, 15, hour=9),
            datetime(1998,  1,  2, hour=9),
            datetime(1998,  1, 15, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_month_days_2(self):
        """Monthly on the first and last days.

        RRULE:FREQ=MONTHLY;COUNT=10;BYMONTHDAY=1,-1
        DTSTART:19970930T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(1, -1),
                              count=10)
        start = datetime(1997, 9, 30, hour=9)
        expected = (
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10,  1, hour=9),
            datetime(1997, 10, 31, hour=9),
            datetime(1997, 11,  1, hour=9),
            datetime(1997, 11, 30, hour=9),
            datetime(1997, 12,  1, hour=9),
            datetime(1997, 12, 31, hour=9),
            datetime(1998,  1,  1, hour=9),
            datetime(1998,  1, 31, hour=9),
            datetime(1998,  2,  1, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_18_months_on_month_days(self):
        """Every 18 months from the 10th to the 15th.

        RRULE:FREQ=MONTHLY;INTERVAL=18;COUNT=10;BYMONTHDAY=10,11,12,13,14,15
        DTSTART:19970910T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              interval=18,
                              on_month_days=(10, 11, 12, 13, 14, 15),
                              count=10)
        start = datetime(1997, 9, 10, hour=9)
        expected = (
            datetime(1997, 9, 10, hour=9),
            datetime(1997, 9, 11, hour=9),
            datetime(1997, 9, 12, hour=9),
            datetime(1997, 9, 13, hour=9),
            datetime(1997, 9, 14, hour=9),
            datetime(1997, 9, 15, hour=9),
            datetime(1999, 3, 10, hour=9),
            datetime(1999, 3, 11, hour=9),
            datetime(1999, 3, 12, hour=9),
            datetime(1999, 3, 13, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_months_on_week_day(self):
        """Every other month on Tuesdays.

        RRULE:FREQ=MONTHLY;INTERVAL=2;BYDAY=TU;COUNT=18
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              interval=2,
                              on_week_days=(TUESDAY,),
                              count=18)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9,  9, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 23, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 11,  4, hour=9),
            datetime(1997, 11, 11, hour=9),
            datetime(1997, 11, 18, hour=9),
            datetime(1997, 11, 25, hour=9),
            datetime(1998,  1,  6, hour=9),
            datetime(1998,  1, 13, hour=9),
            datetime(1998,  1, 20, hour=9),
            datetime(1998,  1, 27, hour=9),
            datetime(1998,  3,  3, hour=9),
            datetime(1998,  3, 10, hour=9),
            datetime(1998,  3, 17, hour=9),
            datetime(1998,  3, 24, hour=9),
            datetime(1998,  3, 31, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_week_dayand_month_day(self):
        """Monthly on every Friday 13th.

        RRULE:FREQ=MONTHLY;BYDAY=FR;BYMONTHDAY=13;COUNT=5
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(13,),
                              on_week_days=(FRIDAY,),
                              count=5)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1998,  2, 13, hour=9),
            datetime(1998,  3, 13, hour=9),
            datetime(1998, 11, 13, hour=9),
            datetime(1999,  8, 13, hour=9),
            datetime(2000, 10, 13, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_week_day_and_month_days(self):
        """Monthly on the first Saturday following the first Sunday.

        RRULE:FREQ=MONTHLY;BYDAY=SA;BYMONTHDAY=7,8,9,10,11,12,13;COUNT=10
        DTSTART:19970913T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(7, 8, 9, 10, 11, 12, 13),
                              on_week_days=(SATURDAY,),
                              count=10)
        start = datetime(1997, 9, 13, hour=9)
        expected = (
            datetime(1997,  9, 13, hour=9),
            datetime(1997, 10, 11, hour=9),
            datetime(1997, 11,  8, hour=9),
            datetime(1997, 12, 13, hour=9),
            datetime(1998,  1, 10, hour=9),
            datetime(1998,  2,  7, hour=9),
            datetime(1998,  3,  7, hour=9),
            datetime(1998,  4, 11, hour=9),
            datetime(1998,  5,  9, hour=9),
            datetime(1998,  6, 13, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_week_days_and_set_pos_1(self):
        """Monthly on the 3rd Tuesday, Wednesday, or Thursday.

        RRULE:FREQ=MONTHLY;COUNT=3;BYDAY=TU,WE,TH;BYSETPOS=3
        DTSTART:19970904T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_week_days=(TUESDAY, WEDNESDAY, THURSDAY),
                              on_set_pos=(3,),
                              count=3)
        start = datetime(1997, 9, 4, hour=9)
        expected = (
            datetime(1997,  9, 4, hour=9),
            datetime(1997, 10, 7, hour=9),
            datetime(1997, 11, 6, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_week_days_and_set_pos_2(self):
        """Monthly on the second to last week day.

        RRULE:FREQ=MONTHLY;BYDAY=MO,TU,WE,TH,FR;BYSETPOS=-2;COUNT=7
        DTSTART:19970929T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_week_days=(
                                  MONDAY,
                                  TUESDAY,
                                  WEDNESDAY,
                                  THURSDAY,
                                  FRIDAY,
                              ),
                              on_set_pos=(-2,),
                              count=7)
        start = datetime(1997, 9, 29, hour=9)
        expected = (
            datetime(1997,  9, 29, hour=9),
            datetime(1997, 10, 30, hour=9),
            datetime(1997, 11, 27, hour=9),
            datetime(1997, 12, 30, hour=9),
            datetime(1998,  1, 29, hour=9),
            datetime(1998,  2, 26, hour=9),
            datetime(1998,  3, 30, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_month_days(self):
        """Monthly on the 15th and 30th.

        Example where an invalid date (30th of February) is ignored.

        RRULE:FREQ=MONTHLY;BYMONTHDAY=15,30;COUNT=5
        DTSTART:20070115T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(15, 30),
                              count=5,)
        start = datetime(2007, 1, 15, hour=9)
        expected = (
            datetime(2007, 1, 15, hour=9),
            datetime(2007, 1, 30, hour=9),
            datetime(2007, 2, 15, hour=9),
            datetime(2007, 3, 15, hour=9),
            datetime(2007, 3, 30, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly(self):
        """Monthly.

        Example where invalid dates (31th of some months) are ignored.

        RRULE:FREQ=MONTHLY;COUNT=12
        DTSTART:20070131T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              count=12)
        start = datetime(2007, 1, 31, hour=9)
        expected = (
            datetime(2007,  1, 31, hour=9),
            datetime(2007,  3, 31, hour=9),
            datetime(2007,  5, 31, hour=9),
            datetime(2007,  7, 31, hour=9),
            datetime(2007,  8, 31, hour=9),
            datetime(2007, 10, 31, hour=9),
            datetime(2007, 12, 31, hour=9),
            datetime(2008,  1, 31, hour=9),
            datetime(2008,  3, 31, hour=9),
            datetime(2008,  5, 31, hour=9),
            datetime(2008,  7, 31, hour=9),
            datetime(2008,  8, 31, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_weekly_1(self):
        """Weekly.

        RRULE:FREQ=WEEKLY;COUNT=10
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              count=10)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9,  9, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 23, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10,  7, hour=9),
            datetime(1997, 10, 14, hour=9),
            datetime(1997, 10, 21, hour=9),
            datetime(1997, 10, 28, hour=9),
            datetime(1997, 11,  4, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_weekly_2(self):
        """Weekly.

        RRULE:FREQ=WEEKLY;UNTIL=19971224T000000
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              until=datetime(1997, 12, 24))
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9,  9, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 23, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10,  7, hour=9),
            datetime(1997, 10, 14, hour=9),
            datetime(1997, 10, 21, hour=9),
            datetime(1997, 10, 28, hour=9),
            datetime(1997, 11,  4, hour=9),
            datetime(1997, 11, 11, hour=9),
            datetime(1997, 11, 18, hour=9),
            datetime(1997, 11, 25, hour=9),
            datetime(1997, 12,  2, hour=9),
            datetime(1997, 12,  9, hour=9),
            datetime(1997, 12, 16, hour=9),
            datetime(1997, 12, 23, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_weeks(self):
        """Every other week.

        With Sunday as the week start.

        RRULE:FREQ=WEEKLY;INTERVAL=2;WKST=SU;COUNT=13
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              interval=2,
                              week_start=SUNDAY,
                              count=13)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10, 14, hour=9),
            datetime(1997, 10, 28, hour=9),
            datetime(1997, 11, 11, hour=9),
            datetime(1997, 11, 25, hour=9),
            datetime(1997, 12,  9, hour=9),
            datetime(1997, 12, 23, hour=9),
            datetime(1998,  1,  6, hour=9),
            datetime(1998,  1, 20, hour=9),
            datetime(1998,  2,  3, hour=9),
            datetime(1998,  2, 17, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_weekly_on_week_days_1(self):
        """Weekly on Tuesday and Thursday.

        With Sunday as the week start.

        RRULE:FREQ=WEEKLY;UNTIL=19971007T000000;WKST=SU;BYDAY=TU,TH
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              week_start=SUNDAY,
                              on_week_days=(TUESDAY, THURSDAY),
                              until=datetime(1997, 10, 7))
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9,  4, hour=9),
            datetime(1997,  9,  9, hour=9),
            datetime(1997,  9, 11, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 18, hour=9),
            datetime(1997,  9, 23, hour=9),
            datetime(1997,  9, 25, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10,  2, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_weekly_on_week_days_2(self):
        """Weekly on Tuesday and Thursday.

        With Sunday as the week start.

        RRULE:FREQ=WEEKLY;COUNT=10;WKST=SU;BYDAY=TU,TH
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              week_start=SUNDAY,
                              on_week_days=(TUESDAY, THURSDAY),
                              count=10)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997, 9,  2, hour=9),
            datetime(1997, 9,  4, hour=9),
            datetime(1997, 9,  9, hour=9),
            datetime(1997, 9, 11, hour=9),
            datetime(1997, 9, 16, hour=9),
            datetime(1997, 9, 18, hour=9),
            datetime(1997, 9, 23, hour=9),
            datetime(1997, 9, 25, hour=9),
            datetime(1997, 9, 30, hour=9),
            datetime(1997, 10, 2, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_4_weeks_on_week_day(self):
        """Every 4 weeks on Sunday.

        RRULE:FREQ=WEEKLY;INTERVAL=4;BYDAY=SU;COUNT=4
        DTSTART:20150322T000000
        """
        rule = RecurrenceRule(WEEKLY,
                              interval=4,
                              on_week_days=(SUNDAY,),
                              count=4)
        start = datetime(2015, 3, 22)
        expected = (
            datetime(2015, 3, 22),
            datetime(2015, 4, 19),
            datetime(2015, 5, 17),
            datetime(2015, 6, 14),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_weeks_on_week_days_1(self):
        """Every other week on Monday, Wednesday, and Friday.

        With Sunday as the week start.

        RRULE:FREQ=WEEKLY;INTERVAL=2;UNTIL=19971224T000000;WKST=SU;BYDAY=MO,WE,FR
        DTSTART:19970901T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              interval=2,
                              week_start=SUNDAY,
                              on_week_days=(MONDAY, WEDNESDAY, FRIDAY),
                              until=datetime(1997, 12, 24),)
        start = datetime(1997, 9, 1, hour=9)
        expected = (
            datetime(1997,  9,  1, hour=9),
            datetime(1997,  9,  3, hour=9),
            datetime(1997,  9,  5, hour=9),
            datetime(1997,  9, 15, hour=9),
            datetime(1997,  9, 17, hour=9),
            datetime(1997,  9, 19, hour=9),
            datetime(1997,  9, 29, hour=9),
            datetime(1997, 10,  1, hour=9),
            datetime(1997, 10,  3, hour=9),
            datetime(1997, 10, 13, hour=9),
            datetime(1997, 10, 15, hour=9),
            datetime(1997, 10, 17, hour=9),
            datetime(1997, 10, 27, hour=9),
            datetime(1997, 10, 29, hour=9),
            datetime(1997, 10, 31, hour=9),
            datetime(1997, 11, 10, hour=9),
            datetime(1997, 11, 12, hour=9),
            datetime(1997, 11, 14, hour=9),
            datetime(1997, 11, 24, hour=9),
            datetime(1997, 11, 26, hour=9),
            datetime(1997, 11, 28, hour=9),
            datetime(1997, 12,  8, hour=9),
            datetime(1997, 12, 10, hour=9),
            datetime(1997, 12, 12, hour=9),
            datetime(1997, 12, 22, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_weeks_on_week_days_2(self):
        """Every other week on Tuesday and Thursday.

        With Sunday as the week start.

        RRULE:FREQ=WEEKLY;INTERVAL=2;COUNT=8;WKST=SU;BYDAY=TU,TH
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              interval=2,
                              week_start=SUNDAY,
                              on_week_days=(TUESDAY, THURSDAY),
                              count=8)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9,  4, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 18, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10,  2, hour=9),
            datetime(1997, 10, 14, hour=9),
            datetime(1997, 10, 16, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_weeks_on_week_days_3(self):
        """Every other week on Tuesday and Sunday.

        RRULE:FREQ=WEEKLY;INTERVAL=2;COUNT=4;BYDAY=TU,SU;WKST=MO
        DTSTART:19970805T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              interval=2,
                              on_week_days=(TUESDAY, SUNDAY),
                              count=4)
        start = datetime(1997, 8, 5, hour=9)
        expected = (
            datetime(1997, 8,  5, hour=9),
            datetime(1997, 8, 10, hour=9),
            datetime(1997, 8, 19, hour=9),
            datetime(1997, 8, 24, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_weeks_on_week_days_4(self):
        """Every other week on Tuesday and Sunday.

        With Sunday as the week start.

        RRULE:FREQ=WEEKLY;INTERVAL=2;COUNT=4;BYDAY=TU,SU;WKST=SU
        DTSTART:19970805T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              interval=2,
                              week_start=SUNDAY,
                              on_week_days=(TUESDAY, SUNDAY),
                              count=4)
        start = datetime(1997, 8, 5, hour=9)
        expected = (
            datetime(1997, 8,  5, hour=9),
            datetime(1997, 8, 17, hour=9),
            datetime(1997, 8, 19, hour=9),
            datetime(1997, 8, 31, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_daily_1(self):
        """Daily.

        RRULE:FREQ=DAILY;COUNT=10
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(DAILY,
                              count=10)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997, 9,  2, hour=9),
            datetime(1997, 9,  3, hour=9),
            datetime(1997, 9,  4, hour=9),
            datetime(1997, 9,  5, hour=9),
            datetime(1997, 9,  6, hour=9),
            datetime(1997, 9,  7, hour=9),
            datetime(1997, 9,  8, hour=9),
            datetime(1997, 9,  9, hour=9),
            datetime(1997, 9, 10, hour=9),
            datetime(1997, 9, 11, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_daily_2(self):
        """Daily.

        RRULE:FREQ=DAILY;UNTIL=19971224T000000
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(DAILY,
                              until=datetime(1997, 12, 24))
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9,  3, hour=9),
            datetime(1997,  9,  4, hour=9),
            datetime(1997,  9,  5, hour=9),
            datetime(1997,  9,  6, hour=9),
            datetime(1997,  9,  7, hour=9),
            datetime(1997,  9,  8, hour=9),
            datetime(1997,  9,  9, hour=9),
            datetime(1997,  9, 10, hour=9),
            datetime(1997,  9, 11, hour=9),
            datetime(1997,  9, 12, hour=9),
            datetime(1997,  9, 13, hour=9),
            datetime(1997,  9, 14, hour=9),
            datetime(1997,  9, 15, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 17, hour=9),
            datetime(1997,  9, 18, hour=9),
            datetime(1997,  9, 19, hour=9),
            datetime(1997,  9, 20, hour=9),
            datetime(1997,  9, 21, hour=9),
            datetime(1997,  9, 22, hour=9),
            datetime(1997,  9, 23, hour=9),
            datetime(1997,  9, 24, hour=9),
            datetime(1997,  9, 25, hour=9),
            datetime(1997,  9, 26, hour=9),
            datetime(1997,  9, 27, hour=9),
            datetime(1997,  9, 28, hour=9),
            datetime(1997,  9, 29, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10,  1, hour=9),
            datetime(1997, 10,  2, hour=9),
            datetime(1997, 10,  3, hour=9),
            datetime(1997, 10,  4, hour=9),
            datetime(1997, 10,  5, hour=9),
            datetime(1997, 10,  6, hour=9),
            datetime(1997, 10,  7, hour=9),
            datetime(1997, 10,  8, hour=9),
            datetime(1997, 10,  9, hour=9),
            datetime(1997, 10, 10, hour=9),
            datetime(1997, 10, 11, hour=9),
            datetime(1997, 10, 12, hour=9),
            datetime(1997, 10, 13, hour=9),
            datetime(1997, 10, 14, hour=9),
            datetime(1997, 10, 15, hour=9),
            datetime(1997, 10, 16, hour=9),
            datetime(1997, 10, 17, hour=9),
            datetime(1997, 10, 18, hour=9),
            datetime(1997, 10, 19, hour=9),
            datetime(1997, 10, 20, hour=9),
            datetime(1997, 10, 21, hour=9),
            datetime(1997, 10, 22, hour=9),
            datetime(1997, 10, 23, hour=9),
            datetime(1997, 10, 24, hour=9),
            datetime(1997, 10, 25, hour=9),
            datetime(1997, 10, 26, hour=9),
            datetime(1997, 10, 27, hour=9),
            datetime(1997, 10, 28, hour=9),
            datetime(1997, 10, 29, hour=9),
            datetime(1997, 10, 30, hour=9),
            datetime(1997, 10, 31, hour=9),
            datetime(1997, 11,  1, hour=9),
            datetime(1997, 11,  2, hour=9),
            datetime(1997, 11,  3, hour=9),
            datetime(1997, 11,  4, hour=9),
            datetime(1997, 11,  5, hour=9),
            datetime(1997, 11,  6, hour=9),
            datetime(1997, 11,  7, hour=9),
            datetime(1997, 11,  8, hour=9),
            datetime(1997, 11,  9, hour=9),
            datetime(1997, 11, 10, hour=9),
            datetime(1997, 11, 11, hour=9),
            datetime(1997, 11, 12, hour=9),
            datetime(1997, 11, 13, hour=9),
            datetime(1997, 11, 14, hour=9),
            datetime(1997, 11, 15, hour=9),
            datetime(1997, 11, 16, hour=9),
            datetime(1997, 11, 17, hour=9),
            datetime(1997, 11, 18, hour=9),
            datetime(1997, 11, 19, hour=9),
            datetime(1997, 11, 20, hour=9),
            datetime(1997, 11, 21, hour=9),
            datetime(1997, 11, 22, hour=9),
            datetime(1997, 11, 23, hour=9),
            datetime(1997, 11, 24, hour=9),
            datetime(1997, 11, 25, hour=9),
            datetime(1997, 11, 26, hour=9),
            datetime(1997, 11, 27, hour=9),
            datetime(1997, 11, 28, hour=9),
            datetime(1997, 11, 29, hour=9),
            datetime(1997, 11, 30, hour=9),
            datetime(1997, 12,  1, hour=9),
            datetime(1997, 12,  2, hour=9),
            datetime(1997, 12,  3, hour=9),
            datetime(1997, 12,  4, hour=9),
            datetime(1997, 12,  5, hour=9),
            datetime(1997, 12,  6, hour=9),
            datetime(1997, 12,  7, hour=9),
            datetime(1997, 12,  8, hour=9),
            datetime(1997, 12,  9, hour=9),
            datetime(1997, 12, 10, hour=9),
            datetime(1997, 12, 11, hour=9),
            datetime(1997, 12, 12, hour=9),
            datetime(1997, 12, 13, hour=9),
            datetime(1997, 12, 14, hour=9),
            datetime(1997, 12, 15, hour=9),
            datetime(1997, 12, 16, hour=9),
            datetime(1997, 12, 17, hour=9),
            datetime(1997, 12, 18, hour=9),
            datetime(1997, 12, 19, hour=9),
            datetime(1997, 12, 20, hour=9),
            datetime(1997, 12, 21, hour=9),
            datetime(1997, 12, 22, hour=9),
            datetime(1997, 12, 23, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_days(self):
        """Every other day.

        RRULE:FREQ=DAILY;INTERVAL=2;COUNT=20
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(DAILY,
                              interval=2,
                              count=20)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9,  4, hour=9),
            datetime(1997,  9,  6, hour=9),
            datetime(1997,  9,  8, hour=9),
            datetime(1997,  9, 10, hour=9),
            datetime(1997,  9, 12, hour=9),
            datetime(1997,  9, 14, hour=9),
            datetime(1997,  9, 16, hour=9),
            datetime(1997,  9, 18, hour=9),
            datetime(1997,  9, 20, hour=9),
            datetime(1997,  9, 22, hour=9),
            datetime(1997,  9, 24, hour=9),
            datetime(1997,  9, 26, hour=9),
            datetime(1997,  9, 28, hour=9),
            datetime(1997,  9, 30, hour=9),
            datetime(1997, 10,  2, hour=9),
            datetime(1997, 10,  4, hour=9),
            datetime(1997, 10,  6, hour=9),
            datetime(1997, 10,  8, hour=9),
            datetime(1997, 10, 10, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_10_days(self):
        """Every 10 days.

        RRULE:FREQ=DAILY;INTERVAL=10;COUNT=5
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(DAILY,
                              interval=10,
                              count=5)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997,  9,  2, hour=9),
            datetime(1997,  9, 12, hour=9),
            datetime(1997,  9, 22, hour=9),
            datetime(1997, 10,  2, hour=9),
            datetime(1997, 10, 12, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_daily_on_month(self):
        """Daily in January.

        RRULE:FREQ=DAILY;UNTIL=20000131T140000;BYMONTH=1
        DTSTART:19980101T090000
        """
        rule = RecurrenceRule(DAILY,
                              on_months=(JANUARY,),
                              until=datetime(2000, 1, 31, hour=14))
        start = datetime(1998, 1, 1, hour=9)
        expected = (
            datetime(1998, 1,  1, hour=9),
            datetime(1998, 1,  2, hour=9),
            datetime(1998, 1,  3, hour=9),
            datetime(1998, 1,  4, hour=9),
            datetime(1998, 1,  5, hour=9),
            datetime(1998, 1,  6, hour=9),
            datetime(1998, 1,  7, hour=9),
            datetime(1998, 1,  8, hour=9),
            datetime(1998, 1,  9, hour=9),
            datetime(1998, 1, 10, hour=9),
            datetime(1998, 1, 11, hour=9),
            datetime(1998, 1, 12, hour=9),
            datetime(1998, 1, 13, hour=9),
            datetime(1998, 1, 14, hour=9),
            datetime(1998, 1, 15, hour=9),
            datetime(1998, 1, 16, hour=9),
            datetime(1998, 1, 17, hour=9),
            datetime(1998, 1, 18, hour=9),
            datetime(1998, 1, 19, hour=9),
            datetime(1998, 1, 20, hour=9),
            datetime(1998, 1, 21, hour=9),
            datetime(1998, 1, 22, hour=9),
            datetime(1998, 1, 23, hour=9),
            datetime(1998, 1, 24, hour=9),
            datetime(1998, 1, 25, hour=9),
            datetime(1998, 1, 26, hour=9),
            datetime(1998, 1, 27, hour=9),
            datetime(1998, 1, 28, hour=9),
            datetime(1998, 1, 29, hour=9),
            datetime(1998, 1, 30, hour=9),
            datetime(1998, 1, 31, hour=9),
            datetime(1999, 1,  1, hour=9),
            datetime(1999, 1,  2, hour=9),
            datetime(1999, 1,  3, hour=9),
            datetime(1999, 1,  4, hour=9),
            datetime(1999, 1,  5, hour=9),
            datetime(1999, 1,  6, hour=9),
            datetime(1999, 1,  7, hour=9),
            datetime(1999, 1,  8, hour=9),
            datetime(1999, 1,  9, hour=9),
            datetime(1999, 1, 10, hour=9),
            datetime(1999, 1, 11, hour=9),
            datetime(1999, 1, 12, hour=9),
            datetime(1999, 1, 13, hour=9),
            datetime(1999, 1, 14, hour=9),
            datetime(1999, 1, 15, hour=9),
            datetime(1999, 1, 16, hour=9),
            datetime(1999, 1, 17, hour=9),
            datetime(1999, 1, 18, hour=9),
            datetime(1999, 1, 19, hour=9),
            datetime(1999, 1, 20, hour=9),
            datetime(1999, 1, 21, hour=9),
            datetime(1999, 1, 22, hour=9),
            datetime(1999, 1, 23, hour=9),
            datetime(1999, 1, 24, hour=9),
            datetime(1999, 1, 25, hour=9),
            datetime(1999, 1, 26, hour=9),
            datetime(1999, 1, 27, hour=9),
            datetime(1999, 1, 28, hour=9),
            datetime(1999, 1, 29, hour=9),
            datetime(1999, 1, 30, hour=9),
            datetime(1999, 1, 31, hour=9),
            datetime(2000, 1,  1, hour=9),
            datetime(2000, 1,  2, hour=9),
            datetime(2000, 1,  3, hour=9),
            datetime(2000, 1,  4, hour=9),
            datetime(2000, 1,  5, hour=9),
            datetime(2000, 1,  6, hour=9),
            datetime(2000, 1,  7, hour=9),
            datetime(2000, 1,  8, hour=9),
            datetime(2000, 1,  9, hour=9),
            datetime(2000, 1, 10, hour=9),
            datetime(2000, 1, 11, hour=9),
            datetime(2000, 1, 12, hour=9),
            datetime(2000, 1, 13, hour=9),
            datetime(2000, 1, 14, hour=9),
            datetime(2000, 1, 15, hour=9),
            datetime(2000, 1, 16, hour=9),
            datetime(2000, 1, 17, hour=9),
            datetime(2000, 1, 18, hour=9),
            datetime(2000, 1, 19, hour=9),
            datetime(2000, 1, 20, hour=9),
            datetime(2000, 1, 21, hour=9),
            datetime(2000, 1, 22, hour=9),
            datetime(2000, 1, 23, hour=9),
            datetime(2000, 1, 24, hour=9),
            datetime(2000, 1, 25, hour=9),
            datetime(2000, 1, 26, hour=9),
            datetime(2000, 1, 27, hour=9),
            datetime(2000, 1, 28, hour=9),
            datetime(2000, 1, 29, hour=9),
            datetime(2000, 1, 30, hour=9),
            datetime(2000, 1, 31, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_daily_on_hours_and_minutes(self):
        """Daily every 20 minutes from 9:00 a.m. to 4:40 p.m.

        RRULE:FREQ=DAILY;BYHOUR=9,10,11,12,13,14,15,16;BYMINUTE=0,20,40;COUNT=48
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(DAILY,
                              on_hours=(9, 10, 11, 12, 13, 14, 15, 16),
                              on_minutes=(0, 20, 40),
                              count=48)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997, 9, 2, hour= 9, minute= 0),
            datetime(1997, 9, 2, hour= 9, minute=20),
            datetime(1997, 9, 2, hour= 9, minute=40),
            datetime(1997, 9, 2, hour=10, minute= 0),
            datetime(1997, 9, 2, hour=10, minute=20),
            datetime(1997, 9, 2, hour=10, minute=40),
            datetime(1997, 9, 2, hour=11, minute= 0),
            datetime(1997, 9, 2, hour=11, minute=20),
            datetime(1997, 9, 2, hour=11, minute=40),
            datetime(1997, 9, 2, hour=12, minute= 0),
            datetime(1997, 9, 2, hour=12, minute=20),
            datetime(1997, 9, 2, hour=12, minute=40),
            datetime(1997, 9, 2, hour=13, minute= 0),
            datetime(1997, 9, 2, hour=13, minute=20),
            datetime(1997, 9, 2, hour=13, minute=40),
            datetime(1997, 9, 2, hour=14, minute= 0),
            datetime(1997, 9, 2, hour=14, minute=20),
            datetime(1997, 9, 2, hour=14, minute=40),
            datetime(1997, 9, 2, hour=15, minute= 0),
            datetime(1997, 9, 2, hour=15, minute=20),
            datetime(1997, 9, 2, hour=15, minute=40),
            datetime(1997, 9, 2, hour=16, minute= 0),
            datetime(1997, 9, 2, hour=16, minute=20),
            datetime(1997, 9, 2, hour=16, minute=40),
            datetime(1997, 9, 3, hour= 9, minute= 0),
            datetime(1997, 9, 3, hour= 9, minute=20),
            datetime(1997, 9, 3, hour= 9, minute=40),
            datetime(1997, 9, 3, hour=10, minute= 0),
            datetime(1997, 9, 3, hour=10, minute=20),
            datetime(1997, 9, 3, hour=10, minute=40),
            datetime(1997, 9, 3, hour=11, minute= 0),
            datetime(1997, 9, 3, hour=11, minute=20),
            datetime(1997, 9, 3, hour=11, minute=40),
            datetime(1997, 9, 3, hour=12, minute= 0),
            datetime(1997, 9, 3, hour=12, minute=20),
            datetime(1997, 9, 3, hour=12, minute=40),
            datetime(1997, 9, 3, hour=13, minute= 0),
            datetime(1997, 9, 3, hour=13, minute=20),
            datetime(1997, 9, 3, hour=13, minute=40),
            datetime(1997, 9, 3, hour=14, minute= 0),
            datetime(1997, 9, 3, hour=14, minute=20),
            datetime(1997, 9, 3, hour=14, minute=40),
            datetime(1997, 9, 3, hour=15, minute= 0),
            datetime(1997, 9, 3, hour=15, minute=20),
            datetime(1997, 9, 3, hour=15, minute=40),
            datetime(1997, 9, 3, hour=16, minute= 0),
            datetime(1997, 9, 3, hour=16, minute=20),
            datetime(1997, 9, 3, hour=16, minute=40),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_3_hours(self):
        """Every 3 hours from 9:00 a.m. to 5:00 p.m.

        RRULE:FREQ=HOURLY;INTERVAL=3;UNTIL=19970902T170000
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(HOURLY,
                              interval=3,
                              until=datetime(1997, 9, 2, hour=17))
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997, 9, 2, hour= 9),
            datetime(1997, 9, 2, hour=12),
            datetime(1997, 9, 2, hour=15),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_15_minutes(self):
        """Every 15 minutes.

        RRULE:FREQ=MINUTELY;INTERVAL=15;COUNT=6
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(MINUTELY,
                              interval=15,
                              count=6)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997, 9, 2, hour= 9, minute= 0),
            datetime(1997, 9, 2, hour= 9, minute=15),
            datetime(1997, 9, 2, hour= 9, minute=30),
            datetime(1997, 9, 2, hour= 9, minute=45),
            datetime(1997, 9, 2, hour=10, minute= 0),
            datetime(1997, 9, 2, hour=10, minute=15),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_90_minutes(self):
        """Every 90 minutes.

        RRULE:FREQ=MINUTELY;INTERVAL=90;COUNT=4
        DTSTART:19970902T090000
        """
        rule = RecurrenceRule(MINUTELY,
                              interval=90,
                              count=4)
        start = datetime(1997, 9, 2, hour=9)
        expected = (
            datetime(1997, 9, 2, hour= 9, minute= 0),
            datetime(1997, 9, 2, hour=10, minute=30),
            datetime(1997, 9, 2, hour=12, minute= 0),
            datetime(1997, 9, 2, hour=13, minute=30),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_weekly_on_week_days_3(self):
        """Weekly on Thursday and Sunday.

        RRULE:FREQ=WEEKLY;COUNT=35;BYDAY=SU,TH
        DTSTART:20111120T100000
        """
        rule = RecurrenceRule(WEEKLY,
                              on_week_days=(THURSDAY, SUNDAY),
                              count=35)
        start = datetime(2011, 11, 20, hour=10)
        expected = (
            datetime(2011, 11, 20, hour=10),
            datetime(2011, 11, 24, hour=10),
            datetime(2011, 11, 27, hour=10),
            datetime(2011, 12,  1, hour=10),
            datetime(2011, 12,  4, hour=10),
            datetime(2011, 12,  8, hour=10),
            datetime(2011, 12, 11, hour=10),
            datetime(2011, 12, 15, hour=10),
            datetime(2011, 12, 18, hour=10),
            datetime(2011, 12, 22, hour=10),
            datetime(2011, 12, 25, hour=10),
            datetime(2011, 12, 29, hour=10),
            datetime(2012,  1,  1, hour=10),
            datetime(2012,  1,  5, hour=10),
            datetime(2012,  1,  8, hour=10),
            datetime(2012,  1, 12, hour=10),
            datetime(2012,  1, 15, hour=10),
            datetime(2012,  1, 19, hour=10),
            datetime(2012,  1, 22, hour=10),
            datetime(2012,  1, 26, hour=10),
            datetime(2012,  1, 29, hour=10),
            datetime(2012,  2,  2, hour=10),
            datetime(2012,  2,  5, hour=10),
            datetime(2012,  2,  9, hour=10),
            datetime(2012,  2, 12, hour=10),
            datetime(2012,  2, 16, hour=10),
            datetime(2012,  2, 19, hour=10),
            datetime(2012,  2, 23, hour=10),
            datetime(2012,  2, 26, hour=10),
            datetime(2012,  3,  1, hour=10),
            datetime(2012,  3,  4, hour=10),
            datetime(2012,  3,  8, hour=10),
            datetime(2012,  3, 11, hour=10),
            datetime(2012,  3, 15, hour=10),
            datetime(2012,  3, 18, hour=10),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_daily_on_months(self):
        """Daily on unordered months.

        RRULE:FREQ=DAILY;UNTIL=20141206T000000;BYMONTH=11,12,1,2,3,4,10
        DTSTART:20141030T000000
        """
        rule = RecurrenceRule(DAILY,
                              on_months=(
                                  NOVEMBER,
                                  DECEMBER,
                                  JANUARY,
                                  FEBRUARY,
                                  MARCH,
                                  APRIL,
                                  OCTOBER,
                              ),
                              until=datetime(2014, 12, 6))
        start = datetime(2014, 10, 30)
        expected = (
            datetime(2014, 10, 30),
            datetime(2014, 10, 31),
            datetime(2014, 11,  1),
            datetime(2014, 11,  2),
            datetime(2014, 11,  3),
            datetime(2014, 11,  4),
            datetime(2014, 11,  5),
            datetime(2014, 11,  6),
            datetime(2014, 11,  7),
            datetime(2014, 11,  8),
            datetime(2014, 11,  9),
            datetime(2014, 11, 10),
            datetime(2014, 11, 11),
            datetime(2014, 11, 12),
            datetime(2014, 11, 13),
            datetime(2014, 11, 14),
            datetime(2014, 11, 15),
            datetime(2014, 11, 16),
            datetime(2014, 11, 17),
            datetime(2014, 11, 18),
            datetime(2014, 11, 19),
            datetime(2014, 11, 20),
            datetime(2014, 11, 21),
            datetime(2014, 11, 22),
            datetime(2014, 11, 23),
            datetime(2014, 11, 24),
            datetime(2014, 11, 25),
            datetime(2014, 11, 26),
            datetime(2014, 11, 27),
            datetime(2014, 11, 28),
            datetime(2014, 11, 29),
            datetime(2014, 11, 30),
            datetime(2014, 12,  1),
            datetime(2014, 12,  2),
            datetime(2014, 12,  3),
            datetime(2014, 12,  4),
            datetime(2014, 12,  5),
            datetime(2014, 12,  6),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_weeks(self):
        """Yearly on first 2 weeks.

        RRULE:FREQ=YEARLY;BYWEEKNO=1,2;UNTIL=20170101T000000
        DTSTART:20130101T000000
        """
        rule = RecurrenceRule(YEARLY,
                              on_weeks=(1, 2),
                              until=datetime(2017, 1, 1))
        start = datetime(2013, 1, 1)
        expected = (
            datetime(2013,  1,  1),
            datetime(2013,  1,  8),
            datetime(2013, 12, 31),
            datetime(2014,  1,  7),
            datetime(2014, 12, 30),
            datetime(2015,  1,  6),
            datetime(2016,  1,  5),
            datetime(2016,  1, 12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_weeks_and_set_pos(self):
        """Yearly on first 2 weeks.

        RRULE:FREQ=YEARLY;BYWEEKNO=1,2;BYSETPOS=1;UNTIL=20170101T000000
        DTSTART:20130101T000000
        """
        rule = RecurrenceRule(YEARLY,
                              on_weeks=(1, 2),
                              on_set_pos=(1,),
                              until=datetime(2017, 1, 1))
        start = datetime(2013, 1, 1)
        expected = (
            datetime(2013,  1,  1),
            datetime(2013, 12, 31),
            datetime(2014, 12, 30),
            datetime(2016,  1,  5),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_leap_year_day_1(self):
        """Yearly on last day of leap year.

        RRULE:FREQ=YEARLY;BYYEARDAY=366;UNTIL=20200101T000000
        DTSTART:20121231T120000
        """
        rule = RecurrenceRule(YEARLY,
                              on_year_days=(366,),
                              until=datetime(2020, 1, 1))
        start = datetime(2012, 12, 31, hour=12)
        expected = (
            datetime(2012, 12, 31, hour=12),
            datetime(2016, 12, 31, hour=12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_nth_week_day_and_month_1(self):
        """Yearly on the last Friday of October.

        RRULE:FREQ=YEARLY;BYDAY=-1FR;BYMONTH=10;UNTIL=20150101T000000
        DTSTART:20101029T120000
        """
        rule = RecurrenceRule(YEARLY,
                              on_months=(OCTOBER,),
                              on_week_days=(FRIDAY(-1),),
                              until=datetime(2015, 1, 1))
        start = datetime(2010, 10, 29, hour=12)
        expected = (
            datetime(2010, 10, 29, hour=12),
            datetime(2011, 10, 28, hour=12),
            datetime(2012, 10, 26, hour=12),
            datetime(2013, 10, 25, hour=12),
            datetime(2014, 10, 31, hour=12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_nth_week_day_and_month_2(self):
        """Yearly on the first Friday of April.

        RRULE:FREQ=YEARLY;BYDAY=1FR;BYMONTH=4;UNTIL=20150101T000000
        DTSTART:20100402T120000
        """
        rule = RecurrenceRule(YEARLY,
                              on_months=(APRIL,),
                              on_week_days=(FRIDAY(1),),
                              until=datetime(2015, 1, 1))
        start = datetime(2010, 4, 2, hour=12)
        expected = (
            datetime(2010, 4, 2, hour=12),
            datetime(2011, 4, 1, hour=12),
            datetime(2012, 4, 6, hour=12),
            datetime(2013, 4, 5, hour=12),
            datetime(2014, 4, 4, hour=12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_month_day_2(self):
        """Monthly on the 31st.

        RRULE:FREQ=MONTHLY;BYMONTHDAY=31;COUNT=12
        DTSTART:20150131T000000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(31,),
                              count=12)
        start = datetime(2015, 1, 31)
        expected = (
            datetime(2015,  1, 31),
            datetime(2015,  3, 31),
            datetime(2015,  5, 31),
            datetime(2015,  7, 31),
            datetime(2015,  8, 31),
            datetime(2015, 10, 31),
            datetime(2015, 12, 31),
            datetime(2016,  1, 31),
            datetime(2016,  3, 31),
            datetime(2016,  5, 31),
            datetime(2016,  7, 31),
            datetime(2016,  8, 31),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_month_day_3(self):
        """Monthly on the 31st from the end.

        RRULE:FREQ=MONTHLY;BYMONTHDAY=-31;COUNT=12
        DTSTART:20150101T000000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_month_days=(-31,),
                              count=12)
        start = datetime(2015, 1, 1)
        expected = (
            datetime(2015,  1, 1),
            datetime(2015,  3, 1),
            datetime(2015,  5, 1),
            datetime(2015,  7, 1),
            datetime(2015,  8, 1),
            datetime(2015, 10, 1),
            datetime(2015, 12, 1),
            datetime(2016,  1, 1),
            datetime(2016,  3, 1),
            datetime(2016,  5, 1),
            datetime(2016,  7, 1),
            datetime(2016,  8, 1),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_leap_year_day_2(self):
        """Yearly on the 366th.

        RRULE:FREQ=YEARLY;BYYEARDAY=366;COUNT=3
        DTSTART:20121231T120000
        """
        rule = RecurrenceRule(YEARLY,
                              on_year_days=(366,),
                              count=3)
        start = datetime(2012, 12, 31, hour=12)
        expected = (
            datetime(2012, 12, 31, hour=12),
            datetime(2016, 12, 31, hour=12),
            datetime(2020, 12, 31, hour=12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_yearly_on_leap_year_day_3(self):
        """Yearly on the 366th from the end.

        RRULE:FREQ=YEARLY;BYYEARDAY=-366;COUNT=3
        DTSTART:20120101T120000
        """
        rule = RecurrenceRule(YEARLY,
                              on_year_days=(-366,),
                              count=3)
        start = datetime(2012, 1, 1, hour=12)
        expected = (
            datetime(2012, 1, 1, hour=12),
            datetime(2016, 1, 1, hour=12),
            datetime(2020, 1, 1, hour=12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_13_months_on_month(self):
        """Every 13 months in May.

        RRULE:FREQ=MONTHLY;INTERVAL=13;BYMONTH=5;COUNT=3
        DTSTART:20100212T000000
        """
        rule = RecurrenceRule(MONTHLY,
                              interval=13,
                              on_months=(MAY,),
                              count=3)
        start = datetime(2010, 2, 12)
        expected = (
            datetime(2013, 5, 12),
            datetime(2026, 5, 12),
            datetime(2039, 5, 12),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_every_2_weeks_on_week_days_5(self):
        """Every other week on Wednesday and Friday.

        RRULE:FREQ=WEEKLY;BYDAY=WE,FR;INTERVAL=2;COUNT=4
        DTSTART:20190101T100000
        """
        rule = RecurrenceRule(WEEKLY,
                              interval=2,
                              on_week_days=(WEDNESDAY, FRIDAY),
                              count=4)
        start = datetime(2019, 1, 1, hour=10)
        expected = (
            datetime(2019, 1,  2, hour=10),
            datetime(2019, 1,  4, hour=10),
            datetime(2019, 1, 16, hour=10),
            datetime(2019, 1, 18, hour=10)
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_weekly_on_month(self):
        """Weekly in February.

        RRULE:FREQ=WEEKLY;UNTIL=19870101T000000;BYMONTH=2
        DTSTART:19850101T090000
        """
        rule = RecurrenceRule(WEEKLY,
                              on_months=(FEBRUARY,),
                              until=datetime(1987, 1, 1))
        start = datetime(1985, 1, 1, hour=9)
        expected = (
            datetime(1985, 2,  5, hour=9),
            datetime(1985, 2, 12, hour=9),
            datetime(1985, 2, 19, hour=9),
            datetime(1985, 2, 26, hour=9),
            datetime(1986, 2,  4, hour=9),
            datetime(1986, 2, 11, hour=9),
            datetime(1986, 2, 18, hour=9),
            datetime(1986, 2, 25, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_monthly_on_month(self):
        """Monthly in February.

        RRULE:FREQ=MONTHLY;UNTIL=19870101T000000;BYMONTH=2
        DTSTART:19850101T090000
        """
        rule = RecurrenceRule(MONTHLY,
                              on_months=(FEBRUARY,),
                              until=datetime(1987, 1, 1))
        start = datetime(1985, 1, 1, hour=9)
        expected = (
            datetime(1985, 2, 1, hour=9),
            datetime(1986, 2, 1, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)

    def test_daily_on_week(self):
        """Daily.

        RRULE:FREQ=DAILY;UNTIL=19870101T000000;BYWEEKNO=1
        DTSTART:19850101T090000
        """
        rule = RecurrenceRule(DAILY,
                              on_weeks=(1,),
                              until=datetime(1987, 1, 1))
        start = datetime(1985, 1, 1, hour=9)
        expected = (
            datetime(1985,  1,  1, hour=9),
            datetime(1985,  1,  2, hour=9),
            datetime(1985,  1,  3, hour=9),
            datetime(1985,  1,  4, hour=9),
            datetime(1985,  1,  5, hour=9),
            datetime(1985,  1,  6, hour=9),
            datetime(1985, 12, 30, hour=9),
            datetime(1985, 12, 31, hour=9),
            datetime(1986,  1,  1, hour=9),
            datetime(1986,  1,  2, hour=9),
            datetime(1986,  1,  3, hour=9),
            datetime(1986,  1,  4, hour=9),
            datetime(1986,  1,  5, hour=9),
            datetime(1986, 12, 29, hour=9),
            datetime(1986, 12, 30, hour=9),
            datetime(1986, 12, 31, hour=9),
        )
        self.assertEqual(tuple(rule.iterate_from(start)), expected)


if __name__ == '__main__':
    unittest_main()
