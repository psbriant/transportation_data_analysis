"""
Description: Executes transportation data analysis and creates all
visualizations.

TODO: Determine how to handle the year 2022 since some months do not have
    ridership data (the values are represented by nans).
"""

import argparse
import logging

import numpy as np
import pandas as pd

from constants import (viz_file_names,
                       BusDataArguments,
                       BarChartArguments,
                       BarChartArguments_2022,
                       BumpChartArguments,
                       LineChartArguments,
                       HeatmapArguments)
from data_processing import (change_column_datatype,
                             create_rankings,
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
    barchart_args_2022 = BarChartArguments_2022()
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

    hm_rmy_data_1999_2022_wd = hm_rmy_data_1999_2022_wd[
        hm_rmy_data_1999_2022_wd['DAY_TYPE'] == 'Weekday']
    hm_rmy_data_1999_2022_sat = hm_rmy_data_1999_2022_sat[
        hm_rmy_data_1999_2022_sat['DAY_TYPE'] == 'Saturday']
    hm_rmy_data_1999_2022_sun = hm_rmy_data_1999_2022_sun[
        hm_rmy_data_1999_2022_sun['DAY_TYPE'] == 'Sunday - Holiday']

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 1999 - 2010.
    hm_rmy_data_1999_2010_wd, hm_rmy_data_1999_2010_sat, \
        hm_rmy_data_1999_2010_sun = hm_rmy_data_1999_2022_wd.copy(), \
        hm_rmy_data_1999_2022_sat.copy(), hm_rmy_data_1999_2022_sun.copy()

    hm_rmy_data_1999_2010_wd = hm_rmy_data_1999_2010_wd[
        hm_rmy_data_1999_2010_wd['YEAR'] <= 2010]
    hm_rmy_data_1999_2010_sat = hm_rmy_data_1999_2010_sat[
        hm_rmy_data_1999_2010_sat['YEAR'] <= 2010]
    hm_rmy_data_1999_2010_sun = hm_rmy_data_1999_2010_sun[
        hm_rmy_data_1999_2010_sun['YEAR'] <= 2010]

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 2011 - 2022.
    hm_rmy_data_2011_2022_wd, hm_rmy_data_2011_2022_sat, \
        hm_rmy_data_2011_2022_sun = hm_rmy_data_1999_2022_wd.copy(), \
        hm_rmy_data_1999_2022_sat.copy(), hm_rmy_data_1999_2022_sun.copy()

    hm_rmy_data_2011_2022_wd = hm_rmy_data_2011_2022_wd[
        hm_rmy_data_2011_2022_wd['YEAR'] >= 2011]
    hm_rmy_data_2011_2022_sat = hm_rmy_data_2011_2022_sat[
        hm_rmy_data_2011_2022_sat['YEAR'] >= 2011]
    hm_rmy_data_2011_2022_sun = hm_rmy_data_2011_2022_sun[
        hm_rmy_data_2011_2022_sun['YEAR'] >= 2011]

    # Create list of heatmap dataframes
    hm_dfs = [hm_rmy_data_1999_2022_wd,
              hm_rmy_data_1999_2022_sat,
              hm_rmy_data_1999_2022_sun,
              hm_rmy_data_1999_2010_wd,
              hm_rmy_data_1999_2010_sat,
              hm_rmy_data_1999_2010_sun,
              hm_rmy_data_2011_2022_wd,
              hm_rmy_data_2011_2022_sat,
              hm_rmy_data_2011_2022_sun]

    # Create aggregate ridership data by route, year for each service type
    agg_year = cta_bus_data.copy()
    agg_year = agg_year.drop(labels=['MONTH'], axis=1)
    agg_year = agg_year.groupby(by=['ROUTE', 'YEAR', 'DAY_TYPE']).sum()
    agg_year = agg_year.reset_index()

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 1999 - 2022.
    agg_year_wd, agg_year_sat, agg_year_sun = agg_year.copy(), \
        agg_year.copy(), agg_year.copy()

    agg_year_wd = agg_year_wd[agg_year_wd['DAY_TYPE'] == 'Weekday']
    agg_year_sat = agg_year_sat[agg_year_sat['DAY_TYPE'] == 'Saturday']
    agg_year_sun = agg_year_sun[agg_year_sun['DAY_TYPE'] == 'Sunday - Holiday']

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 1999 - 2009.
    agg_year_wd_1999_2009, agg_year_sat_1999_2009, agg_year_sun_1999_2009 = agg_year_wd.copy(), \
        agg_year_sat.copy(), agg_year_sun.copy()

    agg_year_wd_1999_2009 = agg_year_wd_1999_2009[
        agg_year_wd_1999_2009['YEAR'] < 2010]
    agg_year_sat_1999_2009 = agg_year_sat_1999_2009[
        agg_year_sat_1999_2009['YEAR'] < 2010]
    agg_year_sun_1999_2009 = agg_year_sun_1999_2009[
        agg_year_sun_1999_2009['YEAR'] < 2010]

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 2010 - 2019.
    agg_year_wd_2010_2019, agg_year_sat_2010_2019, agg_year_sun_2010_2019 = agg_year_wd.copy(), \
        agg_year_sat.copy(), agg_year_sun.copy()

    agg_year_wd_2010_2019 = agg_year_wd_2010_2019[
        (agg_year_wd_2010_2019['YEAR'] > 2009) & (agg_year_wd_2010_2019['YEAR'] < 2020)]
    agg_year_sat_2010_2019 = agg_year_sat_2010_2019[
        (agg_year_sat_2010_2019['YEAR'] > 2009) & (agg_year_sat_2010_2019['YEAR'] < 2020)]
    agg_year_sun_2010_2019 = agg_year_sun_2010_2019[
        (agg_year_sun_2010_2019['YEAR'] > 2009) & (agg_year_sun_2010_2019['YEAR'] < 2020)]

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the years 2020 - 2022.
    agg_year_wd_2020_2022, agg_year_sat_2020_2022, agg_year_sun_2020_2022 = agg_year_wd.copy(), \
        agg_year_sat.copy(), agg_year_sun.copy()

    agg_year_wd_2020_2022 = agg_year_wd_2020_2022[
        agg_year_wd_2020_2022['YEAR'].isin([2020, 2021, 2022])]
    agg_year_sat_2020_2022 = agg_year_sat_2020_2022[
        agg_year_sat_2020_2022['YEAR'].isin([2020, 2021, 2022])]
    agg_year_sun_2020_2022 = agg_year_sun_2020_2022[
        agg_year_sun_2020_2022['YEAR'].isin([2020, 2021, 2022])]

    # Add a rank column based off of ridership.
    ts_dfs = []

    for df in [agg_year_wd, agg_year_sat, agg_year_sun]:
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
    ts_bc_dfs = change_column_datatype(
        df_list=[agg_year_wd,
                 agg_year_sat,
                 agg_year_sun,
                 agg_year_wd_1999_2009,
                 agg_year_sat_1999_2009,
                 agg_year_sun_1999_2009,
                 agg_year_wd_2010_2019,
                 agg_year_sat_2010_2019,
                 agg_year_sun_2010_2019,
                 agg_year_wd_2020_2022,
                 agg_year_sat_2020_2022,
                 agg_year_sun_2020_2022],
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

    # Create absolute file paths for bar charts covering the first 10 months
    # of 2022.
    bc_2022_file_paths = create_absolute_file_paths(
        file_list=viz_file_names['bar_chart_args_2022'],
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

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the year 2022.
    # TODO: Create a function to do this.
    bus_data_2022 = cta_bus_data.copy()
    bus_data_2022 = bus_data_2022[bus_data_2022['YEAR'] == 2022]

    bus_data_2022_wd, bus_data_2022_sat, bus_data_2022_sun = bus_data_2022.copy(), \
        bus_data_2022.copy(), bus_data_2022.copy()

    bus_data_2022_wd = bus_data_2022_wd[
        bus_data_2022_wd['DAY_TYPE'] == 'Weekday']
    bus_data_2022_sat = bus_data_2022_sat[
        bus_data_2022_sat['DAY_TYPE'] == 'Saturday']
    bus_data_2022_sun = bus_data_2022_sun[
        bus_data_2022_sun['DAY_TYPE'] == 'Sunday - Holiday']

    bc_2022_dfs = [bus_data_2022_wd, bus_data_2022_sat, bus_data_2022_sun]

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (1999-2022)-----------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2010 (Weekday, Saturday, Sunday)
    # - 2011-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    llogging.info(
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
    # ---CREATE STACKED BAR CHARTS FOR ROUTES BY RIDERSHIP IN 2022------------
    # ------------------------------------------------------------------------
    # Bar charts are stacked by month for the first ten months of 2022 (data
    # for November and December is unavailable).
    #
    # -Weekday ridership: 2022
    # -Saturday ridership: 2022
    # -Sunday ridership: 2022
    # ------------------------------------------------------------------------

    logging.info("Creating heatmaps for routes by ridership in 2022")
    for df, op in zip(bc_2022_dfs, bc_2022_file_paths):

        create_barchart(
            data=df,
            output_path=op,
            x_value=barchart_args_2022.x_value,
            y_value=barchart_args_2022.y_value,
            x_value_type=barchart_args_2022.x_value_type,
            y_value_type=barchart_args_2022.y_value_type,
            color_values=barchart_args_2022.color_values,
            title=barchart_args_2022.title,
            scheme=barchart_args_2022.scheme,
            sort_order=barchart_args_2022.sort_order)

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
