# Stock Portfolio Tracker — CodeAlpha Task 2

A Python console application that calculates the total investment value of a stock portfolio using manually defined stock prices. It also offers an option to export the portfolio summary to a CSV file.

## Features

- Displays a list of supported stock symbols and their hardcoded sample prices.
- Accepts stock symbols and share quantities from the user.
- Accepts lowercase or uppercase symbols (for example, `aapl` or `AAPL`).
- Validates stock symbols and positive whole-number quantities.
- Combines repeated entries for the same stock.
- Calculates and displays each holding's investment value and the total portfolio value.
- Optionally saves the summary to `portfolio_summary.csv`.
- Uses only Python's standard library; no third-party packages are required.

## Requirements

- Python 3.8 or later
- No external libraries

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

4. Choose stock symbols from the displayed list and enter the number of shares.
5. Type `DONE` when you have entered all holdings.
6. Review the portfolio total and enter `y` if you want to export the result to CSV.

## Supported sample stocks

| Symbol | Sample price per share (USD) |
|---|---:|
| AAPL | 180.00 |
| TSLA | 250.00 |
| GOOGL | 140.00 |
| MSFT | 420.00 |
| AMZN | 175.00 |
| NVDA | 120.00 |
| META | 500.00 |

These prices are intentionally hardcoded to match the assignment instructions. They are illustrative values and are **not live or current market prices**. To change a price, edit the `STOCK_PRICES` dictionary near the top of `main.py`.

## Calculation

For each stock:

`Investment Value = Price per Share × Quantity`

For the complete portfolio:

`Total Investment = Sum of all individual investment values`

## Example

If the user enters 2 shares of AAPL and 3 shares of TSLA:

- AAPL: 2 × $180.00 = $360.00
- TSLA: 3 × $250.00 = $750.00
- **Total investment: $1,110.00**

## Output file

If CSV export is selected, the program creates `portfolio_summary.csv` in the folder from which the program is run. The file contains each stock, its sample price, quantity, investment value, the total, and the generation timestamp.

## Concepts demonstrated

- **Dictionary:** stores stock symbols and their manually defined prices.
- **Input/output:** collects user entries and displays the summary.
- **Loops and conditionals:** process multiple holdings and validate input.
- **Functions:** divide the program into clear, reusable parts.
- **Basic arithmetic:** calculate individual and total investment values.
- **File handling:** write the optional CSV report.

## Project structure

```text
CodeAlpha_StockPortfolioTracker/
├── main.py
└── README.md
```
