"""
Description: File for storing testing configurations including fixtures that
can be reused across all test scripts.
"""

import numpy as np
import pandas as pd
import pytest

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
            - RIDES: A subset of ridership data.

    """
    input_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2022, 1999, 2022, 1999],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'RIDES': [812, 1076, 363, 312]
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
            - RIDES: A subset of ridership data.

    """
    input_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2022, 1999, 2022, 1999],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'RIDES': [812, 1076, 363, 312]
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
            - RIDES: A subset of ridership data.

    """
    input_df1 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2010, 1999, 2022, 2011],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday', 'Weekday', 'Weekday'],
        'RIDES': [812, 1076, 363, 312]
    }
    input_df1 = pd.DataFrame(input_df1)

    input_df2 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2010, 1999, 2022, 2011],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday', 'Saturday', 'Saturday'],
        'RIDES': [266, 10760, 63, 712]
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
        'RIDES': [1000, 93, 234, 312]
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
            - RIDES: A subset of ridership data.
            - RANK: A subset of ridership rankings for specified parameters.
                In this case, they are by year meaning every year will have
                its own rankings.

    """
    expected_rankings_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': [2022, 1999, 2022, 1999],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'RIDES': [812, 1076, 363, 312],
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
            - RIDES: A subset of ridership data.

    """
    expected_updated_type_df = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': ['2022', '1999', '2022', '1999'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'RIDES': [812, 1076, 363, 312]
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
            - RIDES: A subset of ridership data.

    """
    expected_df1 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': ['2010', '1999', '2022', '2011'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday', 'Weekday', 'Weekday'],
        'RIDES': [812, 1076, 363, 312]
    }
    expected_df1 = pd.DataFrame(expected_df1)

    expected_df2 = {
        'ROUTE': [1, 97, 100, 'X21'],
        'YEAR': ['2010', '1999', '2022', '2011'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday', 'Saturday', 'Saturday'],
        'RIDES': [266, 10760, 63, 712]
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
        'RIDES': [1000, 93, 234, 312]
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
            - RIDES: A subset of ridership data.

    """
    expected_subset_df1 = {
        'ROUTE': [100, 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday'],
        'RIDES': [363, 312]
    }
    expected_subset_df1 = pd.DataFrame(expected_subset_df1)

    expected_subset_df2 = {
        'ROUTE': [100, 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday'],
        'RIDES': [63, 712]
    }
    expected_subset_df2 = pd.DataFrame(expected_subset_df2)

    expected_subset_df3 = {
        'ROUTE': [100, 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Sunday - Holiday', 'Sunday - Holiday'],
        'RIDES': [234, 312]
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
            - RIDES: A subset of ridership data.

    """
    expected_subset_df1 = {
        'ROUTE': [1, 'X21'],
        'YEAR': [2010, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday'],
        'RIDES': [812, 312]
    }
    expected_subset_df1 = pd.DataFrame(expected_subset_df1)

    expected_subset_df2 = {
        'ROUTE': [1, 'X21'],
        'YEAR': [2010, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday'],
        'RIDES': [266, 712]
    }
    expected_subset_df2 = pd.DataFrame(expected_subset_df2)

    expected_subset_df3 = {
        'ROUTE': [1, 'X21'],
        'YEAR': [2010, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Sunday - Holiday', 'Sunday - Holiday'],
        'RIDES': [1000, 312]
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
            - RIDES: A subset of ridership data.

    """
    expected_subset_df1 = {
        'ROUTE': ['X21'],
        'YEAR': [2011],
        'MONTH': ['January'],
        'DAY_TYPE': ['Weekday'],
        'RIDES': [312]
    }
    expected_subset_df1 = pd.DataFrame(expected_subset_df1)

    expected_subset_df2 = {
        'ROUTE': ['X21'],
        'YEAR': [2011],
        'MONTH': ['January'],
        'DAY_TYPE': ['Saturday'],
        'RIDES': [712]
    }
    expected_subset_df2 = pd.DataFrame(expected_subset_df2)

    expected_subset_df3 = {
        'ROUTE': ['X21'],
        'YEAR': [2011],
        'MONTH': ['January'],
        'DAY_TYPE': ['Sunday - Holiday'],
        'RIDES': [312]
    }
    expected_subset_df3 = pd.DataFrame(expected_subset_df3)

    expected_subset_dfs = [expected_subset_df1,
                           expected_subset_df2,
                           expected_subset_df3]

    return expected_subset_dfs
