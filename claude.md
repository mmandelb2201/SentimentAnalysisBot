# Project Overview
This project is a quantitative algorithmic trading engine focused on US Equities. We are building two distinct strategies:
1. **The LLM Sentiment Swing Bot:** Fuses Alpha Vantage daily sentiment data with technical momentum indicators for multi-day holds.
2. **The "Panic Sinkhole" Microstructure Bot:** Hunts high-volatility, ask-heavy order book imbalances for short-term mean-reversion bounces (Limit order execution to avoid taker fees).

# Tech Stack
* **Language:** Python 3.10+
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** CatBoost, Scikit-Learn (Decision Trees for surrogate rule extraction)
* **Data Providers:** Alpha Vantage (Sentiment/OHLCV), Alpaca/Polygon (Market Data)
* **Execution:** Alpaca API

# Strict Quantitative Coding Rules

## 1. Data Processing & Vectorization
* NEVER use `.iterrows()`, `.apply()`, or standard `for` loops on Pandas DataFrames unless absolutely necessary.
* Always prioritize vectorized NumPy or Pandas operations for feature engineering and backtesting speed.
* Handle NaNs explicitly. Forward-fill (`ffill()`) for continuous metrics, or drop them depending on the context, but never leave them unhandled before passing to an ML model.

## 2. Preventing Lookahead Bias (CRITICAL)
* Every single predictive feature must be shifted by at least 1 period (`.shift(1)`) before being aligned with a target label.
* When computing rolling statistics, never include the current candle in the prediction for the current candle's outcome.

## 3. Feature Engineering Standards
* DO NOT use absolute price levels (e.g., raw `close` or `vwap`). 
* Always normalize absolute prices into relative metrics (e.g., Rolling Z-Scores, percentage distance from VWAP, or log returns).
* When building technical indicators, focus on multi-timeframe context rather than single-timeframe noise.

## 4. Execution Logic & Committee Scoring
* DO NOT stack multiple execution conditions using strict `AND` gates (e.g., `if A and B and C and D:`), as this causes trade starvation.
* Always use a "Committee Scoring" (soft voting) approach. Assign points to boolean conditions and execute when a threshold score is met (e.g., `score >= 3`).

## 5. Machine Learning Targets
* Always ensure the target labels (y) used for training perfectly mirror the exact Take Profit (TP), Stop Loss (SL), and Time Horizon limits of the execution engine.
* Do not trust overlapping density graphs for ML feature importance; use Quantile/Decile analysis or 2D Interaction Heatmaps to find non-linear alpha.

# Tone and Output Preferences
* Write concise, production-ready code.
* Skip generic explanations of basic Python concepts.
* If a requested feature introduces data leakage or overfitting risks, refuse to write it as requested, point out the mathematical flaw, and suggest a statistically sound alternative.

## 6. Code Quality & Formatting Standards
* **Imports:** All imports MUST be placed at the absolute top of the file. Group them systematically:
    1.  Standard Library imports (e.g., `os`, `sys`, `datetime`).
    2.  Third-party imports (e.g., `pandas`, `numpy`, `requests`).
    3.  Local application/library specific imports.
* **PEP 8 Compliance:** Adhere to PEP 8 standards for naming conventions. Use `snake_case` for variables and functions, and `PascalCase` for classes.
* **Type Hinting:** Use Python type hinting extensively for all function arguments and return types (e.g., `def fetch_data(ticker: str) -> pd.DataFrame:`). This prevents type-mismatch bugs in downstream execution logic.
* **Docstrings:** Every function and class must have a concise docstring explaining its purpose, arguments, and return value.
* **Modularity:** Avoid monolithic files. Break logic down into distinct, testable functions (e.g., separate data fetching, feature engineering, and model inference).
* **Error Handling:** Never use bare `except:` blocks. Always catch specific exceptions (e.g., `except requests.exceptions.RequestException as e:`) and log them appropriately.