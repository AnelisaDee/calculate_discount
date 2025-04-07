def calculate_discount(price, discount_percent):
    if(discount_percent >= 20):
        discount_price = price *(discount_percent / 100)
        final_price = price - discount_price
        return final_price
    else:
        return price

price = float(input("What is the original price? "))
discount_percent = float(input("What is the discount percentage? "))

final_price = calculate_discount(price, discount_percent)

print(f"The final price after discount is: ${final_price:.2f}")