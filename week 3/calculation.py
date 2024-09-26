def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    If the discount is 20% or higher, it applies the discount.
    Otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price
if final_price != original_price:
    print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
