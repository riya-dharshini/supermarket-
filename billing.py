GST_RATE = 0.18

def calculate_gst(amount):
    return amount * GST_RATE

def apply_discount(amount, discount_rate):
    return amount - (amount * discount_rate / 100)

def generate_bill(order, discount_rate=0):
    order.calculate_total()
    gst = calculate_gst(order.total)
    total_with_gst = order.total + gst
    final_total = apply_discount(total_with_gst, discount_rate)
    
    order.discount = discount_rate
    order.final_total = final_total
    return order
