from models import Product, CustomerOrder
from billing import generate_bill
from utils import get_current_date
def main():
    available_products = {
        "Milk": Product("Milk", 50),
        "Bread": Product("Bread", 30),
        "Eggs": Product("Eggs", 5)
    }
    customer_name = input("Enter customer name: ")
    order = CustomerOrder(customer_name)
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        if product_name not in available_products:
            print("Product not found. Please enter a valid product name.")
            continue
        quantity = int(input(f"Enter quantity for {product_name}: "))
        order.add_product(available_products[product_name], quantity)
    order.set_date(get_current_date())
    final_order = generate_bill(order, discount_rate=10)
    print("\n----- BILL -----")
    print(f"Customer: {final_order.customer_name}")
    print(f"Date: {final_order.date}")
    print("Items Ordered:")
    for item in final_order.items:
        print(f"- {item[0].name} x {item[1]}: {item[0].price * item[1]}")
    print(f"Total: {final_order.total}")
    print(f"GST: {final_order.total * 0.18}")
    print(f"Discount: {final_order.discount}%")
    print(f"Final Total: {final_order.final_total}")
if __name__ == "__main__":
    main()
