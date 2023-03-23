"""
Description: Executes transportation data analysis and creates all
visualizations.

# ----------------------------------------------------------------------------
# ---LOAD LIBRARIES-----------------------------------------------------------
# ----------------------------------------------------------------------------

import argparse
import logging

# ----------------------------------------------------------------------------
# ---SET UP LOGGING-----------------------------------------------------------
# ----------------------------------------------------------------------------

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Arguments for visualizing data')
    parser.add_argument(
        '--bus_data_path',
        required=True,
        type=str,
        help='The absolute file path to the bus data being analyzed')

    args = parser.parse_args()

    bus_data_path = args.bus_data_path




