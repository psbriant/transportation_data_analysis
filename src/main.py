"""
Description: Executes transportation data analysis and creates all
visualizations.
"""

import argparse
import logging

import numpy as np
import pandas as pd

from aggregations import aggregate_data
from constants import (viz_file_names,
                       BusDataArguments,
                       BarChartArguments,
                       BumpChartArguments,
                       LineChartArguments,
                       HeatmapArguments)
from data_processing import (change_column_datatype,
                             create_rankings,
                             split_df,
                             subset_dataframes_by_value)
from file_io import create_absolute_file_paths
from visualizations import (create_barchart,
                            create_bumpchart,
                            create_heatmap,
                            create_linechart)


if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s - %(message)s',
                        level=logging.INFO)

    parser = argparse.ArgumentParser(
        description='Arguments for visualizing data')
    parser.add_argument(
        '--bus_data_path',
        required=True,
        type=str,
        help='The absolute file path to the bus data being analyzed')
    parser.add_argument(
        '--output_dir',
        required=True,
        type=str,
        help='The absolute file path to output directory where the plots will'
             ' be saved')

    args = parser.parse_args()

    bus_data_path = args.bus_data_path
    output_dir = args.output_dir

    # ------------------------------------------------------------------------
    # ---INITIALIZE CONSTANT ARGUMENTS----------------------------------------
    # ------------------------------------------------------------------------

    bus_data_args = BusDataArguments()
    barchart_args = BarChartArguments()
    bumpchart_args = BumpChartArguments()
    rrtsa_args = LineChartArguments()
    heatmap_args = HeatmapArguments()

    # ------------------------------------------------------------------------
    # ---LOAD DATASET---------------------------------------------------------
    # ------------------------------------------------------------------------

    logging.info("Loading bus data")
    cta_bus_data = pd.read_csv(bus_data_path, encoding='utf-8')

    # ------------------------------------------------------------------------
    # ---PREP DATA------------------------------------------------------------
    # ------------------------------------------------------------------------

    # Remove 2023 data since it is currently only for a few months
    cta_bus_data = subset_dataframes_by_value(
        dfs=[cta_bus_data],
        operator=['<'],
        target_col=['YEAR'],
        filter_val=[2023])

    # Change values in the month column so that they represent the actual
    # names of each month instead of the numerical representation.
    cta_bus_data['MONTH'] = cta_bus_data['MONTH'].replace(
        bus_data_args.alpha_to_numeric_months)

    # Create dataframe for making heatmaps.
    logging.info("Subsetting data")
    hm_rmy_data = cta_bus_data.copy()

    hm_rmy_data_1999_2022_wd, hm_rmy_data_1999_2022_sat, \
        hm_rmy_data_1999_2022_sun = hm_rmy_data.copy(), hm_rmy_data.copy(), \
        hm_rmy_data.copy()

    hm_rmy_data_1999_2022_wd = hm_rmy_data_1999_2022_wd.query(
        'DAY_TYPE == "Weekday"')
    hm_rmy_data_1999_2022_sat = hm_rmy_data_1999_2022_sat.query(
        'DAY_TYPE == "Saturday"')
    hm_rmy_data_1999_2022_sun = hm_rmy_data_1999_2022_sun.query(
        'DAY_TYPE == "Sunday - Holiday"')

    hm_rmy_1999_2022 = [hm_rmy_data_1999_2022_wd,
                        hm_rmy_data_1999_2022_sat,
                        hm_rmy_data_1999_2022_sun]

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 1999 - 2009.
    hm_rmy_1999_2009 = subset_dataframes_by_value(
        dfs=hm_rmy_1999_2022,
        operator=['<='],
        target_col=['YEAR'],
        filter_val=[2009])

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 2010 - 2022.
    hm_rmy_2010_2022 = subset_dataframes_by_value(
        dfs=hm_rmy_1999_2022,
        operator=['>='],
        target_col=['YEAR'],
        filter_val=[2010])

    # Create list of heatmap dataframes
    hm_dfs = hm_rmy_1999_2022 + hm_rmy_1999_2009 + hm_rmy_2010_2022

    # Create aggregate ridership data by route, year for each service type
    agg_year = aggregate_data(
        df=cta_bus_data,
        agg_cols=['MONTH'],
        id_cols=['ROUTE', 'YEAR', 'DAY_TYPE'],
        agg_type='sum')

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 1999 - 2022.
    agg_year_wd, agg_year_sat, agg_year_sun = agg_year.copy(), \
        agg_year.copy(), agg_year.copy()

    agg_year_wd = agg_year_wd.query('DAY_TYPE == "Weekday"')
    agg_year_sat = agg_year_sat.query('DAY_TYPE == "Saturday"')
    agg_year_sun = agg_year_sun.query('DAY_TYPE == "Sunday - Holiday"')

    agg_year_dfs = [agg_year_wd, agg_year_sat, agg_year_sun]

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 1999 - 2009.
    agg_year_dfs_1999_2009 = subset_dataframes_by_value(
        dfs=agg_year_dfs,
        operator=['<'],
        target_col=['YEAR'],
        filter_val=[2010])

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 2010 - 2019.
    agg_year_dfs_2010_2019 = subset_dataframes_by_value(
        dfs=agg_year_dfs,
        operator=['>', '<'],
        target_col=['YEAR', 'YEAR'],
        filter_val=[2009, 2020])

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 2020 - 2022.
    agg_year_dfs_2020_2022 = subset_dataframes_by_value(
        dfs=agg_year_dfs,
        operator=['>'],
        target_col=['YEAR'],
        filter_val=[2019])

    # Add a rank column based off of ridership.
    ts_dfs = []

    for df in agg_year_dfs:
        ts_rankings = create_rankings(
            df=df,
            value_col=rrtsa_args.value_col,
            rank_col=rrtsa_args.rank_col,
            group_col=rrtsa_args.group_col,
            num_rankings=rrtsa_args.num_rankings)

        ts_dfs.append(ts_rankings)

    # Change values in the "YEAR" column from integers to strings to improve
    # plot readability for barcharts representing more than one year of data.
    # Please note that this must be executed after subsetting each dataframe
    # by the relevant years to avoid raising a TypeError.
    ts_bc_dfs = agg_year_dfs + agg_year_dfs_1999_2009 + agg_year_dfs_2010_2019 + agg_year_dfs_2020_2022
    ts_bc_dfs = change_column_datatype(
        df_list=ts_bc_dfs,
        col='YEAR',
        datatype='str')

    # Change values in the "YEAR" column from integers to strings to improve
    # plot readability for bump charts representing more than one year of
    # data. Please note that this must be executed after subsetting each
    # dataframe by the relevant years to avoid raising a TypeError.
    ts_bpc_dfs = change_column_datatype(
        df_list=ts_dfs,
        col='YEAR',
        datatype='str')

    # Create absolute file paths for heatmaps covering the first 10 months
    # of 2022.
    hm_file_paths = create_absolute_file_paths(
        file_list=viz_file_names['heatmap_args'],
        file_path=output_dir)

    # Create absolute file paths for bar charts covering multiple years
    ts_bc_file_paths = create_absolute_file_paths(
        file_list=viz_file_names['bar_chart_args'],
        file_path=output_dir)

    # Create absolute file paths for bump charts covering 1999 to 2022
    bpc_file_paths = create_absolute_file_paths(
        file_list=viz_file_names['bump_chart_args'],
        file_path=output_dir)

    # Create absolute file paths for ridership time series analysis (rrtsa)
    # line plots covering 1999 to 2022.
    rrtsa_file_paths = create_absolute_file_paths(
        file_list=viz_file_names['line_chart_args'],
        file_path=output_dir)

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (1999-2022)-----------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2009 (Weekday, Saturday, Sunday)
    # - 2010-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    logging.info(
        "Creating heatmaps for ridership by month and year (1999-2022)")
    for df, op in zip(hm_dfs, hm_file_paths):

        create_heatmap(
            data=df,
            output_path=op,
            x_value=heatmap_args.x_value,
            x_value_type=heatmap_args.x_value_type,
            y_value=heatmap_args.y_value,
            y_value_type=heatmap_args.y_value_type,
            color_values=heatmap_args.color_values,
            facet_values=heatmap_args.facet_values,
            facet_columns=heatmap_args.facet_columns,
            scheme=heatmap_args.scheme,
            x_axis_sort_order=heatmap_args.x_axis_sort_order)

    # ------------------------------------------------------------------------
    # ---CREATE STACKED BAR CHARTS FOR ROUTES BY RIDERSHIP--------------------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2009 (Weekday, Saturday, Sunday)
    # - 2010-2019 (Weekday, Saturday, Sunday)
    # - 2020-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    logging.info("Creating stacked bar charts for routes by ridership")
    for df, op in zip(ts_bc_dfs, ts_bc_file_paths):

        create_barchart(
            data=df,
            output_path=op,
            x_value=barchart_args.x_value,
            y_value=barchart_args.y_value,
            x_value_type=barchart_args.x_value_type,
            y_value_type=barchart_args.y_value_type,
            color_values=barchart_args.color_values,
            title=barchart_args.title,
            scheme=barchart_args.scheme)

    # ------------------------------------------------------------------------
    # ---CREATE BUMP CHARTS FOR ROUTES BY RIDERSHIP AND YEAR------------------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2009 (Weekday, Saturday, Sunday)
    # - 2010-2019 (Weekday, Saturday, Sunday)
    # - 2020-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    logging.info("Creating bump charts for routes by ridership and year")
    for df, op in zip(ts_bpc_dfs, bpc_file_paths):
        create_bumpchart(
            data=df,
            output_path=op,
            x_value=bumpchart_args.x_value,
            y_value=bumpchart_args.y_value,
            x_value_type=bumpchart_args.x_value_type,
            y_value_type=bumpchart_args.y_value_type,
            color_values=bumpchart_args.color_values,
            title=bumpchart_args.title,
            scheme=bumpchart_args.scheme,
            value_col=bumpchart_args.value_col,
            rank_col=bumpchart_args.rank_col,
            group_col=bumpchart_args.group_col,
            num_rankings=bumpchart_args.num_rankings)

    # ------------------------------------------------------------------------
    # ---CREATE LINE PLOTS FOR ROUTES BY RIDERSHIP AND YEAR-------------------
    # ------------------------------------------------------------------------
    # The plots created below represent a time series analysis of route
    # ridership or for our purposes a route ridership time series analysis
    # (rrtsa).
    #
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    logging.info("Creating line plots for routes by ridership and year")
    for df, op in zip(ts_dfs, rrtsa_file_paths):
        create_linechart(
            data=df,
            output_path=op,
            x_value=rrtsa_args.x_value,
            y_value=rrtsa_args.y_value,
            x_value_type=rrtsa_args.x_value_type,
            y_value_type=rrtsa_args.y_value_type,
            color_values=rrtsa_args.color_values,
            title=rrtsa_args.title,
            scheme=rrtsa_args.scheme)
