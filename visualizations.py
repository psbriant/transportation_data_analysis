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


def create_bumpchart(
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

    Returns:
        None

    Raises:
        None
    """

    chart = alt.Chart(data).mark_line(point=True).encode(
        x=alt.X(x_value, type=x_value_type),
        y=alt.Y(y_value, type=y_value_type),
        color=alt.Color(color_values, scale=alt.Scale(scheme=scheme))
    ).properties(title=title, width=600, height=150)

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

