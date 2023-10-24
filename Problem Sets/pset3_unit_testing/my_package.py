def calculate_investment_return(initial_investment, annual_rate, num_years):
   
    return initial_investment * (1 + annual_rate * num_years)

def calculate_loan_payment(loan_amount, annual_rate, num_years):
    
    monthly_rate = annual_rate / 12
    num_months = num_years * 12
    return loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** -num_months))

def calculate_compound_interest(principal, rate, time):
    
    return principal * (1 + rate) ** time

