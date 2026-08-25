# Volatility Characteristics Laboratory

An educational Streamlit application from The Mountain Path Academy for discovering the empirical characteristics of market volatility with actual historical market data.

## What students investigate

Each app tab focuses on one characteristic:

1. **Time variation** — rolling volatility shows why risk is not constant.
2. **Clustering** — squared-return autocorrelation shows why large moves group together.
3. **Persistence** — autocorrelation decay and an indicative half-life show how shocks fade.
4. **Mean reversion** — high- and low-volatility periods move around a long-run anchor.
5. **Fat tails** — histograms, Normal overlays and Q–Q plots reveal excess extremes.
6. **Asymmetry** — subsequent absolute moves are compared after positive and negative shocks.
7. **Cross-market dynamics** — normalised rolling volatility and return correlations compare markets.

## Market coverage

- Major world indices
- Major currency pairs and the US Dollar Index
- Gold, silver, crude oil, copper and natural gas
- VIX, US Treasury yields and selected market ETFs
- 5-year, 10-year, 20-year or maximum-available histories
- Daily, weekly and monthly log returns

The app reports the **actual available history** for every selected series. A requested 20-year window does not imply that every instrument has 20 years of usable observations.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Upload this folder to a GitHub repository.
2. Create a Streamlit Community Cloud app.
3. Select the repository, branch and `app.py`.
4. Deploy. The default market-data source requires no API key.

## Data and interpretation notice

The app uses a public market-data interface. Information may be delayed, incomplete, revised or temporarily unavailable. Futures histories represent a provider-supplied continuous series and may contain contract-roll effects. Results are descriptive educational evidence, not investment advice or a trading signal.

© 2026 The Mountain Path Academy · Prof. V. Ravichandran
