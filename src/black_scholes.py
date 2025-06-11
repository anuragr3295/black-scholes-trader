import math


def norm_cdf(x: float) -> float:
    """Cumulative distribution function for the standard normal distribution."""
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def price(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "call") -> float:
    """Compute Black-Scholes price for European options.

    Parameters
    ----------
    S : float
        Current underlying price
    K : float
        Strike price of the option
    T : float
        Time to expiration in years
    r : float
        Risk-free interest rate
    sigma : float
        Volatility of the underlying asset
    option_type : str
        "call" for call option, "put" for put option
    """
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be positive")

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        price = S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    elif option_type == "put":
        price = K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    return price


__all__ = ["price", "norm_cdf"]
