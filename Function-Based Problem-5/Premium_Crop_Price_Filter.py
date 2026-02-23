def premium_crop_filter(prices):
    premium = []

    for price in prices:
        if price > 2000:
            premium.append(price)

    print("Premium Crops:", premium)
crop_prices = [1500, 2500, 1800, 3200]
premium_crop_filter(crop_prices)