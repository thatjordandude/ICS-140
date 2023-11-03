import unittest
from Assignment9 import county_tax, state_tax, total_tax

class TestSalesTax(unittest.TestCase):
    def test_county_tax(self):
        self.assertAlmostEqual(county_tax(1000), 25.00)
        self.assertAlmostEqual(county_tax(2500.50), 62.51)

    def test_state_tax(self):
        self.assertAlmostEqual(state_tax(1000), 50.00)
        self.assertAlmostEqual(state_tax(2500.50), 125.03)

    def test_total_tax(self):
        self.assertAlmostEqual(total_tax(1000), 75.00)
        self.assertAlmostEqual(total_tax(2500.50), 187.54)

if __name__ == "__main__":
    unittest.main()
