import unittest
from utils import from_string_to_list_of_terms, get_coeficient, validate_term, get_pow

class TestFromStringToListOfTerms(unittest.TestCase):
    def test_if_there_is_forbidden_sign_should_raise_error(self):
        
        input1 = '2x^3 - 3x + 1'
        input2 = '2y^3 + 3'
        input3 = '2x*5 / 14'
        exc1 = None
        exc2 = None
        exc3 = None

        try:
            from_string_to_list_of_terms(input1)
        except TypeError as err:
            exc1 = err

        try:
            from_string_to_list_of_terms(input2)
        except TypeError as err:
            exc2 = err

        try:
            from_string_to_list_of_terms(input3)
        except TypeError as err:
            exc3 = err

        self.assertIsNotNone(exc1)
        self.assertIsNotNone(exc2)
        self.assertIsNotNone(exc3)

    def test_with_correct_input(self):
        input = '2x^3 + 3x + 1'
        wanted_result = ['2x^3 ',' 3x ', ' 1']

        result = from_string_to_list_of_terms(input)

        self.assertTrue(result == wanted_result)

class TestGetCoeficient(unittest.TestCase):
    def test_with_correct_values_should_return_int(self):
        input1 = '2x^3'
        input2 = '3x'
        input3 = '1'

        self.assertTrue(get_coeficient(input1) == 2)
        self.assertTrue(get_coeficient(input2) == 3)
        self.assertTrue(get_coeficient(input3) == 1)



class TestValidateTerm(unittest.TestCase):
    # ^ always after x -> Error
    # if there is not ^ and int after x -> Error
    def test_with_swapped_signs(self):
        input1 = '1^x'
        input2 = '2x3'
        exc1 = None
        exc2 = None

        try:
            validate_term(input1)
        except TypeError as err:
            exc1 = err

        try:
            validate_term(input2)
        except TypeError as err:
            exc2 = err

        self.assertIsNotNone(exc1)
        self.assertIsNotNone(exc2)

    def test_with_valid_term(self):
        input = '2x^3'

        self.assertTrue(validate_term(input))

class TestGetPow(unittest.TestCase):
    def test_with_correct_values(self):
        input1 = '2x^3 '
        input2 = '2x^ 2'
        input3 = '2x^ 2 '

        self.assertTrue(get_pow(input1) == 3)
        self.assertTrue(get_pow(input2) == 2)
        self.assertTrue(get_pow(input3) == 2)
        
if __name__ == '__main__':
	unittest.main()