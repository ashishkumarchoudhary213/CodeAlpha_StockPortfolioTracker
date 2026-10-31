"""CodeAlpha Task 2: Stock Portfolio Tracker

A beginner-friendly console application that calculates the value of a
stock portfolio using manually defined (hardcoded) stock prices.
Prices are sample values, not live market prices.
"""

import csv
from datetime import datetime
from pathlib import Path

# Hardcoded sample prices, as required by the task. Values are in USD.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 175.00,
    "NVDA": 120.00,
    "META": 500.00,
}


def display_available_stocks():
    """Display the stock symbols and their sample prices."""
    print("\nAvailable stocks (sample prices in USD):")
    print("-" * 40)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:,.2f}")
    print("-" * 40)


def get_positive_quantity():
    """Read and validate a positive whole-number share quantity."""
    while True:
        raw_quantity = input("Enter quantity (whole shares): ").strip()
        try:
            quantity = int(raw_quantity)
            if quantity <= 0:
                print("Quantity must be greater than zero. Please try again.")
                continue
            return quantity
        except ValueError:
            print("Invalid quantity. Please enter a whole number, such as 5.")


def collect_portfolio():
    """Collect stock symbols and quantities from the user."""
    portfolio = []
    print("\nEnter the stock symbols you own. Type 'DONE' when finished.")

    while True:
        symbol = input("\nStock symbol: ").strip().upper()

        if symbol == "DONE":
            break
        if not symbol:
            print("Stock symbol cannot be empty.")
            continue
        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the available stock list. Please choose a listed symbol.")
            continue

        quantity = get_positive_quantity()
        price = STOCK_PRICES[symbol]
        investment_value = price * quantity

        # Repeated entries for the same symbol are combined in the summary.
        existing_stock = next((item for item in portfolio if item["symbol"] == symbol), None)
        if existing_stock:
            existing_stock["quantity"] += quantity
            existing_stock["investment_value"] += investment_value
        else:
            portfolio.append({
                "symbol": symbol,
                "price": price,
                "quantity": quantity,
                "investment_value": investment_value,
            })

        print(f"Added {quantity} share(s) of {symbol}.")

    return portfolio


def display_summary(portfolio):
    """Print the portfolio breakdown and total investment value."""
    if not portfolio:
        print("\nNo stocks were added. Portfolio is empty.")
        return 0.0

    print("\n" + "=" * 68)
    print("                 STOCK PORTFOLIO SUMMARY")
    print("=" * 68)
    print(f"{'Symbol':<12}{'Price/Share':>16}{'Quantity':>14}{'Investment':>20}")
    print("-" * 68)

    total_value = 0.0
    for item in portfolio:
        price_text = f"${item['price']:,.2f}"
        value_text = f"${item['investment_value']:,.2f}"
        print(
            f"{item['symbol']:<12}"
            f"{price_text:>16}"
            f"{item['quantity']:>14,}"
            f"{value_text:>20}"
        )
        total_value += item["investment_value"]

    print("-" * 68)
    print(f"{'TOTAL INVESTMENT':<42}{f'${total_value:,.2f}':>20}")
    print("=" * 68)
    return total_value


def save_portfolio_to_csv(portfolio, total_value):
    """Save the portfolio breakdown to a CSV file in the current folder."""
    filename = Path("portfolio_summary.csv")
    with filename.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock Symbol", "Price per Share (USD)", "Quantity", "Investment Value (USD)"])
        for item in portfolio:
            writer.writerow([
                item["symbol"],
                f"{item['price']:.2f}",
                item["quantity"],
                f"{item['investment_value']:.2f}",
            ])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", f"{total_value:.2f}"])
        writer.writerow(["Generated At", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "", ""])

    print(f"\nPortfolio successfully saved to: {filename.resolve()}")


def main():
    print("=" * 48)
    print("          STOCK PORTFOLIO TRACKER")
    print("             CodeAlpha - Task 2")
    print("=" * 48)
    print("Note: Prices are hardcoded sample values, not live market data.")

    display_available_stocks()
    portfolio = collect_portfolio()
    total_value = display_summary(portfolio)

    if portfolio:
        while True:
            choice = input("\nWould you like to save this summary as a CSV file? (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                try:
                    save_portfolio_to_csv(portfolio, total_value)
                except OSError as error:
                    print(f"Could not save the CSV file: {error}")
                break
            if choice in ("n", "no"):
                print("CSV export skipped.")
                break
            print("Please enter 'y' for yes or 'n' for no.")

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
