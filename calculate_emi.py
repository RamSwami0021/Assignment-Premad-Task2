def calculate_emi(principal, tenure, interest_rate):
    n = tenure * 12
    r = interest_rate / (12 * 100)
    emi = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    
    return emi

principal_amount = float(input("Enter the principal amount: "))
tenure_years = float(input("Enter the tenure in years: "))
interest_rate = float(input("Enter the annual interest rate: "))

emi = calculate_emi(principal_amount, tenure_years, interest_rate)

total_months = tenure_years * 12
total_amount = emi * total_months
interest_amount = total_amount - principal_amount

table = [
    ["Description", "Value"],
    ["Principal amount", principal_amount],
    ["Interest amount", interest_amount],
    ["Total amount", total_amount],
    ["EMI for the loan", emi]
]

max_length = max(len(row[0]) for row in table)
print("===================================")
for row in table:
    print("-----------------------------------")
    print("{:<{}}  {}".format(row[0], max_length, row[1]))
print("===================================")