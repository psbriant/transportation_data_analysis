"""
Description: Functions for preparing data for plotting.
"""

import logging

import numpy as np
import pandas as pd


def change_column_datatype(
        df_list: list[pd.DataFrame],
        col: str,
        datatype: str) -> list[pd.DataFrame] | pd.DataFrame:
    """
    Changes the datatype of values for a specified column from the current
    datatype to the specified new datatype.

    Arguments:
        df_list (DataFrame): List of pandas dataframes containing the columns
            to update.
        col (str): The column to change the datatype for. Please note that the
            value of this argument should not be a list of different strings.
        datatype (str): The datatype to update to. Please note that the
            value of this argument should not be a list of different datatypes.

    Returns:
        Either a list of pandas dataframes containing the updated column for
        each dataframe (if a list of multiple dataframes were specified for
        the 'df_list' argument) or a single dataframe containing the updated
        column (if a list containing a single dataframe was specified for
        the 'df_list' argument).

    Raises:
        TypeError if the value of argument 'col' is not a string.
        TypeError if the value of argument 'datatype' is not a string.
    """

    # Confirm values for 'col' and 'datatype' are not lists.
    if type(col) is not str:
        raise TypeError("The value of 'col' should be a string")

    if type(datatype) is not str:
        raise TypeError("The value of 'datatype' should be a string")

    updated_dfs = []

    logging.info(
        f'Changing the data type of values in {col} to the type {datatype}')
    for df in df_list:

        if type(df) is not pd.core.frame.DataFrame:
            raise TypeError("The value of 'df' should be a pandas "
                            "dataframe")

        updated_df = df.copy()
        updated_df[col] = updated_df[col].astype(datatype)
        updated_dfs.append(updated_df)

    # Return either a list of dataframes or a single dataframe.
    if len(updated_dfs) > 1:
        return updated_dfs
    else:
        return updated_dfs[0]


def create_rankings(
        df: pd.DataFrame,
        value_col: str,
        rank_col: str,
        group_col: list[str],
        num_rankings: int = 0) -> pd.DataFrame:
    """
    Ranks rows in a dataframe by a specified column.

    Arguments:
        df (DataFrame): Dataset to develop rankings for.
        value_col (str): The name of the column rankings will be based off of.
        rank_col (str): The name of a new column that will contain the
            numerical rankings. This column should not already exist in the
            input Dataframe.
        group_col (strList): The columns used for ensuring rankings are made
            across columns (e.g. specifying the year column in a dataset
            containing bus routes, ridership numbers and years will rank each
            bus route by ridership for each year).
        num_rankings (int): The number of rows to return rankings for. If set
            to zero, no limit will be applied and all rows will be ranked.
            Defaults to zero.

    Returns:
        Dataframe with numerical rankings for each row.

    Raises:
        ValueError if the value of argument 'num_rankings' is greater than the
            number of unique values in 'value_col'.
        ValueError if there is already a column named 'rank_col' in 'df'.
        ValueError if 'rank_col' has the same value as 'value_col'.
    """

    if rank_col in df.columns:
        raise ValueError("rank_col should be a new column")
    if value_col == rank_col:
        raise ValueError(
            "value_col and rank_col should not be the same value")

    rank_df = df.copy()

    # Add a rank column based off of the value of value_col.
    rank_df[rank_col] = rank_df.groupby(group_col)[
        value_col].rank(ascending=False)

    # Subset dataframe by the value of limit. Do not specify if set to zero.
    if num_rankings > len(rank_df[rank_col].unique()):
        raise ValueError(
            "The value of num_rankings should not be greater than the number "
            "of unique values in the value_col")
    if num_rankings > 0:
        rank_df = rank_df[rank_df[rank_col] <= num_rankings]

    return rank_df


def subset_dataframes_by_value(
        dfs: list[pd.DataFrame],
        operator: list[str],
        target_col: list[str],
        filter_val: list) -> list[pd.DataFrame] | pd.DataFrame:
    """
    Subset a dataframe or list of dataframes based on a specific condition.

    Arguments:
        dfs (DataFrameList): List of dataframes to subset.
        operator (strlist): The operations to preform to execute the subset
            (e.g. '>=', '==', '<=' or '!=').
        target_col (strlist): The name of the columns to subset the dataframe
            by.
        filter_val (list): List of specific values to subset the dataframe
            by.

    Returns:
        Dataframe or list of dataframes with subsetted estimates.

    Raises:
        ValueError if operator, target_col and filter_val are not the same
            length.
    """

    # Ensure elements of the query statement are of the same length
    if len(operator) == len(target_col) == len(filter_val):

        # Build query statement
        sub_queries = []

        for op, tc, fv in zip(operator, target_col, filter_val):
            sub_query = f"{tc} {op} {fv}"
            sub_queries.append(sub_query)
        query_statement = ' & '.join(sub_queries)

        # Subset dataframes
        filtered_dfs = []

        for df in dfs:

            sub_df = df.copy()
            sub_df = sub_df.query(query_statement)
            filtered_dfs.append(sub_df)

        if len(filtered_dfs) == 1:
            filtered_dfs = filtered_dfs[0]

        return filtered_dfs

    else:

        raise ValueError(
            "The variables 'operator', 'target_col', and 'filter_val' must be "
            "the same length")


def aggregate_data(
        df: pd.DataFrame,
        agg_cols: list[str],
        id_cols: list[str],
        agg_type: str) -> pd.DataFrame:
    """
    # Create aggregate ridership data by route, year for each service type

    Arguments:
        df (DataFrame): Pandas dataframe to aggregate.
        agg_cols (strList): The column to aggregate the data by.
        id_cols (strList): The columns representing non-aggregated dimensions.
        agg_type (str): The type of aggregation to perform on the data. Must
            be one of either 'sum' or 'mean'.

    Returns:
        Dataframe that has been aggregated by the specified dimensions.

    Raises:
        ValueError if agg_type is not one of 'sum' or 'mean'.
    """

    agg_df = df.copy()
    agg_df = agg_df.drop(columns=agg_cols)

    if agg_type == 'sum':
        agg_df = agg_df.groupby(by=id_cols).sum()

    elif agg_type == 'mean':
        agg_df = agg_df.groupby(by=id_cols).mean()

    else:
        raise ValueError(
            f"Unsupported agg_type of {agg_type}, please use either 'sum' "
            f"or 'mean'")

    agg_df = agg_df.reset_index()

    return agg_df
