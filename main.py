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

from constants import (BusDataArguments,
                       BarChartArguments,
                       BarChartArguments_2022,
                       WeekdayBarChartArguments_2022,
                       SaturdayBarChartArguments_2022,
                       SundayBarChartArguments_2022,
                       WeekdayBarChartArguments_1999_2022,
                       SaturdayBarChartArguments_1999_2022,
                       SundayBarChartArguments_1999_2022,
                       WeekdayBarChartArguments_2020_2022,
                       SaturdayBarChartArguments_2020_2022,
                       SundayBarChartArguments_2020_2022,
                       HeatmapArguments,
                       HeatmapArguments_1999_2010,
                       HeatmapArguments_2011_2022)
from data_processing import (change_column_datatype,
                             create_absolute_file_paths)
from visualizations import (create_barchart, create_heatmap)


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


if __name__ == "__main__":

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

    bus_data_args = BusDataArguments()
    barchart_args = BarChartArguments()
    barchart_args_2022 = BarChartArguments_2022()
    weekday_barchart_args_2022 = WeekdayBarChartArguments_2022()
    saturday_barchart_args_2022 = SaturdayBarChartArguments_2022()
    sunday_barchart_args_2022 = SundayBarChartArguments_2022()
    weekday_barchart_args_1999_2022 = WeekdayBarChartArguments_1999_2022()
    saturday_barchart_args_1999_2022 = SaturdayBarChartArguments_1999_2022()
    sunday_barchart_args_1999_2022 = SundayBarChartArguments_1999_2022()
    weekday_barchart_args_2020_2022 = WeekdayBarChartArguments_2020_2022()
    saturday_barchart_args_2020_2022 = SaturdayBarChartArguments_2020_2022()
    sunday_barchart_args_2020_2022 = SundayBarChartArguments_2020_2022()
    heatmap_args = HeatmapArguments()
    heatmap_args_1999_2010 = HeatmapArguments_1999_2010()
    heatmap_args_2011_2022 = HeatmapArguments_2011_2022()

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
    # the years 2020 - 2022.
    agg_year_wd_2020_2022, agg_year_sat_2020_2022, agg_year_sun_2020_2022 = agg_year_wd.copy(), \
        agg_year_sat.copy(), agg_year_sun.copy()

    agg_year_wd_2020_2022 = agg_year_wd_2020_2022[
        agg_year_wd_2020_2022['YEAR'].isin([2020, 2021, 2022])]
    agg_year_sat_2020_2022 = agg_year_sat_2020_2022[
        agg_year_sat_2020_2022['YEAR'].isin([2020, 2021, 2022])]
    agg_year_sun_2020_2022 = agg_year_sun_2020_2022[
        agg_year_sun_2020_2022['YEAR'].isin([2020, 2021, 2022])]

    # Change values in the "YEAR" column from integers to strings to improve
    # plot readability for barcharts representing more than one year of data.
    # Please note that this must be executed after subsetting each dataframe
    # by the relevant years to avoid raising a TypeError.
    ts_bc_dfs = change_column_datatype(
        df_list=[agg_year_wd,
                 agg_year_sat,
                 agg_year_sun,
                 agg_year_wd_2020_2022,
                 agg_year_sat_2020_2022,
                 agg_year_sun_2020_2022],
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
                   weekday_barchart_args_2020_2022.output_file,
                   saturday_barchart_args_2020_2022.output_file,
                   sunday_barchart_args_2020_2022.output_file],
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
    # TODO: Determine how much of this code can be moved to functions in
    #   data_processing.py
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
    # TODO: Determine how much of this code can be moved to functions in
    #   data_processing.py
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
    # TODO: Determine how much of this code can be moved to functions in
    # data_processing.py
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
    # ---CREATE PLOTS FOR THE TOP TEN ROUTES BY SUNDAY RIDERSHIP IN 2022------
    # ------------------------------------------------------------------------
    # TBD
    # ------------------------------------------------------------------------

    for df, op in zip(bc_2022_dfs, bc_2022_file_paths):

        create_barchart(
            data=df,
            output_path=op,
            x_value=barchart_args.x_value,
            y_value=barchart_args.y_value,
            color_values=barchart_args_2022.color_values,
            sort_order=barchart_args_2022.sort_order)

    # ------------------------------------------------------------------------
    # ---CREATE BARCHARTS FOR ROUTES BY RIDERSHIP-----------------------------
    # ------------------------------------------------------------------------
    # -Weekday ridership, 1999-2022
    # -Saturday ridership, 1999-2022
    # -Sunday ridership, 1999-2022
    # -Weekday ridership, 2020-2022
    # -Saturday ridership, 2020-2022
    # -Sunday ridership, 2020-2022
    # ------------------------------------------------------------------------

    for df, op in zip(ts_bc_dfs, ts_bc_file_paths):

        create_barchart(
            data=df,
            output_path=op,
            x_value=barchart_args.x_value,
            y_value=barchart_args.y_value,
            color_values=barchart_args.color_values)
