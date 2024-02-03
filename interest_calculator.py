percentage = 1.08 #8%, can be changed for different results
def interest_calc(cap, loss):
    year = 0
    for number in range(1, 11):
        cap *= percentage
        cap -= loss   
        year += 1
        print(f"Annual total amount year {year} is {cap:.2f} after {loss} is deducted")

principle = int(input("Enter an initial investment: "))
annual_loss = int(input("Enter an annual loss amount: "))
interest_calc(principle, annual_loss)
