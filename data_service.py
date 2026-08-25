"""Market universes and delayed historical-data retrieval."""
from __future__ import annotations

from datetime import date
import pandas as pd


MARKET_UNIVERSES = {
    "World Indices": {
        "NIFTY 50": "^NSEI", "S&P 500": "^GSPC", "NASDAQ Composite": "^IXIC",
        "Dow Jones": "^DJI", "Russell 2000": "^RUT", "FTSE 100": "^FTSE",
        "DAX": "^GDAXI", "CAC 40": "^FCHI", "Nikkei 225": "^N225",
        "Hang Seng": "^HSI", "Shanghai Composite": "000001.SS", "S&P/ASX 200": "^AXJO",
    },
    "Currencies": {
        "EUR/USD": "EURUSD=X", "GBP/USD": "GBPUSD=X", "USD/JPY": "JPY=X",
        "USD/CHF": "CHF=X", "AUD/USD": "AUDUSD=X", "USD/CAD": "CAD=X",
        "USD/INR": "INR=X", "US Dollar Index": "DX-Y.NYB",
    },
    "Commodities": {
        "Gold": "GC=F", "Silver": "SI=F", "WTI Crude": "CL=F",
        "Brent Crude": "BZ=F", "Copper": "HG=F", "Natural Gas": "NG=F",
    },
    "Risk & Rates": {
        "CBOE VIX": "^VIX", "US 10Y Yield": "^TNX", "US 5Y Yield": "^FVX",
        "US 13W Bill": "^IRX", "US Long Treasury ETF": "TLT", "Emerging Markets ETF": "EEM",
    },
}

ALL_ASSETS = {name: ticker for universe in MARKET_UNIVERSES.values() for name, ticker in universe.items()}
HISTORY_WINDOWS = {"5 Years": 5, "10 Years": 10, "20 Years": 20, "Maximum Available": None}


def download_prices(ticker: str, years: int | None = 20) -> pd.DataFrame:
    """Download daily adjusted market history, allowing long requested windows."""
    import yfinance as yf

    if years is None:
        data = yf.download(ticker, period="max", interval="1d", auto_adjust=True,
                           progress=False, threads=False)
    else:
        start = (pd.Timestamp(date.today()) - pd.DateOffset(years=years, days=10)).date()
        data = yf.download(ticker, start=start, interval="1d", auto_adjust=True,
                           progress=False, threads=False)
    if data.empty:
        raise ValueError("No observations were returned by the market-data provider.")
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    required = [c for c in ["Open", "High", "Low", "Close", "Volume"] if c in data]
    result = data[required].dropna(subset=["Close"]).copy()
    result.index = pd.to_datetime(result.index).tz_localize(None)
    return result[~result.index.duplicated(keep="last")].sort_index()


def prepare_returns(prices: pd.DataFrame, frequency: str = "Daily"):
    close = prices["Close"].copy()
    rule = {"Daily": None, "Weekly": "W-FRI", "Monthly": "ME"}[frequency]
    if rule:
        close = close.resample(rule).last().dropna()
    # A continuous futures series can contain a non-positive settlement (WTI in
    # April 2020). Log returns are undefined there, so isolate the observation
    # instead of generating a misleading infinite/complex return.
    positive_close = close.where(close > 0)
    returns = 100 * __import__("numpy").log(positive_close / positive_close.shift(1))
    return close, returns.dropna().rename("Return (%)")
