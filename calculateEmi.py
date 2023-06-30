def calculate_loan_details(principal, tenure, interest_rate):
    monthly_interest_rate = interest_rate / (12 * 100)
    total_months = int(tenure * 12)
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months) / ((1 + monthly_interest_rate) ** total_months - 1)
    loan_details = []

    remaining_principal = principal
    for month in range(1, total_months + 1):
        interest_payment = remaining_principal * monthly_interest_rate
        principal_payment = emi - interest_payment
        remaining_principal -= principal_payment
        loan_details.append((month, emi, principal_payment, interest_payment, remaining_principal))

    return loan_details


principal_amount = float(input("Enter the principal amount: "))
tenure_years = float(input("Enter the tenure in years: "))
interest_rate = float(input("Enter the annual interest rate: "))

loan_details = calculate_loan_details(principal_amount, tenure_years, interest_rate)
print("====================================================================")
print("*************************** Loan Details ***************************")
print("====================================================================")
print("Month\tEMI\tPrincipal\tInterest\tRemaining Amount")
print("--------------------------------------------------------------------")
for month, emi, principal_payment, interest_payment, remaining_principal in loan_details:
    print("{:d}\t{:.2f}\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(month, emi, principal_payment, interest_payment, remaining_principal))
print("====================================================================")
