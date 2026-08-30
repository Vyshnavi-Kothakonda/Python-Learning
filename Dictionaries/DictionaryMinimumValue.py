prices = {
    "laptop": 55000,
    "mouse": 800,
    "keyboard": 1500,
    "headphones": 2500
}
lowest_item = min(prices, key=prices.get)
print("Lowest Price:", prices[lowest_item])
print("Item:", lowest_item)
