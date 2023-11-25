"""
Description: Tests for data processing functions.
"""

import numpy as np
import pandas as pd
import pytest

from data_processing import (change_column_datatype,
                             create_rankings,
                             subset_dataframes_by_value)


@pytest.fixture
def input_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing data
    processing functions.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    input_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2022, 1999, 2022, 1999],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'AVG_RIDES': [812, 1076, 363, 312]
    }

    input_df = pd.DataFrame(input_df)
    return input_df


@pytest.fixture
def input_updated_type_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing data
    whether column datatypes are correctly updated

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    input_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2022, 1999, 2022, 1999],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'AVG_RIDES': [812, 1076, 363, 312]
    }

    input_df = pd.DataFrame(input_df)

    input_updated_type_df = []
    input_updated_type_df.append(input_df)

    return input_updated_type_df


@pytest.fixture
def input_dfs() -> list[pd.DataFrame]:
    """
    Creates a small dataframe of data that can be used for testing data
    processing functions.

    Arguments:
        NONE

    Returns:
        List of dataframes containing generic ridership data including the
            following:

            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    input_df1 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2010, 1999, 2022, 2011],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday', 'Weekday', 'Weekday'],
        'AVG_RIDES': [812, 1076, 363, 312]
    }
    input_df1 = pd.DataFrame(input_df1)

    input_df2 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2010, 1999, 2022, 2011],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday', 'Saturday', 'Saturday'],
        'AVG_RIDES': [266, 10760, 63, 712]
    }
    input_df2 = pd.DataFrame(input_df2)

    input_df3 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2010, 1999, 2022, 2011],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Sunday - Holiday',
                     'Sunday - Holiday',
                     'Sunday - Holiday',
                     'Sunday - Holiday'],
        'AVG_RIDES': [1000, 93, 234, 312]
    }
    input_df3 = pd.DataFrame(input_df3)

    input_dfs = [input_df1, input_df2, input_df3]

    return input_dfs


@pytest.fixture
def expected_rankings_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing whether
    datasets are ranked correctly by providing an expected test case for a
    general ranking by year.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.
            - RANK: A subset of ridership rankings for specified parameters.
                In this case, they are by year meaning every year will have
                its own rankings.

    """
    expected_rankings_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2022, 1999, 2022, 1999],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'AVG_RIDES': [812, 1076, 363, 312],
        'RANK': [1.0, 1.0, 2.0, 2.0]
    }

    expected_rankings_df = pd.DataFrame(expected_rankings_df)
    return expected_rankings_df


@pytest.fixture
def expected_updated_type_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing whether
    column types have been correctly altered by providing an expected test
    case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    expected_updated_type_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': ['2022', '1999', '2022', '1999'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'AVG_RIDES': [812, 1076, 363, 312]
    }

    expected_updated_type_df = pd.DataFrame(expected_updated_type_df)
    return expected_updated_type_df


@pytest.fixture
def expected_updated_type_dfs() -> list[pd.DataFrame]:
    """
    Creates a small list of dataframes that can be used for testing whether
    column types have been correctly altered by providing an expected test
    case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    expected_df1 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': ['2010', '1999', '2022', '2011'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday', 'Weekday', 'Weekday'],
        'AVG_RIDES': [812, 1076, 363, 312]
    }
    expected_df1 = pd.DataFrame(expected_df1)

    expected_df2 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': ['2010', '1999', '2022', '2011'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday', 'Saturday', 'Saturday'],
        'AVG_RIDES': [266, 10760, 63, 712]
    }
    expected_df2 = pd.DataFrame(expected_df2)

    expected_df3 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': ['2010', '1999', '2022', '2011'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Sunday - Holiday',
                     'Sunday - Holiday',
                     'Sunday - Holiday',
                     'Sunday - Holiday'],
        'AVG_RIDES': [1000, 93, 234, 312]
    }
    expected_df3 = pd.DataFrame(expected_df3)

    expected_dfs = [expected_df1, expected_df2, expected_df3]

    return expected_dfs


@pytest.fixture
def expected_subset_dfs_gtet() -> list[pd.DataFrame]:
    """
    Creates a small dataframe of data that can be used for testing whether
    a list of dataframes have been correctly subsetted by providing an
    expected test case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    expected_subset_df1 = {
        'ROUTE': [100, 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday'],
        'AVG_RIDES': [363, 312]
    }
    expected_subset_df1 = pd.DataFrame(expected_subset_df1)

    expected_subset_df2 = {
        'ROUTE': [100, 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday'],
        'AVG_RIDES': [63, 712]
    }
    expected_subset_df2 = pd.DataFrame(expected_subset_df2)

    expected_subset_df3 = {
        'ROUTE': [100, 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Sunday - Holiday', 'Sunday - Holiday'],
        'AVG_RIDES': [234, 312]
    }
    expected_subset_df3 = pd.DataFrame(expected_subset_df3)

    expected_subset_dfs = [expected_subset_df1,
                           expected_subset_df2,
                           expected_subset_df3]

    return expected_subset_dfs


@pytest.fixture
def expected_subset_dfs_gtalt() -> list[pd.DataFrame]:
    """
    Creates a small dataframe of data that can be used for testing whether
    a list of dataframes have been correctly subsetted by providing an
    expected test case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    expected_subset_df1 = {
        'ROUTE': [1, 'X21'],
        'YEAR': [2010, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday'],
        'AVG_RIDES': [812, 312]
    }
    expected_subset_df1 = pd.DataFrame(expected_subset_df1)

    expected_subset_df2 = {
        'ROUTE': [1, 'X21'],
        'YEAR': [2010, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday'],
        'AVG_RIDES': [266, 712]
    }
    expected_subset_df2 = pd.DataFrame(expected_subset_df2)

    expected_subset_df3 = {
        'ROUTE': [1, 'X21'],
        'YEAR': [2010, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Sunday - Holiday', 'Sunday - Holiday'],
        'AVG_RIDES': [1000, 312]
    }
    expected_subset_df3 = pd.DataFrame(expected_subset_df3)

    expected_subset_dfs = [expected_subset_df1,
                           expected_subset_df2,
                           expected_subset_df3]

    return expected_subset_dfs


@pytest.fixture
def expected_subset_dfs_et() -> list[pd.DataFrame]:
    """
    Creates a small dataframe of data that can be used for testing whether
    a list of dataframes have been correctly subsetted by providing an
    expected test case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    """
    expected_subset_df1 = {
        'ROUTE': ['X21'],
        'YEAR': [2011],
        'MONTH': ['January'],
        'DAY_TYPE': ['Weekday'],
        'AVG_RIDES': [312]
    }
    expected_subset_df1 = pd.DataFrame(expected_subset_df1)

    expected_subset_df2 = {
        'ROUTE': ['X21'],
        'YEAR': [2011],
        'MONTH': ['January'],
        'DAY_TYPE': ['Saturday'],
        'AVG_RIDES': [712]
    }
    expected_subset_df2 = pd.DataFrame(expected_subset_df2)

    expected_subset_df3 = {
        'ROUTE': ['X21'],
        'YEAR': [2011],
        'MONTH': ['January'],
        'DAY_TYPE': ['Sunday - Holiday'],
        'AVG_RIDES': [312]
    }
    expected_subset_df3 = pd.DataFrame(expected_subset_df3)

    expected_subset_dfs = [expected_subset_df1,
                           expected_subset_df2,
                           expected_subset_df3]

    return expected_subset_dfs


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
