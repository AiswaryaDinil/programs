import math
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50,
}
discount_rules = {
    "flat_10_discount": {
        "condition": lambda total: total > 200,
        "amount": 10,
    },
    "bulk_5_discount": {
        "condition": lambda quantity: quantity > 10,
        "amount": quantity * 0.05,
    },
    "bulk_10_discount": {
        "condition": lambda quantity: quantity > 20,
        "amount": quantity * 0.1,
    },
    "tiered_50_discount": {
        "condition": lambda quantity: quantity > 30 and any(quantity > 15 for quantity in quantity_list),
        "amount": lambda quantity_list: sum(
            [
                products[product] * (quantity - 15) * 0.5
                for product, quantity in quantity_list.items()
                if quantity > 15
            ]
        ),
    },
}
fees = {
    "gift_wrap": 1,
    "shipping": 5,
}
quantity_list = []
for product in products:
    quantity = int(input("Enter the quantity of {}: ".format(product)))
    quantity_list.append(quantity)
gift_wrap = input("Is the product wrapped as gift? (y/n): ")
subtotal = sum(
    [
        products[product] * quantity
        for product, quantity in zip(products, quantity_list)
    ]
)
discount_name, discount_amount = None, 0
for discount_rule in discount_rules:
    if discount_rules[discount_rule]["condition"](subtotal):
        discount_name = discount_rule
        discount_amount = discount_rules[discount_rule]["amount"]
        break

shipping_fee = math.ceil(subtotal / 10) * fees["shipping"]

gift_wrap_fee = quantity_list.count(1) * fees["gift_wrap"]

total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

print("Product Name | Quantity | Total")
for product, quantity, total_product in zip(products, quantity_list, [
    products[product] * quantity for product, quantity in zip(products, quantity_list)
]):
    print("{:20} | {:5} | ${:10.2f}".format(product, quantity, total_product))

print("Subtotal: ${:10.2f}".format(subtotal))
if discount_name is not None:
    print("Discount: {:10.2f} ({:s})".format(discount_amount, discount_name))
print("Shipping Fee: ${:10.2f}".format(shipping_fee))
print("Gift Wrap Fee: ${:10.2f}".format(gift_wrap_fee))
print("Total: ${:10.2f}".format(total))
