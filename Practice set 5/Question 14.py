# Dictionary of products and their prices
products = {
    "Laptop": 55000,
    "Mobile": 25000,
    "Headphones": 3000,
    "Tablet": 18000
}

# Find product with highest price
highest_product = max(products, key=products.get)

print("Product with highest price:", highest_product)
print("Price:", products[highest_product])