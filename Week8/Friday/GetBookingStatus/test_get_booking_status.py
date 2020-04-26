import unittest
from unittest.mock import Mock, patch
from get_booking_status import *

booking = Mock()


class TestGetBookingStatus(unittest.TestCase):
    def setUp(self):
        booking.cancelled = False
        booking.is_fully_paid.return_value = False

    def test_if_booking_cancelled(self):
        booking.cancelled = True
        result = get_booking_status(booking)

        self.assertEqual('Cancelled', result)

    def test_if_booking_is_fully_paid(self):
        booking.is_fully_paid.return_value = True

        result = get_booking_status(booking)

        self.assertEqual('Paid', result)

    @patch('get_booking_status.datetime')
    def test_if_booking_still_didnt_started(self, datetime_mock):
        booking.start = datetime(2020, 4, 27)
        datetime_mock.now.return_value = datetime(2020, 4, 26)

        result = get_booking_status(booking)

        self.assertEqual('Upcoming', result)

    @patch('get_booking_status.datetime')
    def test_if_all_ifs_are_false(self, datetime_mock):
        booking.start = datetime(2020, 4, 27)
        datetime_mock.now.return_value = datetime(2020, 5, 1)

        result = get_booking_status(booking)

        self.assertEqual(result, 'Waiting taxes')


if __name__ == '__main__':
    unittest.main()
