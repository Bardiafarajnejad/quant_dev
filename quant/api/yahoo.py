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

YAHOO_FIELDS = Literal["Open","High","Low","Close","Adj Close","Volume"]

def ydh(
    tickers: Union[str, list[str]],
    fields: Union[YAHOO_FIELDS, list[YAHOO_FIELDS]],
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
    if isinstance(fields,str):
        df = df.loc[:,df.columns.get_level_values(1).isin([fields])].T.reset_index(level=1, drop=True).T
    elif isinstance(fields, list):
        df = df.loc[:,df.columns.get_level_values(1).isin(fields)]
    else:
        raise TypeError(f"Unexpected fields: {fields}, must use fields specified in {YAHOO_FIELDS}")
    return df
