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

import constants as cst
from data_processing import change_column_datatype
from file_io import create_absolute_file_paths
from visualizations import (create_barchart, create_bumpchart, create_heatmap)


if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

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
    parser.add_argument(
        '--day_type',
        required=True,
        choices=['Weekday', 'Saturday', 'Sunday - Holiday'],
        type=str,
        help='The type of day to create plots for. Must be one of Weekday, '
             'Saturday or Sunday - Holiday')
    parser.add_argument(
        '--routes',
        required=False,
        type=str,
        nargs='*',
        help='List of routes to create plots for. Plots will be created for '
             'all routes if this argument is not specified.')

    args = parser.parse_args()

    bus_data_path = args.bus_data_path
    output_dir = args.output_dir
    day_type = args.day_type
    routes = args.routes

    # ------------------------------------------------------------------------
    # ---INITIALIZE CONSTANT ARGUMENTS----------------------------------------
    # ------------------------------------------------------------------------

    bus_data_args = cst.BusDataArguments()
    barchart_args = cst.BarChartArguments()
    barchart_args_2022 = cst.BarChartArguments_2022()
    weekday_barchart_args_2022 = cst.WeekdayBarChartArguments_2022()
    saturday_barchart_args_2022 = cst.SaturdayBarChartArguments_2022()
    sunday_barchart_args_2022 = cst.SundayBarChartArguments_2022()
    weekday_barchart_args_1999_2022 = cst.WeekdayBarChartArguments_1999_2022()
    saturday_barchart_args_1999_2022 = cst.SaturdayBarChartArguments_1999_2022()
    sunday_barchart_args_1999_2022 = cst.SundayBarChartArguments_1999_2022()
    weekday_barchart_args_1999_2009 = cst.WeekdayBarChartArguments_1999_2009()
    saturday_barchart_args_1999_2009 = cst.SaturdayBarChartArguments_1999_2009()
    sunday_barchart_args_1999_2009 = cst.SundayBarChartArguments_1999_2009()
    weekday_barchart_args_2010_2019 = cst.WeekdayBarChartArguments_2010_2019()
    saturday_barchart_args_2010_2019 = cst.SaturdayBarChartArguments_2010_2019()
    sunday_barchart_args_2010_2019 = cst.SundayBarChartArguments_2010_2019()
    weekday_barchart_args_2020_2022 = cst.WeekdayBarChartArguments_2020_2022()
    saturday_barchart_args_2020_2022 = cst.SaturdayBarChartArguments_2020_2022()
    sunday_barchart_args_2020_2022 = cst.SundayBarChartArguments_2020_2022()
    bumpchart_args = cst.BumpChartArguments()
    weekday_bumpchart_args = cst.WeekdayBumpChartArguments()
    saturday_bumpchart_args = cst.SaturdayBumpChartArguments()
    sunday_bumpchart_args = cst.SundayBumpChartArguments()
    heatmap_args = cst.HeatmapArguments()
    heatmap_args_1999_2010 = cst.HeatmapArguments_1999_2010()
    heatmap_args_2011_2022 = cst.HeatmapArguments_2011_2022()

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
    wd_rankings, sat_rankings, sun_rankings = agg_year_wd.copy(), \
        agg_year_sat.copy(), agg_year_sun.copy()

    wd_rankings['RANK'] = wd_rankings.groupby('YEAR')[
        'AVG_RIDES'].rank(ascending=False)
    sat_rankings['RANK'] = sat_rankings.groupby('YEAR')[
        'AVG_RIDES'].rank(ascending=False)
    sun_rankings['RANK'] = sun_rankings.groupby('YEAR')[
        'AVG_RIDES'].rank(ascending=False)

    # Subset dataframe so that only the top 10 bus routes per year are present
    wd_rankings = wd_rankings[wd_rankings['RANK'] <= 10]
    sat_rankings = sat_rankings[sat_rankings['RANK'] <= 10]
    sun_rankings = sun_rankings[sun_rankings['RANK'] <= 10]

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
    # plot readability for bump charts representing more than one year of data.
    # Please note that this must be executed after subsetting each dataframe
    # by the relevant years to avoid raising a TypeError.
    ts_bpc_dfs = change_column_datatype(
        df_list=[wd_rankings, sat_rankings, sun_rankings],
        col='YEAR',
        datatype='str')

    # Create absolute file paths for bar charts covering the first 10 months
    # of 2022.
    bc_2022_file_paths = create_absolute_file_paths(
        file_list=[weekday_barchart_args_2022.output_file,
                   saturday_barchart_args_2022.output_file,
                   sunday_barchart_args_2022.output_file],
        file_path=output_dir)

    # Create absolute file paths for bar charts covering multiple years
    ts_bc_file_paths = create_absolute_file_paths(
        file_list=[weekday_barchart_args_1999_2022.output_file,
                   saturday_barchart_args_1999_2022.output_file,
                   sunday_barchart_args_1999_2022.output_file,
                   weekday_barchart_args_1999_2009.output_file,
                   saturday_barchart_args_1999_2009.output_file,
                   sunday_barchart_args_1999_2009.output_file,
                   weekday_barchart_args_2010_2019.output_file,
                   saturday_barchart_args_2010_2019.output_file,
                   sunday_barchart_args_2010_2019.output_file,
                   weekday_barchart_args_2020_2022.output_file,
                   saturday_barchart_args_2020_2022.output_file,
                   sunday_barchart_args_2020_2022.output_file],
        file_path=output_dir)

    # Create absolute file paths for bump charts covering 1999 to 2022
    bpc_file_paths = create_absolute_file_paths(
        file_list=[weekday_bumpchart_args.output_file,
                   saturday_bumpchart_args.output_file,
                   sunday_bumpchart_args.output_file],
        file_path=output_dir)

    # Create subsets for weekday, saturday and sunday - holiday ridership for
    # the year 2022.
    # TODO: Create a function to do this.
    bus_data_2022 = cta_bus_data.copy()
    bus_data_2022 = bus_data_2022[bus_data_2022['YEAR'] == 2022]
    bus_data_2022_wd, bus_data_2022_sat, bus_data_2022_sun = bus_data_2022.copy(), \
        bus_data_2022.copy(), bus_data_2022.copy()
    bus_data_2022_wd = bus_data_2022[bus_data_2022['DAY_TYPE'] == 'Weekday']
    bus_data_2022_sat = bus_data_2022[bus_data_2022['DAY_TYPE'] == 'Saturday']
    bus_data_2022_sun = bus_data_2022[
        bus_data_2022['DAY_TYPE'] == 'Sunday - Holiday']

    bc_2022_dfs = [bus_data_2022_wd, bus_data_2022_sat, bus_data_2022_sun]

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (1999-2022)-----------
    # ------------------------------------------------------------------------
    # Currently heatmaps are only for weekday ridership
    # TODO: Create heatmaps for saturdays and sundays - holidays
    # ------------------------------------------------------------------------

    # Heatmap by weekday ridership, month and year.
    logging.info("Preparing to create heatmap for the years 1999 to 2022")
    logging.info("Subsetting data")
    hm_rmy_data = cta_bus_data.copy()

    # Optionally subset by route if specific route numbers are specified upon
    # execution of this script. if no routes are specified, make plots for all
    # routes.
    if routes:
        hm_rmy_data = hm_rmy_data[
            hm_rmy_data['ROUTE'].isin(routes)]

    # Subset by trip type (e.g. Weekday, Saturday, Sunday - Holiday).
    hm_rmy_data = hm_rmy_data[hm_rmy_data['DAY_TYPE'] == day_type]

    # Create output path for heatmap
    heatmap_output_path = f'{output_dir}{heatmap_args.output_file}'

    logging.info("Creating Heatmap for the years 1999 to 2022")
    create_heatmap(
        data=hm_rmy_data,
        output_path=heatmap_output_path,
        x_value=heatmap_args.x_value,
        y_value=heatmap_args.y_value,
        color_values=heatmap_args.color_values,
        facet_values=heatmap_args.facet_values,
        facet_columns=heatmap_args.facet_columns,
        x_axis_sort_order=heatmap_args.x_axis_sort_order)

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (1999-2010)-----------
    # ------------------------------------------------------------------------
    # Currently heatmaps are only for weekday ridership
    # TODO: Create heatmaps for saturdays and sundays - holidays
    # ------------------------------------------------------------------------

    # Heatmap by weekday ridership, month and year.
    logging.info("Preparing to create heatmap for the years 1999 to 2010")
    logging.info("Subsetting data")
    hm_rmy_data_1999_2010 = hm_rmy_data.copy()
    hm_rmy_data_1999_2010 = hm_rmy_data_1999_2010[
        hm_rmy_data_1999_2010['YEAR'] < 2011]

    # Create output path for heatmap
    heatmap_output_path = f'{output_dir}{heatmap_args_1999_2010.output_file}'

    logging.info("Creating Heatmap for the years 1999 to 2010")
    create_heatmap(
        data=hm_rmy_data_1999_2010,
        output_path=heatmap_output_path,
        x_value=heatmap_args_1999_2010.x_value,
        y_value=heatmap_args_1999_2010.y_value,
        color_values=heatmap_args_1999_2010.color_values,
        facet_values=heatmap_args_1999_2010.facet_values,
        facet_columns=heatmap_args_1999_2010.facet_columns,
        x_axis_sort_order=heatmap_args_1999_2010.x_axis_sort_order)

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (2011-2022)-----------
    # ------------------------------------------------------------------------
    # Currently heatmaps are only for weekday ridership
    # TODO: Create heatmaps for saturdays and sundays - holidays
    # ------------------------------------------------------------------------

    # Heatmap by weekday ridership, month and year.
    logging.info("Preparing to create heatmap for the years 2011 to 2022")
    logging.info("Subsetting data")
    hm_rmy_data_2011_2022 = hm_rmy_data.copy()
    hm_rmy_data_2011_2022 = hm_rmy_data_2011_2022[
        hm_rmy_data_2011_2022['YEAR'] > 2010]

    # Create output path for heatmap
    heatmap_output_path = f'{output_dir}{heatmap_args_2011_2022.output_file}'

    logging.info("Creating Heatmap for the years 2011 to 2022")
    create_heatmap(
        data=hm_rmy_data_2011_2022,
        output_path=heatmap_output_path,
        x_value=heatmap_args_2011_2022.x_value,
        y_value=heatmap_args_2011_2022.y_value,
        color_values=heatmap_args_2011_2022.color_values,
        facet_values=heatmap_args_2011_2022.facet_values,
        facet_columns=heatmap_args_2011_2022.facet_columns,
        x_axis_sort_order=heatmap_args_2011_2022.x_axis_sort_order)

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

    for df, op in zip(bc_2022_dfs, bc_2022_file_paths):

        create_barchart(
            data=df,
            output_path=op,
            x_value=barchart_args.x_value,
            y_value=barchart_args.y_value,
            color_values=barchart_args_2022.color_values,
            title=barchart_args.title,
            sort_order=barchart_args_2022.sort_order)

    # ------------------------------------------------------------------------
    # ---CREATE STACKED BAR CHARTS FOR ROUTES BY RIDERSHIP--------------------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2009 (Weekday, Saturday, Sunday)
    # - 2010-2019 (Weekday, Saturday, Sunday)
    # - 2020-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    for df, op in zip(ts_bc_dfs, ts_bc_file_paths):

        create_barchart(
            data=df,
            output_path=op,
            x_value=barchart_args.x_value,
            y_value=barchart_args.y_value,
            color_values=barchart_args.color_values,
            title=barchart_args.title)

    # ------------------------------------------------------------------------
    # ---CREATE BUMP CHARTS FOR ROUTES BY RIDERSHIP AND YEAR------------------
    # ------------------------------------------------------------------------
    # - 1999-2022 (Weekday, Saturday, Sunday)
    # - 1999-2009 (Weekday, Saturday, Sunday)
    # - 2010-2019 (Weekday, Saturday, Sunday)
    # - 2020-2022 (Weekday, Saturday, Sunday)
    # ------------------------------------------------------------------------

    for df, op in zip(ts_bpc_dfs, bpc_file_paths):
        create_bumpchart(
            data=df,
            output_path=op,
            x_value=bumpchart_args.x_value,
            y_value=bumpchart_args.y_value,
            color_values=bumpchart_args.color_values,
            title=bumpchart_args.title,
            scheme=bumpchart_args.scheme)
