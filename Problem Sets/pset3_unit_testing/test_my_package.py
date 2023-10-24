import unittest
import my_package 

class TestMyPackage(unittest.TestCase):

    def test_calculate_compound_interest(self):
        # Test 1: Check if the function returns the correct result
        principal = 1000
        rate = 0.05
        time = 5
        expected_result = 1276.28
        result = my_package.calculate_compound_interest(principal, rate, time)
        self.assertAlmostEqual(result, expected_result, places=2)

        # Test 2: Test with different inputs
        principal = 2000
        rate = 0.03
        time = 7
        expected_result = 2545.97
        result = my_package.calculate_compound_interest(principal, rate, time)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_calculate_loan_payment(self):
        # Test 1: Check if the function returns the correct result
        loan_amount = 20000
        annual_rate = 0.06
        num_years = 5
        expected_result = 377.42
        result = my_package.calculate_loan_payment(loan_amount, annual_rate, num_years)
        self.assertAlmostEqual(result, expected_result, places=2)

        # Test 2: Test with different inputs
        loan_amount = 15000
        annual_rate = 0.04
        num_years = 10
        expected_result = 160.96
        result = my_package.calculate_loan_payment(loan_amount, annual_rate, num_years)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_calculate_investment_return(self):
        # Test 1: Check if the function returns the correct result
        initial_investment = 5000
        annual_rate = 0.08
        num_years = 10
        expected_result = 8509.50
        result = my_package.calculate_investment_return(initial_investment, annual_rate, num_years)
        self.assertAlmostEqual(result, expected_result, places=2)

        # Test 2: Test with different inputs
        initial_investment = 3000
        annual_rate = 0.1
        num_years = 5
        expected_result = 4861.58
        result = my_package.calculate_investment_return(initial_investment, annual_rate, num_years)
        self.assertAlmostEqual(result, expected_result, places=2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)