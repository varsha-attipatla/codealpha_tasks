# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 300
}

# Dictionary to store user's portfolio
portfolio = {}

# Ask how many different stocks user wants to enter
num_stocks = int(input("How many different stocks do you want to enter? "))

# Get stock info from user
for _ in range(num_stocks):
    stock_name = input("Enter stock name (e.g., AAPL): ").upper()
    if stock_name not in stock_prices:
        print(f"Stock {stock_name} is not available in our price list.")
        continue
    quantity = int(input(f"Enter quantity for {stock_name}: "))
    portfolio[stock_name] = quantity

# Calculate total investment
total_investment = 0
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x ${price} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: Save to a file
save = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.csv", "w") as file:
        file.write("Stock,Quantity,Price per Share,Total Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock},{quantity},{price},{value}\n")
        file.write(f"\nTotal Investment,,,{total_investment}")
    print("Summary saved to 'portfolio_summary.csv'.")
