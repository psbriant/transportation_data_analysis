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

from constants import (HeatmapArguments,
                       HeatmapArguments_1999_2010,
                       HeatmapArguments_2011_2022)
from visualizations import (create_heatmap)


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
    cta_bus_data = cta_bus_data.replace(
        {1: 'January',
         2: 'February',
         3: 'March',
         4: 'April',
         5: 'May',
         6: 'June',
         7: 'July',
         8: 'August',
         9: 'September',
         10: 'October',
         11: 'November',
         12: 'December'})

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (1999-2022)-----------
    # ------------------------------------------------------------------------
    # Currently heatmaps are only for weekday ridership
    # TODO: Determine how much of this code can be moved to functions in
    # data_processing.py
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
    # data_processing.py
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
    # ---CREATE PLOTS FOR THE TOP TEN ROUTES BY SATURDAY RIDERSHIP IN 2022----
    # ------------------------------------------------------------------------
    # TBD
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # ---CREATE PLOTS FOR THE TOP TEN ROUTES BY SUNDAY RIDERSHIP IN 2022------
    # ------------------------------------------------------------------------
    # TBD
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # ---CREATE PLOTS FOR THE TOP TEN ROUTES BY SATURDAY RIDERSHIP (1999-2022)
    # ------------------------------------------------------------------------
    # TBD
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # ---CREATE PLOTS FOR THE TOP TEN ROUTES BY SUNDAY RIDERSHIP (1999-2022)--
    # ------------------------------------------------------------------------
    # TBD
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # ---CREATE PLOTS FOR THE TOP TEN ROUTES BY RIDERSHIP (1999-2022)---------
    # ------------------------------------------------------------------------
    # TBD
    # ------------------------------------------------------------------------
