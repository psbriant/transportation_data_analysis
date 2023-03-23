"""
Project: Transportation data analysis
Description:
TBD
"""

import logging

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def create_heatmap(
        data: pd.DataFrame,
        output_path: str,
        data_index: str,
        data_columns: str,
        data_values: str) -> None:
    """
    Create a heatmap for specified data and columns.

    TODO: Figure out how to best set up kwargs for pandas and seaborn
    functions.
    TODO: Figure out what type hints would look like for a list of strings.

    Arguments:
        data (DataFrame): Input data to visualize.
        output_path (str): Absolute file path (including the name of the file)
            to save the heatmap to.
        data_index (strList): Column to use to make new frame's index.
        data_columns (strList): List of columns to use to make new frame's
            columns.
        data_values (strList): Columns to use for populating new frame's
            values. If not specified, all remaining columns will be used and
            the result will have hierarchically indexed columns.

    Returns:
        None

    Raises:
        None
    """

    data = data.copy()

    # TODO: determine where this should be set or whether this needs to be set
    #  at all.
    sns.set_theme()

    # Convert data to long-form for plotting
    data_long = data.pivot(
        index=data_index,
        columns=data_columns,
        values=data_values)

    # Create a heatmap with the numeric values in each cell
    # TODO: Add logging for specific dimensions being plotted
    # TODO: Eventually move hardcoded arguments to constants.
    f, ax = plt.subplots(figsize=(18, 12))
    hm = sns.heatmap(data_long, annot=True, fmt='g', linewidths=.5, ax=ax)
    fig = hm.get_figure()
    fig.savefig(output_path)
