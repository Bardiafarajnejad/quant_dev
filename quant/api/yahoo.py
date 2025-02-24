import yfinance as yf
import pandas as pd
from typing import Literal, Union

YAHOO_FREQUENCIES = Literal[
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ]

def ydh(
    tickers: Union[str, list[str]],
    start_date: pd.Timestamp = pd.Timestamp(1980, 1, 1).floor("D"),
    end_date: pd.Timestamp = pd.Timestamp.now(),
    frequency: YAHOO_FREQUENCIES = "1d",
    threads: bool = False,
) -> pd.DataFrame:

    df: pd.DataFrame = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        interval=frequency,
        threads=threads,
        group_by="tickers",
        auto_adjust=False,
    )
    return df
