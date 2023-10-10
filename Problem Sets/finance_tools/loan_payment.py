def calculate_loan_payment(loan_amount, annual_rate, num_years):
    
    monthly_rate = annual_rate / 12
    num_months = num_years * 12
    return loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** -num_months))