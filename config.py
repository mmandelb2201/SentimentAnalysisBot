# --- AI & Semiconductors ---
# fmt: off
TICKERS = [
    "NVDA", "AMD", "TSM", "AVGO", "MU",
    "INTC", "ARM", "QCOM", "ASML", "SMCI",
    "MRVL", "TXN", "KLAC", "AMAT", "LRCX",

    # --- Mega-Cap Tech ---
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "TSLA", "NFLX", "CRM", "ADBE", "ORCL",

    # --- High-Beta Software / Cloud ---
    "PLTR", "CRWD", "SNOW", "DDOG", "NET",
    "NOW", "SHOP", "MDB", "TEAM", "ZS",
    "PANW", "HUBS", "WDAY", "XYZ", "ROKU",  # XYZ = Block Inc (formerly SQ)

    # --- Retail & Crypto Narrative ---
    "COIN", "MSTR", "HOOD", "MARA", "RIOT",
    "RBLX", "U", "GME", "AMC", "SOFI",
]
# fmt: on

# --- Benchmark ---
# Pulled via Alpha Vantage (TIME_SERIES_DAILY_ADJUSTED)
BENCHMARK_TICKER = ["SPY"]

# --- Macro Universe ---
# Pulled via yfinance: S&P 500 Futures, Nasdaq 100 Futures, 10-Year Treasury Yield
MACRO_YFINANCE = ["ES=F", "NQ=F", "^TNX"]

# --- Macro filename stem → output column name mapping ---
# The yfinance fetcher sanitises ticker symbols when writing CSVs:
#   '^' → '_'  and  '=' → '_'
# This map translates those safe stems back to human-readable column names
# used in the merged dataset.
MACRO_YFINANCE_MAP: dict[str, str] = {
    "ES_F": "ESF_Close",  # S&P 500 Futures   (ES=F  → ES_F_daily.csv)
    "NQ_F": "NQF_Close",  # Nasdaq 100 Futures (NQ=F  → NQ_F_daily.csv)
    "_TNX": "TNX_Close",  # 10-Year Treasury   (^TNX  → _TNX_daily.csv)
}
