"""
Description: Functions for creating aggregate data
"""

import logging

import numpy as np
import pandas as pd


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
