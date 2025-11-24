def increase_price_by_5(func):
    def wrapper(price_dict):
        updated = {item: round(price * 1.05, 2) for item, price in price_dict.items()}
        return func(updated)
    return wrapper

@increase_price_by_5
def display_prices(prices):
    print("After increase  price\n")
    for item, price in prices.items():
        print(f"{item}: {price}")

prices = {"Pen": 10, "Book": 50, "Bag": 800, "Bottle": 120}
display_prices(prices)
