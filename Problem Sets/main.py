# main.py

from finance_tools.compound_interest import calculate_compound_interest
from finance_tools.loan_payment import calculate_loan_payment
from finance_tools.investment_return import calculate_investment_return

# Calculating compound interest
principal = 1000
rate = 0.05
time = 5
future_value = calculate_compound_interest(principal, rate, time)
print(f"Future value with compound interest: ${future_value:.2f}")

# Calculating loan payment
loan_amount = 20000
annual_rate = 0.06
num_years = 5
monthly_payment = calculate_loan_payment(loan_amount, annual_rate, num_years)
print(f"Monthly loan payment: ${monthly_payment:.2f}")

# Calculating investment return
initial_investment = 5000
annual_rate = 0.08
num_years = 10
investment_value = calculate_investment_return(initial_investment, annual_rate, num_years)
print(f"Future investment value: ${investment_value:.2f}")