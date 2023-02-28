# Turtle Trading System in Python
The Turtle Trading System is a popular trading strategy that was originally taught by Richard Dennis and William Eckhardt to a group of traders in the 1980s. The strategy is based on a set of rules for entering and exiting trades, using a combination of price action and trend-following indicators. This python code implements the Turtle Trading System for stocks using pandas, numpy, and matplotlib libraries.

## Installation
1. Clone the repository or download the ZIP file.
2. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the program files.
3. Run the program using the following command:
```bash
python turtle_trading_system.py
```
4. The program will download historical stock price data for the specified ticker using the yfinance library, and then use that data to backtest the Turtle Trading System. The final portfolio value and Sharpe ratio will be printed to the console, and a plot of the portfolio's cumulative returns will be displayed in a separate window.

## Customization
The program can be customized by modifying the following parameters:

- `N`: The number of days to use for the moving average and ATR calculations.
- `K1`: The multiple of ATR to use for the stop loss.
- `K2`: The multiple of ATR to use for adding to a position.
- `unit`: The size of each position in dollars.
The program can also be customized by changing the ticker variable to a different stock symbol.

## Notes
- This program assumes that all trades are executed at the close of the day.
- This program does not take into account trading fees or slippage.
- This program only backtests the Turtle Trading System on a single stock. It is recommended to backtest on a portfolio of stocks for more accurate results.

## License
This code is released under the GNU General Public License v3.0. This means that you are free to use, modify and distribute the code, subject to the terms and conditions of the license. Please refer to the LICENSE file for more details.

## Disclaimer
 The code and information provided in this repository are for educational and informational purposes only. It is not intended to be and should not be construed as investment advice or a recommendation of any particular security, strategy, or investment product. The user of this code should be aware that there are risks involved in trading securities and that the use of this code and any results it produces does not guarantee any profits or prevent any losses. The user assumes all responsibility and risk for any trades they may enter into based on the information and signals produced by this code.