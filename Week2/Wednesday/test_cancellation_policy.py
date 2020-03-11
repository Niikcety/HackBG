import unittest
from cancellation_policy import validate_conditions, ensure_conditions, group_conditions


class TestValidateConditions(unittest.TestCase):
    def test_validation_passes_with_valid_conditions(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 100}
        ]

        validate_conditions(conditions)

    def test_raises_exception_if_all_conditions_have_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_more_than_one_condition_with_no_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10000},
            {'percent': 10},
            {'percent': 100}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_hours_bigger_than_24(self):
        # ARRANGE
        conditions = [
            {'hours': 72, 'percent': 10000},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Hours cannot be > 24.')


class TestEnsureConditions(unittest.TestCase):
	def test_passes_with_valid_conditions(self):
		given = [
		  {'hours': 24, 'percent': 10 },
		  {'hours': 12, 'percent': 50 },
		  {'hours': 6, 'percent': 80 },
		  {'percent': 100 }
		]
		wanted = [
		  {'hours': 24, 'percent': 10 },
		  {'hours': 12, 'percent': 50 },
		  {'hours': 6, 'percent': 80 },
		  {'hours': 0,'percent': 100 }
		] 

		self.assertEqual(ensure_conditions(given), wanted)

class TestGroupConditions(unittest.TestCase):
	def test_passes_with_ordered_conditions(self):
		given = [
		  {'hours': 24, 'percent': 10 },
		  {'hours': 12, 'percent': 50 },
		  {'hours': 6, 'percent': 80 },
		  {'hours':0,'percent': 100 }
		]
		wanted = [
			(24,12),
			(12,6),
			(6,0)
		]

		self.assertEqual(group_conditions(given),wanted)

	def test_passes_with_unordered_conditions(self):
		given = [
			{'hours':0,'percent': 100 },
			{'hours': 12, 'percent': 50 },
			{'hours': 6, 'percent': 80 },
			{'hours': 24, 'percent': 10 }
		]
		wanted = [
			(24,12),
			(12,6),
			(6,0)
		]

		self.assertEqual(group_conditions(given),wanted)

if __name__ == '__main__':
    unittest.main()