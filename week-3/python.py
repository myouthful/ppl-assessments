def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount (if applicable).

  Args:
      price: The original price of the item.
      discount_percent: The discount percentage (0 to 100).

  Returns:
      The final price after applying the discount, or the original price if the discount is less than 20%.
  """

  discount = price * discount_percent / 100
  if discount_percent >= 20:
    return price - discount
  else:
    return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate final price with discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the result
print(f"Final price after discount: ${final_price:.2f}")
