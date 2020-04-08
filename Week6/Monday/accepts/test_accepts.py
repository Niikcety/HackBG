import unittest
from accepts import accepts


@accepts(str, str, str)
def say_hello(name, family):
    return "{} {}".format(name, family)


@accepts(str, str, int)
def say_hello2(fname, mname, lname):
    return "{} {} {}".format(fname, mname, lname)


@accepts(str, str, int)
def say_hello3(first_name, family_name, age):
    return "My name is {} {} and I'm {} years old".format(first_name, family_name, age)


class TestAccepts(unittest.TestCase):
    def test_with_different_length_of_inner_and_outter_arguments(self):
        exc = None

        try:
            say_hello('Niki', 'Neshev')
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_with_incorrect_arguments_should_raise_error(self):
        exc = None

        try:
            say_hello2('Niki', 'Kolev', 'Neshev')
        except TypeError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_with_correct_arguments(self):
        wanted_result = "My name is {} {} and I'm {} years old".format('Nikolay', 'Neshev', 21)
        result = say_hello3('Nikolay', 'Neshev', 21)

        self.assertEqual(wanted_result, result)


if __name__ == '__main__':
    unittest.main()
