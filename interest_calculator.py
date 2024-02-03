
def interest_calc(principle):
    principle = int(input("Enter a annual ammount: "))
    percentage = 0.08
    annual_loss = 100,000
    year = 0
    for number in range(1, 10):
        number = (principle + percentage) - annual_loss
        year += 1
        print(f"Annual total amount year {year} ")
