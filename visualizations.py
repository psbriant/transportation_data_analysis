"""
Project: Transportation data analysis
Description:
TBD
"""

import logging

import altair as alt
import numpy as np
import pandas as pd


def create_heatmap(
    data: pd.DataFrame,
    output_path: str,
    x_value: str,
    y_value: str,
    color_values: str,
    facet_values: str,
    facet_columns: int) -> None:
    """
    Create a heatmap for specified data and columns.

    TODO: Figure out how to best set up kwargs for pandas and seaborn
    functions.
    TODO: Figure out what type hints would look like for a list of strings.

    Arguments:
        data (DataFrame): Input data to visualize.
        output_path (str): Absolute file path (including the name of the file)
            to save the heatmap to.
        x_value (str): The name of the column representing the x-axis of the
            heatmap.
        y_value (str): The name of the column representing the y-axis of the
            heatmap.
        color_values (str): The name of column representing the values to
            plot.
        facet_values (str): The name of the column representing the values to
            create a facet grid of plots for.
        facet_columns (int): The number of columns the facet grid will
            contain.

    Returns:
        None

    Raises:
        None
    """

    data = data.copy()

    chart = alt.Chart(data).mark_rect().encode(
        alt.X(x_value, type='ordinal'),
        alt.Y(y_value, type='ordinal'),
        alt.Color(color_values, type='quantitative'),
        alt.Facet(facet_values,
                  type='ordinal',
                  columns=facet_columns),
        stroke = alt.value('black'),
        strokeWidth = alt.value(0.2),
    )

    chart.save(output_path)

