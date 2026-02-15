prices = [450, 1200, 899, 1500, 300]
count = 0  
for price in prices:
    if price > 1000:
        count += 1
print("Products above 1000:", count)
