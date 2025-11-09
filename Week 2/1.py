product_prices = [85, 75, 45, 90, 35, 120, 50, 65]

filtered_prices = list(filter(lambda price: price >= 50, product_prices))
discounted_prices = list(map(lambda price: round(price * 0.9, 2), filtered_prices))

print("Original prices:", product_prices)
print("Prices >= $50:", filtered_prices)
print("Prices after 10% discount:", discounted_prices)