from main import Product

try:
    product_price = input("Enter price\n")
    product_quantity = input("Enter quantity\n")
    product_description = input("Enter description\n")
    product_color = input("Enter color")

    Product.create(prod_price=product_price, prod_quantity=product_quantity,  prod_description= product_description, prod_color=product_color)
    print("products created successfully")

except:
    print("Failed to create products")