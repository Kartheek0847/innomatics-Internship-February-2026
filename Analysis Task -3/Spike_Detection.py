sales = [1200, 1500, 900, 2200, 1400, 3000]
average_sales = sum(sales) / len(sales)
threshold = average_sales * 1.3

for day, amount in enumerate(sales, start=1):
    if amount > threshold:
        print(f"Day {day}: {amount}")
