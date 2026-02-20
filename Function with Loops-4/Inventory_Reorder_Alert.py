def check_inventory(stock_data):
    for product, quantity in stock_data.items():
        if quantity < 15:
            print(product, "- Reorder Alert")
        else:
            print(product, "- Stock OK")


products = {
    "Rice": 20,
    "Sugar": 10,
    "Oil": 18,
    "Salt": 5
}

check_inventory(products)