"""
Description: Functions for preparing data for plotting.
"""

import logging

import numpy as np
import pandas as pd


def create_absolute_file_paths(
        file_list: list[str],
        file_path: str) -> list[str] | str:
    """

    Arguments:
        file_list (strList): List of files to join with a specified absolute
            path.
        file_path (str): The file path to join the files specified in
        'file_list' to.

    Returns:
        Either a list of absolute file paths or a single absolute file
        path depending on the length of file_list.

    Raises:
        TypeError if the value of the 'file_list' argument  is not a list.
        TypeError if the value of the file_path is not a string.
    """

    # Confirm values for 'file_list' are not strings and 'file_path' are not
    # lists.
    if type(file_list) is not list:
        raise TypeError("The value of 'file_list' should be a list")

    if type(file_path) is not str:
        raise TypeError("The value of 'file_path' should be a string")

    abs_file_paths = []

    for file_name in file_list:
        logging.info(
            f'Joining file path {file_path} with file {file_name}')
        abs_path = f'{file_path}{file_name}'
        abs_file_paths.append(abs_path)

    # Return either a list of file paths or a single file path.
    if len(abs_file_paths) > 1:
        return abs_file_paths
    else:
        return abs_file_paths[0]


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

        updated_df = df.copy()
        updated_df[col] = updated_df[col].astype(datatype)
        updated_dfs.append(updated_df)

    # Return either a list of dataframes or a single dataframe.
    if len(updated_dfs) > 1:
        return updated_dfs
    else:
        return updated_dfs[0]
