import unittest
from unittest.mock import patch
import pandas as pd

from quant.api.yahoo import ydh


class TestAPIYahoo(unittest.TestCase):
    @patch("quant.api.yahoo.yf.download")
    def test_tickers_list_fields_none(self, mock_yf_download):
        tickers = ["TSLA", "NVDA"]
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [
            [
                13.14,
                13.15,
                12.91,
                13.06,
                13.02,
                192424000.0,
                233.33,
                239.57,
                230.37,
                235.22,
                235.22,
                148949700.0,
            ]
        ]
        df_columns = pd.MultiIndex.from_product(
            [tickers, fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers, start_date=data_date, end_date=data_date + pd.Timedelta(days=1)
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)
        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_tickers_list_fields_list_of_2(self, mock_yf_download):
        tickers = ["TSLA", "NVDA"]
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        fields_wanted = ["Close", "Volume"]
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [
            [
                13.14,
                13.15,
                12.91,
                13.06,
                13.02,
                192424000.0,
                233.33,
                239.57,
                230.37,
                235.22,
                235.22,
                148949700.0,
            ]
        ]
        df_columns = pd.MultiIndex.from_product(
            [tickers, fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers,
            fields=fields_wanted,
            start_date=data_date,
            end_date=data_date + pd.Timedelta(days=1),
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)
        column_mask = expected_output.columns.get_level_values(1).isin(fields_wanted)
        expected_output = expected_output.iloc[:, column_mask]

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_tickers_list_fields_list_of_1(self, mock_yf_download):
        tickers = ["TSLA", "NVDA"]
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        fields_wanted = ["Close"]
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [
            [
                13.14,
                13.15,
                12.91,
                13.06,
                13.02,
                192424000.0,
                233.33,
                239.57,
                230.37,
                235.22,
                235.22,
                148949700.0,
            ]
        ]
        df_columns = pd.MultiIndex.from_product(
            [tickers, fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers,
            fields=fields_wanted,
            start_date=data_date,
            end_date=data_date + pd.Timedelta(days=1),
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)
        column_mask = expected_output.columns.get_level_values(1).isin(fields_wanted)
        expected_output = expected_output.iloc[:, column_mask]

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_tickers_list_fields_str(self, mock_yf_download):
        tickers = ["TSLA", "NVDA"]
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        fields_wanted = "Close"
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [
            [
                13.14,
                13.15,
                12.91,
                13.06,
                13.02,
                192424000.0,
                233.33,
                239.57,
                230.37,
                235.22,
                235.22,
                148949700.0,
            ]
        ]
        df_columns = pd.MultiIndex.from_product(
            [tickers, fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers,
            fields=fields_wanted,
            start_date=data_date,
            end_date=data_date + pd.Timedelta(days=1),
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)
        column_mask = expected_output.columns.get_level_values(1).isin([fields_wanted])
        expected_output = (
            expected_output.iloc[:, column_mask].T.reset_index(level=1, drop=True).T
        )

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_tickers_str_fields_none(self, mock_yf_download):
        tickers = "TSLA"
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [[13.14, 13.15, 12.91, 13.06, 13.02, 192424000.0]]
        df_columns = pd.MultiIndex.from_product(
            [[tickers], fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers, start_date=data_date, end_date=data_date + pd.Timedelta(days=1)
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_tickers_str_fields_list_of_2(self, mock_yf_download):
        tickers = "TSLA"
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        fields_wanted = ["Close", "Volume"]
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [[13.14, 13.15, 12.91, 13.06, 13.02, 192424000.0]]
        df_columns = pd.MultiIndex.from_product(
            [[tickers], fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers,
            fields=fields_wanted,
            start_date=data_date,
            end_date=data_date + pd.Timedelta(days=1),
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)
        column_mask = expected_output.columns.get_level_values(1).isin(fields_wanted)
        expected_output = expected_output.iloc[:, column_mask]

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_tickers_str_fields_list_of_1(self, mock_yf_download):
        tickers = "TSLA"
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        fields_wanted = ["Close"]
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [[13.14, 13.15, 12.91, 13.06, 13.02, 192424000.0]]
        df_columns = pd.MultiIndex.from_product(
            [[tickers], fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers,
            fields=fields_wanted,
            start_date=data_date,
            end_date=data_date + pd.Timedelta(days=1),
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)
        column_mask = expected_output.columns.get_level_values(1).isin(fields_wanted)
        expected_output = expected_output.iloc[:, column_mask]

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_tickers_str_fields_str(self, mock_yf_download):
        tickers = "TSLA"
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        fields_wanted = "Close"
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [[13.14, 13.15, 12.91, 13.06, 13.02, 192424000.0]]
        df_columns = pd.MultiIndex.from_product(
            [[tickers], fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        actual_output = ydh(
            tickers,
            fields=fields_wanted,
            start_date=data_date,
            end_date=data_date + pd.Timedelta(days=1),
        )
        expected_output = pd.DataFrame(df_data, columns=df_columns, index=df_index)
        column_mask = expected_output.columns.get_level_values(1).isin([fields_wanted])
        expected_output = (
            expected_output.iloc[:, column_mask].T.reset_index(level=1, drop=True).T
        )

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        pd.testing.assert_frame_equal(actual_output, expected_output)
        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    @patch("quant.api.yahoo.yf.download")
    def test_fields_type_error(self, mock_yf_download):
        tickers = "TSLA"
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        fields_wanted = 0
        data_date = pd.Timestamp(2020, 12, 31)

        df_data = [[13.14, 13.15, 12.91, 13.06, 13.02, 192424000.0]]
        df_columns = pd.MultiIndex.from_product(
            [[tickers], fields], names=["Ticker", "Price"]
        )
        df_index = pd.DatetimeIndex([data_date], name="Date", freq=None)
        mock_yf_download.return_value = pd.DataFrame(
            df_data, columns=df_columns, index=df_index
        )

        with self.assertRaises(TypeError) as context:
            ydh(
                tickers,
                fields=fields_wanted,
                start_date=data_date,
                end_date=data_date + pd.Timedelta(days=1),
            )
        self.assertEqual(
            context.exception.args[0], f"Unexpected fields type: {fields_wanted}"
        )

        call_args_expected = {
            "tickers": tickers,
            "start": data_date,
            "end": data_date + pd.Timedelta(days=1),
            "interval": "1d",
            "threads": False,
            "group_by": "tickers",
            "auto_adjust": False,
        }

        self.assertEqual(mock_yf_download.call_args.kwargs, call_args_expected)

    def test_api_working(self):
        tickers = "TSLA"
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        data_date = pd.Timestamp(2020, 12, 31)
        actual_output = ydh(
            tickers,
            fields=None,
            start_date=data_date,
            end_date=data_date + pd.Timedelta(days=1),
        )

        self.assertTrue(len(actual_output) > 0)
        self.assertFalse(actual_output.empty)
        self.assertListEqual(
            list(actual_output.columns.get_level_values(0)), [tickers] * len(fields)
        )
        self.assertListEqual(list(actual_output.columns.get_level_values(1)), fields)
        self.assertListEqual(list(actual_output.index), [data_date])
        self.assertListEqual(list(actual_output.columns.names), ['Ticker', 'Price'])
        self.assertEqual(actual_output.index.name, 'Date')
