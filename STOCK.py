#codeAlpha_projectname_stock portifolio
def stock_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 175,
        "AMZN": 185,
        "MSFT": 420
    }

    portfolio = {}
    
    print("--- Stock Portfolio Tracker ---")
    print("Available stocks in system:", ", ".join(stock_prices.keys()))
    
    while True:
        stock_name = input("\nEnter stock symbol to add (or type 'done' to calculate): ").upper().strip()
        if stock_name == "DONE":
            break
        
        if stock_name not in stock_prices:
            print("Stock symbol not recognized. Please choose from the available list.")
            continue
        
        try:
            quantity = int(input(f"Enter the quantity of {stock_name} you own: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            
            portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")

    print("\n--- Portfolio Summary ---")
    total_investment = 0
    summary_lines = ["--- Portfolio Summary ---"]

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_investment += value
        line = f"{stock}: {qty} shares @ ${price} each = ${value}"
        print(line)
        summary_lines.append(line)

    total_line = f"\nTotal Portfolio Value: ${total_investment}"
    print(total_line)
    summary_lines.append(total_line)

    try:
        with open("portfolio_summary.txt", "w") as file:
            file.write("\n".join(summary_lines))
        print("\nPortfolio details successfully saved to 'portfolio_summary.txt'.")
    except IOError:
        print("\nError: Could not save summary to file.")

if __name__ == "__main__":
    stock_tracker()
