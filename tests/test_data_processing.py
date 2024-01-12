"""
Description: Tests for data processing functions.
"""

import numpy as np
import pandas as pd
import pytest

from data_processing import (aggregate_data,
                             change_column_datatype,
                             create_rankings,
                             subset_dataframes_by_value)


@pytest.mark.parametrize(
    "df_list,col,datatype,expected",
    [('input_updated_type_df', 'YEAR', 'str', 'expected_updated_type_df'),
     ('input_dfs',
      'YEAR',
      'str',
      'expected_updated_type_dfs')])
def test_change_column_datatype(
    df_list: list[pd.DataFrame],
    col: str,
    datatype: str,
    expected: pd.DataFrame,
    request) -> list[pd.DataFrame] | pd.DataFrame:
    """
    Tests the following:
    1. Tests whether the column data type has changed.

    Arguments:
        df_list (DataFrame): List of pandas dataframes containing the columns
            to update.
        col (str): The column to change the datatype for. Please note that the
            value of this argument should not be a list of different strings.
        datatype (str): The datatype to update to. Please note that the
            value of this argument should not be a list of different datatypes.
        expected (DataFrame): Dataframe with the expected
            result of changing the datatype of an expected column.
        request: A special fixture used to provide information regarding the
            requesting test function. This is used to retrieve the value of
            fixtures used in parameterized tests.

    Returns:
        NONE

    """
    df_list = request.getfixturevalue(df_list)
    expected = request.getfixturevalue(expected)

    test_type_updates = change_column_datatype(
        df_list=df_list,
        col=col,
        datatype=datatype)

    if len(df_list) == 1:
        assert test_type_updates.equals(expected)

    else:
        for i in range(len(test_type_updates)):
            test_case = test_type_updates[i
            ].reset_index(drop=True)

            assert test_case.equals(expected[i])


@pytest.mark.parametrize(
    "df,value_col,rank_col,group_col,num_rankings,expected",
    [('input_df', 'AVG_RIDES', 'RANK', ['YEAR'], 0, 'expected_rankings_df')])
def test_create_rankings(
        df: pd.DataFrame,
        value_col: str,
        rank_col: str,
        group_col: list[str],
        num_rankings: int,
        expected: pd.DataFrame,
        request) -> pd.DataFrame:
    """
    Tests the following:
    1. Tests whether rankings were correctly executed.

    Arguments:
        df (DataFrame): Dataset to develop rankings for.
        value_col (str): The name of the column rankings will be based off of.
        rank_col (str): The name of the column containing the numerical
            rankings.
        group_col (strList): The columns used for ensuring rankings are made
            across columns (e.g. specifying the year column in a dataset
            containing bus routes, ridership numbers and years will rank each
            bus route by ridership for each year).
        num_rankings (int): The number of rows to return rankings for. If set
            to zero, no limit will be applied and all rows will be ranked.
        expected (DataFrame): Dataframe with the expected
            result of creating rankings.
        request: A special fixture used to provide information regarding the
            requesting test function. This is used to retrieve the value of
            fixtures used in parameterized tests.

    Returns:
        NONE

    """
    df = request.getfixturevalue(df)
    expected = request.getfixturevalue(expected)

    test_rankings = create_rankings(
        df=df,
        value_col=value_col,
        rank_col=rank_col,
        group_col=group_col,
        num_rankings=num_rankings)

    assert test_rankings.equals(expected)


@pytest.mark.parametrize(
    "dfs,operator,target_col,filter_val,expected",
    [('input_dfs', ['>='], ['YEAR'], [2011], 'expected_subset_dfs_gtet'),
     ('input_dfs',
      ['>', '<'],
      ['YEAR', 'YEAR'],
      [2009, 2020],
      'expected_subset_dfs_gtalt'),
     ('input_dfs', ['=='], ['YEAR'], [2011], 'expected_subset_dfs_et')])
def test_subset_dataframes_by_value(
        dfs: list[pd.DataFrame],
        operator: list[str],
        target_col: list[str],
        filter_val: list,
        expected: list[pd.DataFrame],
        request) -> list[pd.DataFrame]:
    """
    Tests the following:
    1. Whether a list of dataframes were correctly subsetted by a specified
        condition.

    Arguments:
        dfs (DataFrameList): List of dataframes to subset.
        operator (strlist): The operations to preform to execute the subset
            (e.g. '>=', '==', '<=' or '!=').
        target_col (strlist): The name of the columns to subset the dataframe
            by.
        filter_val (list): List of specific values to subset the dataframe
            by.
        expected (DataFrameList): List of dataframes with the
            expected result of subsetting the dataframe.
        request: A special fixture used to provide information regarding the
            requesting test function. This is used to retrieve the value of
            fixtures used in parameterized tests.

    Returns:
        NONE

    """
    dfs = request.getfixturevalue(dfs)
    expected = request.getfixturevalue(expected)
    test_dfs = subset_dataframes_by_value(
        dfs=dfs,
        operator=operator,
        target_col=target_col,
        filter_val=filter_val)

    for i in range(len(test_dfs)):
        test_case = test_dfs[i].reset_index(drop=True)

        assert test_case.equals(expected[i])
