import pandas as pd
import numpy as np
import yfinance as yf


# Define parameters
N = 55 # Number of days for moving average and average true range
K1 = 2 # Multiple of ATR to use for stop loss
K2 = 0.5 # Multiple of ATR to use for adding to position
fractional_equity = 0.02 # Fraction of equity to risk per trade

# Load historical data
ticker = "RIG"
data = yf.download(ticker, period="1y")

from IPython.display import display
display(data)

# Calculate the True Range for each day
true_range = pd.DataFrame({
    "TR1": abs(data["High"] - data["Low"]),
    "TR2": abs(data["High"] - data["Adj Close"].shift(1)),
    "TR3": abs(data["Low"] - data["Adj Close"].shift(1))
})
data["TR"] = true_range.max(axis=1)

# Calculate the Average True Range (ATR)
data["ATR"] = data["TR"].rolling(window=N+1).mean()
display(data)

# Calculate the entry and exit points for long positions
data["long_entry"] = data["High"].rolling(window=N+1).max().shift(1)
data["long_exit"] = data["Low"].rolling(window=N+1).min().shift(1)

# Calculate the entry and exit points for short positions
data["short_entry"] = data["Low"].rolling(window=N+1).min().shift(1)
data["short_exit"] = data["High"].rolling(window=N+1).max().shift(1)
display(data)

# Create a DataFrame to store the trading signals and the cumulative returns
signals = pd.DataFrame(index=data.index)
signals["signal"] = 0.0
signals["signal"] = np.where(data["Adj Close"] > data["long_entry"], 1.0, signals["signal"])
signals["signal"] = np.where(data["Adj Close"] < data["short_entry"], -1.0, signals["signal"])
signals["positions"] = signals["signal"].diff()
signals["returns"] = np.log(data["Adj Close"]/data["Adj Close"].shift(1))
display(signals)

# Backtest the trading signals
initial_capital = float(100000.0)
positions = pd.DataFrame(index=signals.index).fillna(0.0)
positions["RIG"] = 100 * signals["signal"]
portfolio = positions.multiply(data["Adj Close"], axis=0)
pos_diff = positions.diff()
portfolio["holdings"] = (positions.multiply(data["Adj Close"], axis=0)).sum(axis=1)
portfolio["cash"] = initial_capital - (pos_diff.multiply(data["Adj Close"], axis=0)).sum(axis=1).cumsum()
portfolio["total"] = portfolio["cash"] + portfolio["holdings"]
portfolio["returns"] = portfolio["total"].pct_change()
# Print the final portfolio value and the Sharpe ratio
print("Final Portfolio Value: ${:.2f}".format(portfolio["total"].iloc[-1]))

# indicates how much return an investor is receiving for each fractional_equity of risk taken
print("Sharpe Ratio: {:.2f}".format((portfolio["returns"].mean() / portfolio["returns"].std()) * np.sqrt(252)))
data['ATR'].ewm


