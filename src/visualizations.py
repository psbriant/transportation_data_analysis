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
        sort_order_y_axis: str = '-x',
        sort_order_color: str | list[str] = 'ascending') -> None:
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
        sort_order_y_axis (str): The sort order for the y-axis. Defaults to
            '-x'.
        sort_order_color (str or strlist): The sort order for the color scheme
            and legend. One of "ascending", "descending", or a list of strings
            containing a custom order. Defaults to ascending.

    Returns:
        None

    Raises:
        None
    """

    chart = alt.Chart(data).mark_bar().encode(
        alt.X(x_value, type=x_value_type),
        alt.Y(y_value, type=y_value_type, sort=sort_order_y_axis),
        alt.Color(color_values,
                  sort=sort_order_color,
                  scale=alt.Scale(scheme=scheme))
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

# def create_waterfall_chart(
#         data: pd.DataFrame,
#         output_path: str,
#         x_value: str,
#         y_value: str) -> None:
#     """
#     Arguments:
#         data (DataFrame): Input data to visualize.
#         output_path (str): Absolute file path (including the name of the file)
#             to save the plot to.
#         x_value (str): The name of the column representing the x-axis.
#         y_value (str): The name of the column representing the y-axis.
#
#     Returns:
#         NONE
#     """
#
#     # The "base_chart" defines the transform_window, transform_calculate, and
#     # X axis
#     base_chart = alt.Chart(data).transform_window(
#         window_sum_amount=f"sum({y_value})",
#         window_lead_label=f"lead({x_value})",
#     ).transform_calculate(
#         calc_lead="datum.window_lead_label === null ? datum.label : datum.window_lead_label",
#         calc_prev_sum="datum.label === 'End' ? 0 : datum.window_sum_amount - datum.amount",
#         calc_amount="datum.label === 'End' ? datum.window_sum_amount : datum.amount",
#         calc_text_amount="(datum.label !== 'Begin' && datum.label !== 'End' && datum.calc_amount > 0 ? '+' : '') + datum.calc_amount",
#         calc_center="(datum.window_sum_amount + datum.calc_prev_sum) / 2",
#         calc_sum_dec="datum.window_sum_amount < datum.calc_prev_sum ? datum.window_sum_amount : ''",
#         calc_sum_inc="datum.window_sum_amount > datum.calc_prev_sum ? datum.window_sum_amount : ''",
#     ).encode(
#         x=alt.X(
#             "label:O",
#             axis=alt.Axis(title="Months", labelAngle=0),
#             sort=None,
#         )
#     )
#
#     # alt.condition does not support multiple if else conditions which is why
#     # we use a dictionary instead. See https://stackoverflow.com/a/66109641
#     # for more information
#     color_coding = {
#         "condition": [
#             {"test": "datum.label === 'Begin' || datum.label === 'End'",
#              "value": "#878d96"},
#             {"test": "datum.calc_amount < 0", "value": "#24a148"},
#         ],
#         "value": "#fa4d56",
#     }
#
#     bar = base_chart.mark_bar(size=45).encode(
#         y=alt.Y("calc_prev_sum:Q", title="Amount"),
#         y2=alt.Y2("window_sum_amount:Q"),
#         color=color_coding,
#     )
#
#     # The "rule" chart is for the horizontal lines that connect the bars
#     rule = base_chart.mark_rule(
#         xOffset=-22.5,
#         x2Offset=22.5,
#     ).encode(
#         y="window_sum_amount:Q",
#         x2="calc_lead",
#     )
#
#     # Add values as text
#     text_pos_values_top_of_bar = base_chart.mark_text(
#         baseline="bottom",
#         dy=-4
#     ).encode(
#         text=alt.Text("calc_sum_inc:N"),
#         y="calc_sum_inc:Q"
#     )
#     text_neg_values_bot_of_bar = base_chart.mark_text(
#         baseline="top",
#         dy=4
#     ).encode(
#         text=alt.Text("calc_sum_dec:N"),
#         y="calc_sum_dec:Q"
#     )
#     text_bar_values_mid_of_bar = base_chart.mark_text(
#         baseline="middle").encode(
#         text=alt.Text("calc_text_amount:N"),
#         y="calc_center:Q",
#         color=alt.value("white"),
#     )
#
#     final_chart = alt.layer(
#         bar,
#         rule,
#         text_pos_values_top_of_bar,
#         text_neg_values_bot_of_bar,
#         text_bar_values_mid_of_bar
#         ).properties(
#         width=800,
#         height=450
#         )
#
#     bar.save(output_path)
#     # final_chart.save(output_path)
