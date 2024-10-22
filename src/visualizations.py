"""
Description: Functions for creating analytical visualizations.
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
    x_axis_title: str,
    y_axis_title: str,
    color_title: str,
    color_values: str,
    facet_values: str,
    facet_columns: int,
    x_axis_sort_order: list[str],
    scheme: str,
    x_value_type: str,
    y_value_type: str,
    save_chart: bool = True) -> None:
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
        x_axis_title (str): The x-axis label of the plot.
        y_axis_title (str): The y-axis label of the plot.
        color_title (str): The legend label.
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
        save_chart (bool): Must be one of either True or False. If True,
            output plot to the file path specified by output_path. If False,
            return the plot. Defaults to True.

    Returns:
        Object representing the chart being created.

    Raises:
        TypeError if the value of the 'save_chart' argument  is not a bool.
    """

    # Confirm values for 'save_chart' are boolean values.
    if type(save_chart) is not bool:
        raise TypeError("The value of 'save_chart' should be a bool")

    data = data.copy()

    chart = alt.Chart(data).mark_rect().encode(
        alt.X(x_value,
              type=x_value_type,
              title=x_axis_title,
              sort=x_axis_sort_order),
        alt.Y(y_value, type=y_value_type, title=y_axis_title),
        alt.Color(color_values,
                  type='quantitative',
                  title=color_title,
                  scale=alt.Scale(scheme=scheme)),
        alt.Facet(facet_values,
                  type='ordinal',
                  columns=facet_columns),
        stroke=alt.value('black'),
        strokeWidth=alt.value(0.2),
    )

    if save_chart:
        chart.save(output_path)
    else:
        return chart


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
        x_axis_title: str,
        y_axis_title: str,
        color_title: str,
        sort_order_y_axis: str = '-x',
        sort_order_color: str | list[str] = 'ascending',
        save_chart: bool = True) -> None:
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
        x_axis_title (str): The x-axis label of the plot.
        y_axis_title (str): The y-axis label of the plot.
        color_title (str): The legend label.
        sort_order_y_axis (str): The sort order for the y-axis. Defaults to
            '-x'.
        sort_order_color (str or strlist): The sort order for the color scheme
            and legend. One of "ascending", "descending", or a list of strings
            containing a custom order. Defaults to ascending.
        save_chart (bool): Must be one of either True or False. If True,
            output plot to the file path specified by output_path. If False,
            return the plot. Defaults to True.

    Returns:
        Object representing the chart being created.

    Raises:
        TypeError if the value of the 'save_chart' argument  is not a bool.
    """

    # Confirm values for 'save_chart' are boolean values.
    if type(save_chart) is not bool:
        raise TypeError("The value of 'save_chart' should be a bool")

    data = data.copy()

    chart = alt.Chart(data).mark_bar().encode(
        alt.X(x_value, type=x_value_type, title=x_axis_title),
        alt.Y(y_value,
              type=y_value_type,
              title=y_axis_title,
              sort=sort_order_y_axis),
        alt.Color(color_values,
                  sort=sort_order_color,
                  title=color_title,
                  scale=alt.Scale(scheme=scheme))
    ).properties(title=title)

    if save_chart:
        chart.save(output_path)
    else:
        return chart


def create_linechart(
        data: pd.DataFrame,
        output_path: str,
        x_value: str,
        y_value: str,
        color_values: str,
        title: str,
        scheme: str,
        x_value_type: str,
        y_value_type: str,
        x_axis_title: str,
        y_axis_title: str,
        color_title: str,
        save_chart: bool = True) -> None:
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
        x_axis_title (str): The x-axis label of the plot.
        y_axis_title (str): The y-axis label of the plot.
        color_title (str): The legend label.
        save_chart (bool): Must be one of either True or False. If True,
            output plot to the file path specified by output_path. If False,
            return the plot. Defaults to True.

    Returns:
        Object representing the chart being created.

    Raises:
        TypeError if the value of the 'save_chart' argument  is not a bool.
    """

    # Confirm values for 'save_chart' are boolean values.
    if type(save_chart) is not bool:
        raise TypeError("The value of 'save_chart' should be a bool")

    data = data.copy()

    chart = alt.Chart(data).mark_line(point=True).encode(
        x=alt.X(x_value, type=x_value_type, title=x_axis_title),
        y=alt.Y(y_value, type=y_value_type, title=y_axis_title),
        color=alt.Color(color_values,
                        title=color_title,
                        scale=alt.Scale(scheme=scheme))
    ).properties(title=title)

    if save_chart:
        chart.save(output_path)
    else:
        return chart


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
        x_axis_title: str,
        y_axis_title: str,
        color_title: str,
        value_col: str,
        rank_col: str,
        group_col: list[str],
        num_rankings: int,
        save_chart: bool = True) -> None:
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
        x_axis_title (str): The x-axis label of the plot.
        y_axis_title (str): The y-axis label of the plot.
        color_title (str): The legend label.
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
        save_chart (bool): Must be one of either True or False. If True,
            output plot to the file path specified by output_path. If False,
            return the plot. Defaults to True.


    Returns:
        Object representing the chart being created.

    Raises:
        TypeError if the value of the 'save_chart' argument  is not a bool.
    """

    # Confirm values for 'save_chart' are boolean values.
    if type(save_chart) is not bool:
        raise TypeError("The value of 'save_chart' should be a bool")

    data = data.copy()

    logging.info("Creating rankings for bumpchart")
    ranked_data = create_rankings(
        df=data,
        value_col=value_col,
        rank_col=rank_col,
        group_col=group_col,
        num_rankings=num_rankings)

    logging.info("Plotting bumpchart data")
    chart = create_linechart(
        data=ranked_data,
        output_path=output_path,
        x_value=x_value,
        y_value=y_value,
        color_values=color_values,
        title=title,
        scheme=scheme,
        x_value_type=x_value_type,
        y_value_type=y_value_type,
        x_axis_title=x_axis_title,
        y_axis_title=y_axis_title,
        color_title=color_title)

    if save_chart:
        chart.save(output_path)
    else:
        return chart


def create_areachart(
        data: pd.DataFrame,
        output_path: str,
        x_value: str,
        y_value: str,
        title: str,
        x_value_type: str,
        y_value_type: str,
        x_axis_title: str,
        y_axis_title: str,
        color: str,
        save_chart: bool = True) -> None:
    """
    Create an area chart for specified data and columns.

    Arguments:
        data (DataFrame): Input data to visualize.
        output_path (str): Absolute file path (including the name of the file)
            to save the plot to.
        x_value (str): The name of the column representing the x-axis.
        y_value (str): The name of the column representing the y-axis.
        title (str): The title of the plot.
        x_value_type (str): The type of data that will be plotted on the
            x-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
        y_value_type (str): The type of data that will be plotted on the
            y-axis. Must be one of quantitative, ordinal, nominal, temporal,
            or geojson.
        x_axis_title (str): The x-axis label of the plot.
        y_axis_title (str): The y-axis label of the plot.
        color (str): The color of the area plot. Can be the name of a color or
            a hexidecimal.
        save_chart (bool): Must be one of either True or False. If True,
            output plot to the file path specified by output_path. If False,
            return the plot. Defaults to True.

    Returns:
        Object representing the chart being created.

    Raises:
        TypeError if the value of the 'save_chart' argument  is not a bool.
    """

    # Confirm values for 'save_chart' are boolean values.
    if type(save_chart) is not bool:
        raise TypeError("The value of 'save_chart' should be a bool")

    data = data.copy()

    chart = alt.Chart(data).mark_area(
        color=color,
        interpolate='step-after',
        line=True
    ).encode(
        x=alt.X(x_value, type=x_value_type, title=x_axis_title),
        y=alt.Y(y_value, type=y_value_type, title=y_axis_title)
    ).properties(title=title)

    chart.save(output_path)

    if save_chart:
        chart.save(output_path)
    else:
        return chart
