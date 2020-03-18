import unittest
from cash_desk import Bill, BillBatch, CashDesk


class TestBill(unittest.TestCase):
    def test_constructor_of_the_class_with_negative_value_should_raise_value_error(self):
        exc = None

        try:
            Bill(-2)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_constructor_of_the_class_with_value_different_than_integer_should_raise_type_error(self):
        exc = None

        try:
            Bill(2.2)
        except TypeError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_dunder_int_should_return_the_amount(self):
        bill = Bill(2)

        self.assertEqual(int(bill), 2)

    def test_dunder_str_should_return_string(self):
        bill = Bill(10)

        self.assertEqual(str(bill), 'A 10$ bill')

    def test_dunder_repr_should_return_string(self):
        bill = Bill(5)

        self.assertEqual(repr(bill), 'A 5$ bill')

    def test_dunder_eq_should_return_boolean(self):
        bill1 = Bill(5)
        bill2 = Bill(5)
        bill3 = Bill(10)

        self.assertTrue(bill1 == bill2)
        self.assertFalse(bill1 == bill3)

    def test_dunder_lt(self):

    	self.assertTrue(Bill(5) < Bill(10))


class TestBillBatch(unittest.TestCase):
    def test_constructor_if_given_list_is_not_from_Bills(self):
        lst = [Bill(2), 2]
        exc = None

        try:
            BillBatch(lst)
        except TypeError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_dunder_len_should_return_length_of_the_list(self):
        lst = [Bill(2), Bill(3)]
        batch = BillBatch(lst)

        result = len(batch)

        self.assertTrue(result == 2)

    

class TestCashDesk(unittest.TestCase):
    def test_take_money_with_element_different_than_batch_and_bill(self):
        exc = None
        a = CashDesk()

        try:
            a.take_money(3)
        except TypeError as err:
            exc = err

        self.assertIsNotNone(exc)



if __name__ == '__main__':
    unittest.main()
