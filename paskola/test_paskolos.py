import unittest
from loan_calculator import LoanCalculator

class TestLoanCalculator(unittest.TestCase):
    
    def test_monthly_payment(self):
        # Test with 0 interest rate
        loan_calculator = LoanCalculator(1000, 0, 1)
        self.assertEqual(loan_calculator.calculate_monthly_payment(), 83.33)
        
        # Test with 5% interest rate
        loan_calculator = LoanCalculator(1000, 5, 1)
        self.assertEqual(loan_calculator.calculate_monthly_payment(), 85.61)
        
        # Test with 10% interest rate
        loan_calculator = LoanCalculator(1000, 10, 1)
        self.assertEqual(loan_calculator.calculate_monthly_payment(), 87.92)
        
    def test_total_cost(self):
        # Test with 0 interest rate
        loan_calculator = LoanCalculator(1000, 0, 1)
        self.assertEqual(loan_calculator.calculate_total_cost(), 1000)
        
        # Test with 5% interest rate
        loan_calculator = LoanCalculator(1000, 5, 1)
        self.assertEqual(loan_calculator.calculate_total_cost(), 1027.29)
        
        # Test with 10% interest rate
        loan_calculator = LoanCalculator(1000, 10, 1)
        self.assertEqual(loan_calculator.calculate_total_cost(), 1055.06)
        
    def test_payment_schedule(self):
        # Test with 0 interest rate
        loan_calculator = LoanCalculator(1000, 0, 1)
        expected_schedule = [
            (1, 0.0, 83.33, 916.67),
            (2, 0.0, 83.33, 833.33),
            (3, 0.0, 83.33, 750.0),
            (4, 0.0, 83.33, 666.67),
            (5, 0.0, 83.33, 583.33),
            (6, 0.0, 83.33, 500.0),
            (7, 0.0, 83.33, 416.67),
            (8, 0.0, 83.33, 333.33),
            (9, 0.0, 83.33, 250.0),
            (10, 0.0, 83.33, 166.67),
            (11, 0.0, 83.33, 83.33),
            (12, 0.0, 83.33, 0.0)
        ]
        self.assertEqual(loan_calculator.get_payment_schedule(), expected_schedule)
        
        # Test with 5% interest rate
        loan_calculator = LoanCalculator(1000, 5, 1)
        expected_schedule = [
            (1, 4.17, 81.45, 918.55),
            (2, 3.82, 81.8, 836.75),
            (3, 3.46, 82.16, 754.59),
            (4, 3.08, 82.54, 672.05),
            (5, 2.69, 82.92, 589.13),
            (6, 2.28, 83.33, 505.8),
            (7, 1.86, 83.75, 422.05),
            (9, 1.43, 84.18, 337.87),
            (10, 0.99, 84.62, 253.25),
            (11, 0.54, 85.07, 168.18),
            (12, 0.08, 85.53, 82.65)
            ]
        self.assertEqual(loan_calculator.get_payment_schedule(), expected_schedule)
    
# Test with 10% interest rate
        loan_calculator = LoanCalculator(1000, 10, 1)
        expected_schedule = [        (1, 8.33, 79.25, 920.75),        (2, 7.34, 80.24, 840.51),        (3, 6.34, 81.23, 759.28),        (4, 5.34, 82.23, 677.05),        (5, 4.33, 83.24, 593.81),        (6, 3.31, 84.26, 509.55),        (7, 2.29, 85.28, 424.27),        (8, 1.26, 86.31, 338.96),        (9, 0.22, 87.35, 253.61),        (10, -0.83, 88.39, 168.22),        (11, -1.88, 89.44, 82.78),        (12, -2.94, 90.5, -2.72)    ]
        self.assertEqual(loan_calculator.get_payment_schedule(), expected_schedule)