import unittest
import pytz
from datetime import datetime

from weather.simulator.utils.timezone import TimeZone


class TimeZoneTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_current_local_time_for_sydney(self):
        au_tz = pytz.timezone('Australia/Sydney')
        observed_time = TimeZone.current_local_time('Sydney')
        expected_time = datetime.now(tz=au_tz).isoformat(timespec='seconds')
        self.assertEqual(expected_time, observed_time, 'Sydney Time mismatch.. Check, if not run in the same second')

    def test_current_local_time_for_london(self):
        uk_tz = pytz.timezone('Europe/London')
        observed_time = TimeZone.current_local_time('London')
        expected_time = datetime.now(tz=uk_tz).isoformat(timespec='seconds')
        self.assertEqual(expected_time, observed_time, 'London Time mismatch..  Check, if not run in the same second')

    def test_current_local_time_for_UTC(self):
        utc_tz = pytz.timezone('UTC')
        observed_time = TimeZone.current_local_time('UTC')
        expected_time = datetime.now(tz=utc_tz).isoformat(timespec='seconds')
        self.assertEqual(expected_time, observed_time, 'UTC Time mismatch.. .. Check, if not run in the same second')

    def test_current_local_time_for_petersburg(self):
        ptr_tz = pytz.timezone('America/Indiana/Petersburg')
        observed_time = TimeZone.current_local_time('Petersburg')
        expected_time = datetime.now(tz=ptr_tz).isoformat(timespec='seconds')
        self.assertEqual(expected_time, observed_time, 'Petersburg Time mismatch. Check, if not run in the same second')

    def test_current_local_time_for_bangalore(self):
        ptr_tz = pytz.timezone('UTC')
        observed_time = TimeZone.current_local_time('Bangalore')  # Bangalore time isn't in the standard timezones
        expected_time = datetime.now(tz=ptr_tz).isoformat(timespec='seconds')
        self.assertEqual(expected_time, observed_time, 'Bangalore Time mismatch. Check, if not run in the same second')

    def tearDown(self):
        pass
