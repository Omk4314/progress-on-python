#Building an inventory system
#category-> item-> details
global price
inventory = {
    "Electronics": {
        "Laptop": {"quantity": 10, "price": 999.99, "supplier": "TechCorp"},
        "Mouse":  {"quantity": 50, "price": 25.50,  "supplier": "GadgetInc"}
    },
    "Furniture": {
        "Chair": {"quantity": 20, "price": 150.00, "supplier": "ComfortCo"}
    }
}


def main():
    cat = input("Enter the category you want the total value of (furniture/electronics): ").title()
    total_value(inventory[cat])

def total_value(inventory_item):
    products = {}
    products = inventory_item
    total = 0
    for product_info in products.values():
        total += product_info["quantity"] * product_info["price"]
    print(total)


main()



