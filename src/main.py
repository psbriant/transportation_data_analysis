"""
Description: Executes transportation data analysis and creates all
visualizations.
"""

import argparse
import logging

import numpy as np
import pandas as pd

from aggregations import (aggregate_data, get_route_count)
from constants import (viz_file_names,
                       BusDataArguments,
                       BarChartArguments,
                       BumpChartArguments,
                       LineChartArguments,
                       HeatmapArguments,
                       RouteCountArguments,
                       RidershipRecoveryArguments)
from data_processing import (change_column_datatype,
                             create_rankings,
                             split_df,
                             subset_dataframes_by_value)
from file_io import create_absolute_file_paths
from visualizations import (create_areachart,
                            create_barchart,
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
    route_count_args = RouteCountArguments()
    ridership_recovery_args = RidershipRecoveryArguments()

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
    hm_rmy_data, hm_rmy_agg_data = cta_bus_data.copy(), cta_bus_data.copy()

    # Create tiers for binning heatmaps:
    # 1. Calculate mean ridership for each route
    # 2. Create three tiers (bins) for low, medium and high ridership using
    # the previously calculated mean.
    # 3. Split data by ridership tiers.
    # 4. Split data by day type.
    hm_rmy_agg_data = hm_rmy_agg_data.drop(columns=['MONTH'])

    # 1. Calculate mean ridership for each route
    hm_rmy_agg_data = aggregate_data(
        df=cta_bus_data,
        agg_cols=['YEAR'],
        id_cols=['ROUTE', 'DAY_TYPE'],
        agg_type='mean')

    hm_rmy_agg_data = hm_rmy_agg_data.rename(
        columns={'AVG_RIDES': 'ROUTE_MEAN'})

    hm_rmy_data = hm_rmy_data.merge(
        hm_rmy_agg_data,
        how='left',
        on=['ROUTE', 'DAY_TYPE'])

    # 2. Create three tiers (bins) for low, medium and high ridership using
    # the previously calculated mean.
    hm_rmy_data['RIDERSHIP_TIER'] = pd.qcut(
        x=hm_rmy_data['ROUTE_MEAN'],
        q=3,
        labels=['low', 'medium', 'high'])

    hm_rmy_data = hm_rmy_data.drop(labels=['ROUTE_MEAN'], axis=1)

    # 3. Split data by ridership tiers.
    hm_rmy_data_tiers = split_df(df=hm_rmy_data, split_col='RIDERSHIP_TIER')
    hm_rmy_data_tiers = list(hm_rmy_data_tiers.values())

    # 4. Split data by day type.
    hm_rmy_1999_2022 = []

    for tier in hm_rmy_data_tiers:
        tdt_split = split_df(df=tier, split_col='DAY_TYPE')
        tdt_split = list(tdt_split.values())
        hm_rmy_1999_2022 += tdt_split

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
    agg_year_dfs = split_df(df=agg_year, split_col='DAY_TYPE')
    agg_year_dfs = list(agg_year_dfs.values())

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

    # Create subsets for the covid recovery analysis for 2019 and 2022 and use
    # them to create a recovery ratio.
    recovery_ratio = agg_year.copy()

    recovery_ratio_2019 = recovery_ratio[recovery_ratio['YEAR'] == 2019]
    recovery_ratio_2022 = recovery_ratio[recovery_ratio['YEAR'] == 2022]

    recovery_ratio_2019 = recovery_ratio_2019.rename(
        columns={'AVG_RIDES': 'AVG_RIDES_2019'})
    recovery_ratio_2022 = recovery_ratio_2022.rename(
        columns={'AVG_RIDES': 'AVG_RIDES_2022'})

    recovery_ratio_2019 = recovery_ratio_2019.drop(labels=['YEAR'], axis=1)
    recovery_ratio_2022 = recovery_ratio_2022.drop(labels=['YEAR'], axis=1)

    recovery_ratio_2019_2022 = recovery_ratio_2019.merge(
        recovery_ratio_2022,
        how='outer',
        on=['ROUTE', 'DAY_TYPE'])
    recovery_ratio_2019_2022 = recovery_ratio_2019_2022.dropna()

    recovery_ratio_2019_2022[
        'PERCENT_RECOVERED'] = (
            recovery_ratio_2019_2022[
                'AVG_RIDES_2022'] / recovery_ratio_2019_2022[
                                       'AVG_RIDES_2019']) * 100

    recovery_ratio_2019_2022 = recovery_ratio_2019_2022.drop(
        labels=['AVG_RIDES_2019', 'AVG_RIDES_2022'],
        axis=1)

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 1999 - 2022.
    rr_2019_2022_dfs = split_df(
        df=recovery_ratio_2019_2022,
        split_col='DAY_TYPE')
    rr_2019_2022_dfs = list(rr_2019_2022_dfs.values())

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
        df_list=agg_year_dfs,
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

    # Create absolute file paths for route count time series analysis (rctsa)
    # covering 1999 to 2022.
    rctsa_file_paths = create_absolute_file_paths(
        file_list=viz_file_names['route_count_bar_chart_args'],
        file_path=output_dir)

    # Create absolute file paths for ridership recovery analysis between 2019
    # and 2022.
    rrbc_file_paths = create_absolute_file_paths(
        file_list=viz_file_names['ridership_recovery_args'],
        file_path=output_dir)

    # Create year over year data for the change in the number of bus routes.
    route_counts = cta_bus_data.copy()
    route_counts = get_route_count(
        df=route_counts,
        route_dims=route_count_args.route_dims,
        count_dim=route_count_args.count_dim,
        count_col=route_count_args.count_col)

    route_counts = route_counts.sort_values(by='YEAR', ascending=True)
    route_counts['YOY'] = route_counts['COUNT'].diff()
    route_counts = route_counts.reset_index(drop=True)
    year_start = route_counts['YEAR'][0]
    year_end = route_counts['YEAR'][len(route_counts['YEAR']) - 1]

    route_yoy = route_counts.copy()
    route_yoy['YOY'].loc[route_yoy['YEAR'] == year_start] = \
        route_yoy['COUNT'].loc[route_yoy['YEAR'] == year_start]

    route_yoy['YOY'].loc[route_yoy['YEAR'] == year_end] = \
        route_yoy['COUNT'].loc[route_yoy['YEAR'] == year_end]

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (1999-2022)-----------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2009 (Weekday, Saturday, Sunday)
    # - 2010-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    logging.info(
        "Creating heatmaps for ridership by month and year (1999-2022)")
    for hm_df, hm_op in zip(hm_dfs, hm_file_paths):
        create_heatmap(
            data=hm_df,
            output_path=hm_op,
            x_value=heatmap_args.x_value,
            x_value_type=heatmap_args.x_value_type,
            y_value=heatmap_args.y_value,
            y_value_type=heatmap_args.y_value_type,
            x_axis_title=heatmap_args.x_axis_title,
            y_axis_title=heatmap_args.y_axis_title,
            color_title=heatmap_args.color_title,
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
    for ts_bc_df, ts_bc_op in zip(ts_bc_dfs, ts_bc_file_paths):
        create_barchart(
            data=ts_bc_df,
            output_path=ts_bc_op,
            x_value=barchart_args.x_value,
            y_value=barchart_args.y_value,
            x_value_type=barchart_args.x_value_type,
            y_value_type=barchart_args.y_value_type,
            color_values=barchart_args.color_values,
            title=barchart_args.title,
            x_axis_title=barchart_args.x_axis_title,
            y_axis_title=barchart_args.y_axis_title,
            color_title=barchart_args.color_title,
            scheme=barchart_args.scheme)

    # ------------------------------------------------------------------------
    # ---CREATE BAR CHARTS FOR RIDERSHIP RECOVERY BY ROUTE--------------------
    # ------------------------------------------------------------------------
    # - 2019-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    logging.info("Creating bar charts for ridership recovery by route")
    for rr_2019_2022_df, rr_bc_op in zip(rr_2019_2022_dfs, rrbc_file_paths):
        create_barchart(
            data=rr_2019_2022_df,
            output_path=rr_bc_op,
            x_value=ridership_recovery_args.x_value,
            y_value=ridership_recovery_args.y_value,
            x_value_type=ridership_recovery_args.x_value_type,
            y_value_type=ridership_recovery_args.y_value_type,
            color_values=ridership_recovery_args.color_values,
            title=ridership_recovery_args.title,
            x_axis_title=ridership_recovery_args.x_axis_title,
            y_axis_title=ridership_recovery_args.y_axis_title,
            color_title=ridership_recovery_args.color_title,
            scheme=ridership_recovery_args.scheme)

    # ------------------------------------------------------------------------
    # ---CREATE BUMP CHARTS FOR ROUTES BY RIDERSHIP AND YEAR------------------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2009 (Weekday, Saturday, Sunday)
    # - 2010-2019 (Weekday, Saturday, Sunday)
    # - 2020-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    logging.info("Creating bump charts for routes by ridership and year")
    for ts_bpc_df, ts_bpc_op in zip(ts_bpc_dfs, bpc_file_paths):
        create_bumpchart(
            data=ts_bpc_df,
            output_path=ts_bpc_op,
            x_value=bumpchart_args.x_value,
            y_value=bumpchart_args.y_value,
            x_value_type=bumpchart_args.x_value_type,
            y_value_type=bumpchart_args.y_value_type,
            color_values=bumpchart_args.color_values,
            x_axis_title=bumpchart_args.x_axis_title,
            y_axis_title=bumpchart_args.y_axis_title,
            color_title=bumpchart_args.color_title,
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
    for ts_df, ts_op in zip(ts_dfs, rrtsa_file_paths):
        create_linechart(
            data=ts_df,
            output_path=ts_op,
            x_value=rrtsa_args.x_value,
            y_value=rrtsa_args.y_value,
            x_value_type=rrtsa_args.x_value_type,
            y_value_type=rrtsa_args.y_value_type,
            x_axis_title=rrtsa_args.x_axis_title,
            y_axis_title=rrtsa_args.y_axis_title,
            color_title=rrtsa_args.color_title,
            color_values=rrtsa_args.color_values,
            title=rrtsa_args.title,
            scheme=rrtsa_args.scheme)
