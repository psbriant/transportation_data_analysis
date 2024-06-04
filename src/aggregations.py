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


def get_route_count(
        df: pd.DataFrame,
        route_dims: list[str],
        count_dim: list[str],
        count_col: str) -> pd.DataFrame:
    """
    Create a count of the number of bus routes by a specified set of
    dimensions (e.g. year).

    Arguments:
        df (DataFrame): Pandas dataframe to create counts for.
        route_dims (strList): The columns required for counting the number of
            bus routes.
        count_dim (str): The column used for creating dimension specific
            counts.
        count_col (str): The name of the column that will contain the number
            bus routes.

    Returns:
        Dataframe of the number of bus routes by a specified dimension.

    Raises:
        NONE
    """

    route_count = df.copy()

    # Remove columns not involved in counting the number of bus routes.
    route_count = route_count[route_dims]
    route_count = route_count.drop_duplicates().reset_index(drop=True)

    # Create a count of the number of bus routes by specified dimensions
    route_count[count_col] = route_count.groupby(
        count_dim)[count_dim].transform('count')
    route_count = route_count[[count_dim, count_col]]
    route_count = route_count.drop_duplicates().reset_index(drop=True)

    return route_count
