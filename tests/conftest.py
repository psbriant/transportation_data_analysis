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
            - AVG_RIDES: A subset of ridership data.

    """
    input_df = {
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': [2022, 2001, 2022, 2001],
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
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': [2022, 2001, 2022, 2001],
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
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': [2010, 2001, 2022, 2011],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday', 'Weekday', 'Weekday'],
        'AVG_RIDES': [812, 1076, 363, 312]
    }
    input_df1 = pd.DataFrame(input_df1)

    input_df2 = {
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': [2010, 2001, 2022, 2011],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday', 'Saturday', 'Saturday'],
        'AVG_RIDES': [266, 10760, 63, 712]
    }
    input_df2 = pd.DataFrame(input_df2)

    input_df3 = {
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': [2010, 2001, 2022, 2011],
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
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': [2022, 2001, 2022, 2001],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday', 'Weekday', 'Saturday'],
        'AVG_RIDES': [812, 1076, 363, 312],
        'RANK': [1.0, 1.0, 2.0, 2.0]
    }

    expected_rankings_df = pd.DataFrame(expected_rankings_df)
    return expected_rankings_df


@pytest.fixture
def expected_rankings_subset_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing whether
    datasets are ranked correctly by providing an expected test case for a
    general ranking by year limited by a specific number of values that get
    ranked.

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
    expected_rankings_subset_df = {
        'ROUTE': ['1', '97'],
        'YEAR': [2022, 2001],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Weekday', 'Sunday - Holiday'],
        'AVG_RIDES': [812, 1076],
        'RANK': [1.0, 1.0]
    }

    expected_rankings_subset_df = pd.DataFrame(expected_rankings_subset_df)
    return expected_rankings_subset_df


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
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': ['2022', '2001', '2022', '2001'],
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
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': ['2010', '2001', '2022', '2011'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday', 'Weekday', 'Weekday'],
        'AVG_RIDES': [812, 1076, 363, 312]
    }
    expected_df1 = pd.DataFrame(expected_df1)

    expected_df2 = {
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': ['2010', '2001', '2022', '2011'],
        'MONTH': ['October', 'January', 'October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday', 'Saturday', 'Saturday'],
        'AVG_RIDES': [266, 10760, 63, 712]
    }
    expected_df2 = pd.DataFrame(expected_df2)

    expected_df3 = {
        'ROUTE': ['1', '97', '100', 'X21'],
        'YEAR': ['2010', '2001', '2022', '2011'],
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
        'ROUTE': ['100', 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Weekday', 'Weekday'],
        'AVG_RIDES': [363, 312]
    }
    expected_subset_df1 = pd.DataFrame(expected_subset_df1)

    expected_subset_df2 = {
        'ROUTE': ['100', 'X21'],
        'YEAR': [2022, 2011],
        'MONTH': ['October', 'January'],
        'DAY_TYPE': ['Saturday', 'Saturday'],
        'AVG_RIDES': [63, 712]
    }
    expected_subset_df2 = pd.DataFrame(expected_subset_df2)

    expected_subset_df3 = {
        'ROUTE': ['100', 'X21'],
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


@pytest.fixture
def input_agg_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing aggregation
    functions.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.

    """
    input_agg_df = {
        'ROUTE': ['3', '3', '3', '3', '3', '3', '3', '3', '3'],
        'YEAR': [2011, 2011, 2011, 2011, 2011, 2011, 2010, 2010, 2010],
        'MONTH': ['February',
                  'February',
                  'January',
                  'January',
                  'January',
                  'January',
                  'December',
                  'December',
                  'December'],
        'DAY': [1, 2, 1, 2, 3, 4, 29, 30, 31],
        'DAY_TYPE': ['Weekday',
                     'Weekday',
                     'Saturday',
                     'Sunday - Holiday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday'],
        'AVG_RIDES': [691, 765, 107, 50, 419, 764, 800, 609, 1078]
    }
    input_agg_df = pd.DataFrame(input_agg_df)

    return input_agg_df


@pytest.fixture
def input_route_count_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing the
    get_route_count function.

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
    input_route_count_df = {
        'ROUTE': ['1',
                  '1',
                  '1',
                  '1',
                  '1',
                  '1',
                  '1',
                  '1',
                  '2',
                  '2',
                  '2',
                  '2',
                  '3',
                  '3'],
        'YEAR': [1999,
                 1999,
                 2000,
                 2000,
                 2001,
                 2001,
                 2002,
                 2002,
                 2000,
                 2000,
                 2001,
                 2001,
                 2001,
                 2001],
        'MONTH': ['January',
                  'February',
                  'January',
                  'February',
                  'January',
                  'February',
                  'January',
                  'February',
                  'January',
                  'February',
                  'January',
                  'February',
                  'January',
                  'February'],
        'DAY_TYPE': ['Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday',
                     'Weekday'],
        'AVG_RIDES': [812,
                      1076,
                      363,
                      312,
                      109,
                      333,
                      251,
                      691,
                      579,
                      273,
                      400,
                      910,
                      710,
                      234]
    }

    input_route_count_df = pd.DataFrame(input_route_count_df)
    return input_route_count_df


@pytest.fixture
def expected_month_agg_sum_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing sum
    aggregations by providing an expected test case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.

    """
    expected_month_agg_df = {
        'ROUTE': ['3', '3', '3', '3', '3'],
        'MONTH': ['December', 'February', 'January', 'January', 'January'],
        'YEAR': [2010, 2011, 2011, 2011, 2011],
        'DAY_TYPE': ['Weekday',
                     'Weekday',
                     'Saturday',
                     'Sunday - Holiday',
                     'Weekday'],
        'AVG_RIDES': [2487, 1456, 107, 50, 1183]
    }
    expected_month_agg_df = pd.DataFrame(expected_month_agg_df)

    return expected_month_agg_df


@pytest.fixture
def expected_year_agg_sum_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing sum
    aggregations by providing an expected test case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.

    """
    expected_year_agg_df = {
        'ROUTE': ['3', '3', '3', '3'],
        'YEAR': [2010, 2011, 2011, 2011],
        'DAY_TYPE': ['Weekday',
                     'Saturday',
                     'Sunday - Holiday',
                     'Weekday'],
        'AVG_RIDES': [2487, 107, 50, 2639]
    }
    expected_year_agg_df = pd.DataFrame(expected_year_agg_df)

    return expected_year_agg_df


@pytest.fixture
def expected_month_agg_mean_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing mean
    aggregations by providing an expected test case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.

    """
    expected_month_agg_df = {
        'ROUTE': ['3', '3', '3', '3', '3'],
        'MONTH': ['December', 'February', 'January', 'January', 'January'],
        'YEAR': [2010, 2011, 2011, 2011, 2011],
        'DAY_TYPE': ['Weekday',
                     'Weekday',
                     'Saturday',
                     'Sunday - Holiday',
                     'Weekday'],
        'AVG_RIDES': [829, 728, 107, 50, 591.5]
    }
    expected_month_agg_df = pd.DataFrame(expected_month_agg_df)

    return expected_month_agg_df


@pytest.fixture
def expected_year_agg_mean_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing mean
    aggregations by providing an expected test case.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.

    """
    expected_year_agg_df = {
        'ROUTE': ['3', '3', '3', '3'],
        'YEAR': [2010, 2011, 2011, 2011],
        'DAY_TYPE': ['Weekday',
                     'Saturday',
                     'Sunday - Holiday',
                     'Weekday'],
        'AVG_RIDES': [829, 107, 50, 659.75]
    }
    expected_year_agg_df = pd.DataFrame(expected_year_agg_df)

    return expected_year_agg_df


@pytest.fixture
def expected_day_type_split_dict() -> pd.DataFrame:
    """
    Creates a small dictionary of dataframes that can be used for testing
    dataframes split from larger dataframes based on the values of a specific
    column.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.
    """

    expected_day_type_split_dict = {
        'Weekday': pd.DataFrame({
            'ROUTE': ['1', '100'],
            'YEAR': [2022, 2022],
            'MONTH': ['October', 'October'],
            'DAY_TYPE': ['Weekday', 'Weekday'],
            'AVG_RIDES': [812, 363]}),
        'Sunday - Holiday': pd.DataFrame({
            'ROUTE': ['97'],
            'YEAR': [2001],
            'MONTH': ['January'],
            'DAY_TYPE': ['Sunday - Holiday'],
            'AVG_RIDES': [1076]}),
        'Saturday': pd.DataFrame({
            'ROUTE': ['X21'],
            'YEAR': [2001],
            'MONTH': ['January'],
            'DAY_TYPE': ['Saturday'],
            'AVG_RIDES': [312]})
    }

    return expected_day_type_split_dict


@pytest.fixture
def expected_month_split_dict() -> pd.DataFrame:
    """
    Creates a small dictionary of dataframes that can be used for testing
    dataframes split from larger dataframes based on the values of a specific
    column.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.
    """

    expected_month_split_dict = {
        'October': pd.DataFrame({
            'ROUTE': ['1', '100'],
            'YEAR': [2022, 2022],
            'MONTH': ['October', 'October'],
            'DAY_TYPE': ['Weekday', 'Weekday'],
            'AVG_RIDES': [812, 363]}),
        'January': pd.DataFrame({
            'ROUTE': ['97', 'X21'],
            'YEAR': [2001, 2001],
            'MONTH': ['January', 'January'],
            'DAY_TYPE': ['Sunday - Holiday', 'Saturday'],
            'AVG_RIDES': [1076, 312]})
    }

    return expected_month_split_dict


@pytest.fixture
def expected_route_split_dict() -> pd.DataFrame:
    """
    Creates a small dictionary of dataframes that can be used for testing
    dataframes split from larger dataframes based on the values of a specific
    column.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.

    """
    expected_route_split_dict = {
        '1': pd.DataFrame({
            'ROUTE': ['1'],
            'YEAR': [2022],
            'MONTH': ['October'],
            'DAY_TYPE': ['Weekday'],
            'AVG_RIDES': [812]}),
        '97': pd.DataFrame({
            'ROUTE': ['97'],
            'YEAR': [2001],
            'MONTH': ['January'],
            'DAY_TYPE': ['Sunday - Holiday'],
            'AVG_RIDES': [1076]}),
        '100': pd.DataFrame({
            'ROUTE': ['100'],
            'YEAR': [2022],
            'MONTH': ['October'],
            'DAY_TYPE': ['Weekday'],
            'AVG_RIDES': [363]}),
        'X21': pd.DataFrame({
            'ROUTE': ['X21'],
            'YEAR': [2001],
            'MONTH': ['January'],
            'DAY_TYPE': ['Saturday'],
            'AVG_RIDES': [312]})
    }

    return expected_route_split_dict


@pytest.fixture
def expected_year_split_dict() -> pd.DataFrame:
    """
    Creates a small dictionary of dataframes that can be used for testing
    dataframes split from larger dataframes based on the values of a specific
    column.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - ROUTE: A subset of bus route numbers.
            - YEAR: A subset of the years data was reported for.
            - MONTH: A subset of the months data was reported for.
            - DAY: A subset of the days data was reported for.
            - DAY_TYPE: Each of the types of days that data was reported for
                (Weekdays, Saturdays and Sunday Holidays).
            - AVG_RIDES: A subset of ridership data.

    NOTE: The ridership numbers used for this test dataset were created
        specifically for testing purposes instead of being taken from the
        actual CTA dataset.

    """
    expected_year_split_dict = {
        2022: pd.DataFrame({
            'ROUTE': ['1', '100'],
            'YEAR': [2022, 2022],
            'MONTH': ['October', 'October'],
            'DAY_TYPE': ['Weekday', 'Weekday'],
            'AVG_RIDES': [812, 363]}),
        2001: pd.DataFrame({
            'ROUTE': ['97', 'X21'],
            'YEAR': [2001, 2001],
            'MONTH': ['January', 'January'],
            'DAY_TYPE': ['Sunday - Holiday', 'Saturday'],
            'AVG_RIDES': [1076, 312]})
    }

    return expected_year_split_dict


@pytest.fixture
def expected_route_count_df() -> pd.DataFrame:
    """
    Creates a small dataframe of data that can be used for testing whether
    route counts have been generate correctly.

    Arguments:
        NONE

    Returns:
        Dataframe of generic test ridership data that includes the following:
            - YEAR: A subset of the years data was reported for.
            - COUNT: The number of bus routes in operation for each year.

    """
    expected_route_count_df = {
        'YEAR': [1999, 2000, 2001, 2002],
        'COUNT': [1, 2, 3, 1]
    }

    expected_route_count_df = pd.DataFrame(expected_route_count_df)
    return expected_route_count_df
