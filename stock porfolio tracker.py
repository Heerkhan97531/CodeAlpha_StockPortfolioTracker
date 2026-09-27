#python project
#Stock porfolio tracker 

def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 400,
        "AMZN": 175
    }
    
    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks and their prices are:")
    for stock, price in stock_prices.items():
        print(f" - {stock}: ${price} per share")
    print("-" * 40)
    
    user_portfolio = {}
    
    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL, TSLA) or type 'done' to finish: ").strip().upper()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print("This stock is not available. Please try again!")
            continue
            
        try:
            quantity = int(input(f"How many shares of {stock_name} do you want to buy? "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
            
        if stock_name in user_portfolio:
            user_portfolio[stock_name] += quantity
        else:
            user_portfolio[stock_name] = quantity
            
        print(f"Success! {quantity} shares of {stock_name} have been added.\n")

    if not user_portfolio:
        print("You did not add any stock. Program is exiting.")
        return

    print("\n" + "="*20 + " PORTFOLIO SUMMARY " + "="*20)
    grand_total = 0
    summary_lines = []
    
    summary_lines.append("--- My Stock Portfolio Summary ---\n")
    
    for stock, qty in user_portfolio.items():
        unit_price = stock_prices[stock]
        total_cost = unit_price * qty
        grand_total += total_cost
        
        line = f"Stock: {stock} | Quantity: {qty} | Price per share: ${unit_price} | Total: ${total_cost}"
        print(line)
        summary_lines.append(line + "\n")
        
    final_message = f"\nGrand Total Investment: ${grand_total}"
    print("=" * 60)
    print(final_message)
    print("=" * 60)
    
    summary_lines.append(f"\n{final_message}\n")
    file_choice = input("DO you wna to save this potfolio summary in a text file?(yes/no):").strip()
    if file_choice == "yes":
        file_name = "portfolio_summary.txt"
        with open(file_name, "w") as file:
            file.writelines (summary_lines)
        print(f"Success! your data has been successfully saved in '{file_name}' file")
    else:
        print("Alright, file not saved.")

if __name__ == "__main__":
    stock_portfolio_tracker()