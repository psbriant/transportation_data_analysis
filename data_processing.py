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
            raise TypeError("The type of 'col' should be a pandas "
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
        rank_col (str): The name of the column containing the numerical
            rankings.
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
        NONE
    """

    rank_df = df.copy()

    # Add a rank column based off of the value of value_col.
    rank_df[rank_col] = rank_df.groupby(group_col)[
        value_col].rank(ascending=False)

    # Subset dataframe by the value of limit. Do not specify if set to zero.
    if num_rankings > 0:
        rank_df = rank_df[rank_df[rank_col] <= num_rankings]

    return rank_df
