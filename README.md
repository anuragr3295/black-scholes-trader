# Black Scholes Trader

This project demonstrates a very simple framework for building an algorithmic trader
that consumes real-time market data from Polygon.io via WebSockets and uses the
Black‑Scholes model to price options.

## Features

- Connects to the Polygon WebSocket API
- Computes theoretical option prices with the Black‑Scholes model
- Provides a starting point for real-time trading strategies

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Export your Polygon API key as an environment variable:

   ```bash
   export POLYGON_API_KEY="<your-api-key>"
   ```

3. Run the trader:

   ```bash
   python -m src.trader
   ```

The example subscribes to trades for `AAPL`. Modify `src/trader.py` to subscribe
to additional symbols or implement trading logic in the `on_message` method.

**Note:** Actual trading execution is not included. You would need to integrate
with a brokerage API to send real orders.
