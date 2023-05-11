class LoanCalculator:
    def __init__(self, loan_amount, interest_rate, loan_term_years):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term_years = loan_term_years
        self.loan_term_months = loan_term_years * 12

    def calculate_monthly_payment(self):
        r = self.interest_rate / 1200
        n = self.loan_term_months
        P = self.loan_amount
        monthly_payment = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
        return round(monthly_payment, 2)

    def calculate_total_cost(self):
        monthly_payment = self.calculate_monthly_payment()
        total_cost = monthly_payment * self.loan_term_months
        return round(total_cost, 2)

    def get_payment_schedule(self):
        monthly_payment = self.calculate_monthly_payment()
        balance = self.loan_amount
        payment_schedule = []
        for month in range(1, self.loan_term_months + 1):
            interest_payment = balance * self.interest_rate / 1200
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            row = (month, round(interest_payment, 2), round(principal_payment, 2), round(balance, 2))
            payment_schedule.append(row)
        return payment_schedule
        
if __name__ == '__main__':
    loan_amount = 100000
    interest_rate = 4.5
    loan_term_years = 30

    calculator = LoanCalculator(loan_amount, interest_rate, loan_term_years)

    monthly_payment = calculator.calculate_monthly_payment()
    total_cost = calculator.calculate_total_cost()
    payment_schedule = calculator.get_payment_schedule()

    print(f"Monthly payment: ${monthly_payment}")
    print(f"Total cost of the loan: ${total_cost}")
    print("Payment schedule:")
    print("Month\tInterest\tPrincipal\tBalance")
    for row in payment_schedule:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")