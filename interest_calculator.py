inflation_rate = 0.043 # as of 2023
initial_principal = int(input("Initial investment: "))
annual_withdrawal = int(input("Yearly withdrawal: "))
interest_rate = 0.08 #float(input("Interest rate (as a decimal, e.g., 0.08 for 8%): "))
def inflation_fighter(principal, withdrawal, interest, inflation):
    
    year = 0

    while principal > 0 and year < 100:  # Check until the principal depletes or reach 100 years
        year += 1
        interest_earned = principal * interest
        net_gain = interest_earned - withdrawal
        principal += net_gain  # Update principal for the next year
        
        # Correct calculation for net gain percentage relative to the principal at the start of the year
        net_gain_percentage = (net_gain / (principal - net_gain)) * 100
        
        if net_gain_percentage > inflation * 100:
            print(f"In year {year}, the net gain of {net_gain_percentage:.2f}% surpasses the inflation rate of {inflation*100:.2f}% with a total balance of {principal:.2f}.")
            return  # Exit after surpassing inflation
        
    if principal <= 0:
        print("The principal is depleted before surpassing inflation.")
    elif year >= 100:
        print("After 100 years, the investment has not surpassed the inflation rate.")

# Call the function with corrected parameters
inflation_fighter(initial_principal, annual_withdrawal, interest_rate, inflation_rate)
