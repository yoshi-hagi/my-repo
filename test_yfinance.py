import yfinance as yf

df = yf.download('7203.T')

print(df.tail())