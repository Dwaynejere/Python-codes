# SMALL E-COMMERCE PLATFORM

def add_product(product_name, price, quantity):

    print(product_name,"is", price,"Quantity", quantity)

    #DICTIONARY
product = {
        'product_name' : "Air Forces",
        'price' : "2500.00",
        'quantity' : 5
       }
add_product(**product)

def update_price(product, new_price):

    print("The product is:",product,"The New Price is:", new_price)
    
    #DICTIONARY
product = {
        "product_name" : "Air Forces",
        "price" : 2500.00,
        "quantity" : 5
}

Update = {
    "new_price" : 5000.00
}


Update |= product

print(Update)

def update_quantity(product, quantity_change):
    print("Updated quantity of the Product:", quantity_change)
product = {
        "product_name" : "Air Forces",
        "price" : 2500.00,
        "quantity" : 5
}

quantity_change = {
        "quantity" : 20
}

quantity_change |= product
    
print(quantity_change)

