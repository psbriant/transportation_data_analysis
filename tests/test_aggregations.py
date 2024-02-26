"""
Description: Tests for aggregation functions.
"""

import numpy as np
import pandas as pd
import pytest

from aggregations import aggregate_data


@pytest.mark.parametrize(
    "df,agg_cols,id_cols,agg_type,expected",
    [('input_agg_df',
      ['DAY'],
      ['ROUTE', 'MONTH', 'YEAR', 'DAY_TYPE'],
      'sum',
      'expected_month_agg_sum_df'),
     ('input_agg_df',
      ['DAY', 'MONTH'],
      ['ROUTE', 'YEAR', 'DAY_TYPE'],
      'sum',
      'expected_year_agg_sum_df'),
     ('input_agg_df',
      ['DAY'],
      ['ROUTE', 'MONTH', 'YEAR', 'DAY_TYPE'],
      'mean',
      'expected_month_agg_mean_df'),
     ('input_agg_df',
      ['DAY', 'MONTH'],
      ['ROUTE', 'YEAR', 'DAY_TYPE'],
      'mean',
      'expected_year_agg_mean_df')])
def test_aggregate_data(
        df: pd.DataFrame,
        agg_cols: list[str],
        id_cols: list[str],
        agg_type: str,
        expected: pd.DataFrame,
        request) -> pd.DataFrame:
    """
    Tests the following:
    1. Sum aggregation by month
    2. Sum aggregation by year
    3. Mean aggregation by month
    4. Mean aggregation by year

    Arguments:
        df (DataFrame): Pandas dataframe to aggregate.
        agg_cols (strList): The column to aggregate the data by.
        id_cols (strList): The columns representing non-aggregated dimensions.
        agg_type (str): The type of aggregation to perform on the data. Must
            be one of either 'sum' or 'mean'.
        expected (DataFrame): Dataframe with the expected result of
            aggregating the dataframe by specified dimensions.
        request: A special fixture used to provide information regarding the
            requesting test function. This is used to retrieve the value of
            fixtures used in parameterized tests.

    Returns:
        NONE
    """

    df = request.getfixturevalue(df)
    expected = request.getfixturevalue(expected)

    test_df = aggregate_data(
        df=df,
        agg_cols=agg_cols,
        id_cols=id_cols,
        agg_type=agg_type)

    pd.testing.assert_frame_equal(test_df, expected)


@pytest.mark.parametrize(
    "df,agg_cols,id_cols,agg_type",
    [('input_agg_df',
      ['DAY'],
      ['ROUTE', 'MONTH', 'YEAR', 'DAY_TYPE'],
      'Sum'),
     ('input_agg_df',
      ['DAY'],
      ['ROUTE', 'MONTH', 'YEAR', 'DAY_TYPE'],
      'MEAN'),
     ('input_agg_df',
      ['DAY'],
      ['ROUTE', 'MONTH', 'YEAR', 'DAY_TYPE'],
      'median')])
def test_aggregate_data_value_exceptions(
        df: pd.DataFrame,
        agg_cols: list[str],
        id_cols: list[str],
        agg_type: str,
        request) -> pd.DataFrame:
    """
    Tests the following:
    1. Tests whether ValueErrors are raised if agg_type is not one of 'sum' or
        'mean'.

    Arguments:
        df (DataFrame): Pandas dataframe to aggregate.
        agg_cols (strList): The column to aggregate the data by.
        id_cols (strList): The columns representing non-aggregated dimensions.
        agg_type (str): The type of aggregation to perform on the data. Must
            be one of either 'sum' or 'mean'.
        request: A special fixture used to provide information regarding the
            requesting test function. This is used to retrieve the value of
            fixtures used in parameterized tests.

    Returns:
        NONE

    """
    df = request.getfixturevalue(df)

    with pytest.raises(ValueError):
        aggregate_data(
            df=df,
            agg_cols=agg_cols,
            id_cols=id_cols,
            agg_type=agg_type)
