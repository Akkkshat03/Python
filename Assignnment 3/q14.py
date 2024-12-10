earnings_per_year = 1000
machine_cost = 6000
salvage_value = 2000
alternate_rate = 0.12

years = 1
while True:
    total_earnings = earnings_per_year * years + salvage_value
    alternative_investment = machine_cost * ((1 + alternate_rate) ** years)
    if total_earnings > alternative_investment:
        print(f"Minimum life of machine: {years} years")
        break
    years += 1
