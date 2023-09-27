"""
Project: Transportation data analysis
Description:
TBD
"""

import logging

from data_processing import (create_rankings)

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
    facet_columns: int,
    x_axis_sort_order: list[str],
    scheme: str,
    x_value_type: str,
    y_value_type: str) -> None:
    """
    Create a heatmap for specified data and columns.

    TODO: Figure out how to best set up kwargs for pandas and altair functions

    Arguments:
        data (DataFrame): Input data to visualize.
        output_path (str): Absolute file path (including the name of the file)
            to save the plot to.
        x_value (str): The name of the column representing the x-axis.
        y_value (str): The name of the column representing the y-axis.
        color_values (str): The name of column representing the values to
            plot.
        facet_values (str): The name of the column representing the values to
            create a facet grid of plots for.
        facet_columns (int): The number of columns the facet grid will
            contain.
        x_axis_sort_order (strList): A list of strings representing the order
            of values on the x-axis.
        scheme (str): The color scheme to use. Please refer to the full
            gallery of available color schemes at
            https://vega.github.io/vega/docs/schemes/
        x_value_type (str): The type of data that will be plotted on the
            x-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
        y_value_type (str): The type of data that will be plotted on the
            y-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.

    Returns:
        None

    Raises:
        None
    """

    data = data.copy()

    chart = alt.Chart(data).mark_rect().encode(
        alt.X(x_value, type=x_value_type, sort=x_axis_sort_order),
        alt.Y(y_value, type=y_value_type),
        alt.Color(color_values,
                  type='quantitative',
                  scale=alt.Scale(scheme=scheme)),
        alt.Facet(facet_values,
                  type='ordinal',
                  columns=facet_columns),
        stroke = alt.value('black'),
        strokeWidth = alt.value(0.2),
    )

    chart.save(output_path)


def create_barchart(
        data: pd.DataFrame,
        output_path: str,
        x_value: str,
        y_value: str,
        color_values: str,
        title: str,
        scheme: str,
        x_value_type: str,
        y_value_type: str,
        sort_order: str | list[str] = 'ascending') -> None:
    """
    Create a bar chart for specified data and columns.

    Arguments:
        data (DataFrame): Input data to visualize.
        output_path (str): Absolute file path (including the name of the file)
            to save the plot to.
        x_value (str): The name of the column representing the x-axis.
        y_value (str): The name of the column representing the y-axis.
        color_values (str): The name of column representing the values to
            plot.
        title (str): The title of the plot.
        scheme (str): The color scheme to use. Please refer to the full
            gallery of available color schemes at
            https://vega.github.io/vega/docs/schemes/
        x_value_type (str): The type of data that will be plotted on the
            x-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
        y_value_type (str): The type of data that will be plotted on the
            y-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
        sort_order (str or strlist): The sort order. One of "ascending",
            "descending", or a list of strings containing a custom order.
            Defaults to ascending.

    Returns:
        None

    Raises:
        None
    """

    chart = alt.Chart(data).mark_bar().encode(
        alt.X(x_value, type=x_value_type),
        alt.Y(y_value, type=y_value_type),
        alt.Color(color_values,
                  sort=sort_order,
                  scale=alt.Scale(scheme=scheme)),
    ).properties(title=title)

    chart.save(output_path)


def create_linechart(
        data: pd.DataFrame,
        output_path: str,
        x_value: str,
        y_value: str,
        color_values: str,
        title: str,
        scheme: str,
        x_value_type: str,
        y_value_type: str) -> None:
    """
    Create a line chart for specified data and columns.

    Arguments:
        data (DataFrame): Input data to visualize.
        output_path (str): Absolute file path (including the name of the file)
            to save the plot to.
        x_value (str): The name of the column representing the x-axis.
        y_value (str): The name of the column representing the y-axis.
        color_values (str): The name of column representing the values to
            plot.
        title (str): The title of the plot.
        scheme (str): The color scheme to use. Please refer to the full
            gallery of available color schemes at
            https://vega.github.io/vega/docs/schemes/
        x_value_type (str): The type of data that will be plotted on the
            x-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
        y_value_type (str): The type of data that will be plotted on the
            y-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.

    Returns:
        None

    Raises:
        None
    """

    chart = alt.Chart(data).mark_line(point=True).encode(
        x=alt.X(x_value, type=x_value_type),
        y=alt.Y(y_value, type=y_value_type),
        color=alt.Color(color_values, scale=alt.Scale(scheme=scheme))
    ).properties(title=title)

    chart.save(output_path)


def create_bumpchart(
        data: pd.DataFrame,
        output_path: str,
        x_value: str,
        y_value: str,
        color_values: str,
        title: str,
        scheme: str,
        x_value_type: str,
        y_value_type: str,
        value_col: str,
        rank_col: str,
        group_col: list[str],
        num_rankings: int) -> None:
    """
    Create a bump chart for specified data and columns.

    Arguments:
        data (DataFrame): Input data to visualize.
        output_path (str): Absolute file path (including the name of the file)
            to save the plot to.
        x_value (str): The name of the column representing the x-axis.
        y_value (str): The name of the column representing the y-axis.
        color_values (str): The name of column representing the values to
            plot.
        title (str): The title of the plot.
        scheme (str): The color scheme to use. Please refer to the full
            gallery of available color schemes at
            https://vega.github.io/vega/docs/schemes/
        x_value_type (str): The type of data that will be plotted on the
            x-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
        y_value_type (str): The type of data that will be plotted on the
            y-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
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
        None

    Raises:
        None
    """

    logging.info("Creating rankings for bumpchart")
    ranked_data = create_rankings(
        df=data,
        value_col=value_col,
        rank_col=rank_col,
        group_col=group_col,
        num_rankings=num_rankings)

    logging.info("Plotting bumpchart data")
    create_linechart(
        data=ranked_data,
        output_path=output_path,
        x_value=x_value,
        y_value=y_value,
        color_values=color_values,
        title=title,
        scheme=scheme,
        x_value_type=x_value_type,
        y_value_type=y_value_type)
