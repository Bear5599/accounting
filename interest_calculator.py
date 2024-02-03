percentage = 1.08 # 8%, can be changed for different results

def interest_calc(cap, loss):
    year = 0
    inflation_rate = 4.3  # Inflation rate for comparison
    for _ in range(1, 11):
        initial_cap = cap
        cap_after_interest = cap * percentage  # Capital after interest
        cap = cap_after_interest - loss  # Final capital after deducting loss
        year += 1
        
        # Calculate net gain or loss percentage
        net_gain_percentage = ((cap_after_interest - loss) / initial_cap - 1) * 100
        
        print(f"Annual total amount year {year} is {cap:.2f} after {loss} is deducted")
        
        if net_gain_percentage > inflation_rate:
            print(f"You made over inflation this year with a net gain of {net_gain_percentage:.2f}%")
        else:
            print(f"You lost under inflation this year with a net gain of {net_gain_percentage:.2f}%")

# Example input values for testing
principle = int(input("Enter an initial investment: "))
annual_loss = int(input("Enter an annual loss amount: "))
interest_calc(principle, annual_loss)
