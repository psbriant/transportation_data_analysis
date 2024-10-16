"""
Description: Tests for visualization functions.
"""

import altair as alt
import numpy as np
import pandas as pd
import pytest

from visualizations import (create_heatmap,
                            create_barchart,
                            create_linechart,
                            create_bumpchart)


# @pytest.mark.parametrize(
#     "data,output_path,x_value,y_value,color_values,facet_values,facet_columns,x_axis_sort_order,scheme,x_value_type,y_value_type,request",
#     [('input_df', ['>='], ['YEAR'], [2011], 'expected_subset_dfs_gtet'),
#      ('input_dfs',
#       ['>', '<'],
#       ['YEAR', 'YEAR'],
#       [2009, 2020],
#       'expected_subset_dfs_gtalt'),
#      ('input_dfs', ['=='], ['YEAR'], [2011], 'expected_subset_dfs_et')])
# def test_create_heatmap(
#         data: pd.DataFrame,
#         output_path: str,
#         x_value: str,
#         y_value: str,
#         color_values: str,
#         facet_values: str,
#         facet_columns: int,
#         x_axis_sort_order: list[str],
#         scheme: str,
#         x_value_type: str,
#         y_value_type: str,
#         request) -> None:
#     """
#
#     Arguments:
#         data (DataFrame): Input data to visualize.
#         output_path (str): Absolute file path (including the name of the file)
#             to save the plot to.
#         x_value (str): The name of the column representing the x-axis.
#         y_value (str): The name of the column representing the y-axis.
#         color_values (str): The name of column representing the values to
#             plot.
#         facet_values (str): The name of the column representing the values to
#             create a facet grid of plots for.
#         facet_columns (int): The number of columns the facet grid will
#             contain.
#         x_axis_sort_order (strList): A list of strings representing the order
#             of values on the x-axis.
#         scheme (str): The color scheme to use. Please refer to the full
#             gallery of available color schemes at
#             https://vega.github.io/vega/docs/schemes/
#         x_value_type (str): The type of data that will be plotted on the
#             x-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         y_value_type (str): The type of data that will be plotted on the
#             y-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         request: A special fixture used to provide information regarding the
#             requesting test function. This is used to retrieve the value of
#             fixtures used in parameterized tests.
#
#     Returns:
#         NONE
#
#     """
#     create_heatmap(
#         data=data,
#         output_path=output_path,
#         x_value=x_value,
#         x_value_type=x_value_type,
#         y_value=y_value,
#         y_value_type=y_value_type,
#         color_values=color_values,
#         facet_values=facet_values,
#         facet_columns=facet_columns,
#         scheme=scheme,
#         x_axis_sort_order=x_axis_sort_order)
#
#
# @pytest.mark.parametrize(
#     "data,output_path,x_value,y_value,color_values,title,scheme,x_value_type,y_value_type,sort_order,request",
#     [('input_df', ['>='], ['YEAR'], [2011], 'expected_subset_dfs_gtet'),
#      ('input_dfs',
#       ['>', '<'],
#       ['YEAR', 'YEAR'],
#       [2009, 2020],
#       'expected_subset_dfs_gtalt'),
#      ('input_dfs', ['=='], ['YEAR'], [2011], 'expected_subset_dfs_et')])
# def test_create_barchart(
#         data: pd.DataFrame,
#         output_path: str,
#         x_value: str,
#         y_value: str,
#         color_values: str,
#         title: str,
#         scheme: str,
#         x_value_type: str,
#         y_value_type: str,
#         sort_order: str | list[str],
#         request) -> None:
#     """
#
#     Arguments:
#         data (DataFrame): Input data to visualize.
#         output_path (str): Absolute file path (including the name of the file)
#             to save the plot to.
#         x_value (str): The name of the column representing the x-axis.
#         y_value (str): The name of the column representing the y-axis.
#         color_values (str): The name of column representing the values to
#             plot.
#         title (str): The title of the plot.
#         scheme (str): The color scheme to use. Please refer to the full
#             gallery of available color schemes at
#             https://vega.github.io/vega/docs/schemes/
#         x_value_type (str): The type of data that will be plotted on the
#             x-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         y_value_type (str): The type of data that will be plotted on the
#             y-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         sort_order (str or strlist): The sort order. One of "ascending",
#             "descending", or a list of strings containing a custom order.
#             Defaults to ascending.
#         request: A special fixture used to provide information regarding the
#             requesting test function. This is used to retrieve the value of
#             fixtures used in parameterized tests.
#
#     Returns:
#         NONE
#
#     """
#     create_barchart(
#         data=data,
#         output_path=output_path,
#         x_value=x_value,
#         y_value=y_value,
#         x_value_type=x_value_type,
#         y_value_type=y_value_type,
#         color_values=color_values,
#         title=title,
#         scheme=scheme,
#         sort_order=sort_order)
#
#
# @pytest.mark.parametrize(
#     "data,output_path,x_value,y_value,color_values,title,scheme,x_value_type,y_value_type,request",
#     [('input_df', ['>='], ['YEAR'], [2011], 'expected_subset_dfs_gtet'),
#      ('input_dfs',
#       ['>', '<'],
#       ['YEAR', 'YEAR'],
#       [2009, 2020],
#       'expected_subset_dfs_gtalt'),
#      ('input_dfs', ['=='], ['YEAR'], [2011], 'expected_subset_dfs_et')])
# def test_create_linechart(
#         data: pd.DataFrame,
#         output_path: str,
#         x_value: str,
#         y_value: str,
#         color_values: str,
#         title: str,
#         scheme: str,
#         x_value_type: str,
#         y_value_type: str,
#         request) -> None:
#     """
#
#     Arguments:
#         data (DataFrame): Input data to visualize.
#         output_path (str): Absolute file path (including the name of the file)
#             to save the plot to.
#         x_value (str): The name of the column representing the x-axis.
#         y_value (str): The name of the column representing the y-axis.
#         color_values (str): The name of column representing the values to
#             plot.
#         title (str): The title of the plot.
#         scheme (str): The color scheme to use. Please refer to the full
#             gallery of available color schemes at
#             https://vega.github.io/vega/docs/schemes/
#         x_value_type (str): The type of data that will be plotted on the
#             x-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         y_value_type (str): The type of data that will be plotted on the
#             y-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         request: A special fixture used to provide information regarding the
#             requesting test function. This is used to retrieve the value of
#             fixtures used in parameterized tests.
#
#     Returns:
#         NONE
#
#     """
#     create_linechart(
#         data=data,
#         output_path=output_path,
#         x_value=x_value,
#         y_value=y_value,
#         x_value_type=x_value_type,
#         y_value_type=y_value_type,
#         color_values=color_values,
#         title=title,
#         scheme=scheme)
#
#
# @pytest.mark.parametrize(
#     "data,output_path,x_value,y_value,color_values,title,scheme,x_value_type,y_value_type,value_col,rank_col,group_col,num_rankings,request",
#     [('input_df', ['>='], ['YEAR'], [2011], 'expected_subset_dfs_gtet'),
#      ('input_dfs',
#       ['>', '<'],
#       ['YEAR', 'YEAR'],
#       [2009, 2020],
#       'expected_subset_dfs_gtalt'),
#      ('input_dfs', ['=='], ['YEAR'], [2011], 'expected_subset_dfs_et')])
# def test_create_bumpchart(
#         data: pd.DataFrame,
#         output_path: str,
#         x_value: str,
#         y_value: str,
#         color_values: str,
#         title: str,
#         scheme: str,
#         x_value_type: str,
#         y_value_type: str,
#         value_col: str,
#         rank_col: str,
#         group_col: list[str],
#         num_rankings: int,
#         request) -> None:
#     """
#
#     Arguments:
#         data (DataFrame): Input data to visualize.
#         output_path (str): Absolute file path (including the name of the file)
#             to save the plot to.
#         x_value (str): The name of the column representing the x-axis.
#         y_value (str): The name of the column representing the y-axis.
#         color_values (str): The name of column representing the values to
#             plot.
#         title (str): The title of the plot.
#         scheme (str): The color scheme to use. Please refer to the full
#             gallery of available color schemes at
#             https://vega.github.io/vega/docs/schemes/
#         x_value_type (str): The type of data that will be plotted on the
#             x-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         y_value_type (str): The type of data that will be plotted on the
#             y-axis. Must be one of quantitative, ordinal, nominal, temporal,
#             or geojson.
#         value_col (str): The name of the column rankings will be based off of.
#         rank_col (str): The name of the column containing the numerical
#             rankings.
#         group_col (strList): The columns used for ensuring rankings are made
#             across columns (e.g. specifying the year column in a dataset
#             containing bus routes, ridership numbers and years will rank each
#             bus route by ridership for each year).
#         num_rankings (int): The number of rows to return rankings for. If set
#             to zero, no limit will be applied and all rows will be ranked.
#             Defaults to zero.
#         request: A special fixture used to provide information regarding the
#             requesting test function. This is used to retrieve the value of
#             fixtures used in parameterized tests.
#
#     Returns:
#         NONE
#
#     """
#     create_bumpchart(
#         data=data,
#         output_path=output_path,
#         x_value=x_value,
#         y_value=y_value,
#         x_value_type=x_value_type,
#         y_value_type=y_value_type,
#         color_values=color_values,
#         title=title,
#         scheme=scheme,
#         value_col=value_col,
#         rank_col=rank_col,
#         group_col=group_col,
#         num_rankings=num_rankings)
