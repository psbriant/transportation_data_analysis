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

from constants import (HeatmapArguments)
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

    args = parser.parse_args()

    bus_data_path = args.bus_data_path
    output_dir = args.output_dir

    # ------------------------------------------------------------------------
    # ---INITIALIZE CONSTANT ARGUMENTS----------------------------------------
    # ------------------------------------------------------------------------

    heatmap_args = HeatmapArguments()

    # ------------------------------------------------------------------------
    # ---LOAD DATASET---------------------------------------------------------
    # ------------------------------------------------------------------------

    logging.info("Loading data")
    cta_bus_data = pd.read_csv(bus_data_path, encoding='utf-8')

    # ------------------------------------------------------------------------
    # ---CREATE HEATMAP FOR RIDERSHIP BY MONTH AND YEAR (1999-2022)-----------
    # ------------------------------------------------------------------------
    # Currently heatmaps are only for weekday ridership
    # TODO: Determine how much of this code can be moved to functions in
    # data_processing.py
    # ------------------------------------------------------------------------

    # Heatmap by weekday ridership, month and year.
    hm_rmy_data = cta_bus_data.copy()
    hm_rmy_data = hm_rmy_data[hm_rmy_data['ROUTE'] == '1']
    hm_rmy_data = hm_rmy_data[hm_rmy_data['DAY_TYPE'] == 'Weekday']

    # Create output path for heatmap
    heatmap_output_path = f'{output_dir}{heatmap_args.output_file}'

    # TODO figure out how to declare these variables using constants.py.
    create_heatmap(
        data=hm_rmy_data,
        output_path=heatmap_output_path,
        data_index=heatmap_args.index,
        data_columns=heatmap_args.columns,
        data_values=heatmap_args.values)

    # ------------------------------------------------------------------------
    # ---CREATE PLOTS FOR THE TOP TEN ROUTES BY WEEKDAY RIDERSHIP (1999-2022)-
    # ------------------------------------------------------------------------
    # TBD
    # ------------------------------------------------------------------------

    # Create dataset for the top ten routes by weekday ridership from 1999 to
    # 2022 by copying, subsetting and aggregating the original CTA bus
    # ridership dataset.
    ttrwdr_1999_2022 = cta_bus_data.copy()
    # Subset to weekday ridership only
    ttrwdr_1999_2022 = ttrwdr_1999_2022[
        ttrwdr_1999_2022['DAY_TYPE'] == 'Weekday']
    # Test by subsetting for October
    ttrwdr_1999_2022 = ttrwdr_1999_2022[ttrwdr_1999_2022['MONTH'] == 10]
    # Test by subsetting for ten routes
    ttrwdr_1999_2022 = ttrwdr_1999_2022[ttrwdr_1999_2022['ROUTE'].isin(
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])]
    ttrwdr_1999_2022 = ttrwdr_1999_2022.drop(
        labels=['MONTH', 'DAY_TYPE'],
        axis=1)

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
