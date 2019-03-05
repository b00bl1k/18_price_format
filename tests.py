import unittest
from decimal import Decimal
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_string_float(self):
        self.assertEqual("1 234.12", format_price("1234.12"))

    def test_string_float_with_trailing_zeros(self):
        self.assertEqual("1 234", format_price("1234.000"))

    def test_string_int(self):
        self.assertEqual("12 345 678", format_price("12345678"))

    def test_int(self):
        self.assertEqual("1 234 567", format_price(1234567))

    def test_float(self):
        self.assertEqual("1 234.12", format_price(1234.12))

    def test_string_value_error(self):
        self.assertEqual(None, format_price("123a.54"))

    def test_none(self):
        self.assertEqual(None, format_price(None))

    def test_list(self):
        self.assertEqual(None, format_price([123]))

    def test_bool(self):
        self.assertEqual(None, format_price(True))

    def test_round(self):
        self.assertEqual("0", format_price("0.0000000001"))

    def test_decimal(self):
        self.assertEqual("0.10", format_price(Decimal(".1")))


if __name__ == "__main__":
    unittest.main()
