"""
Description: File for storing recurring settings
"""

from dataclasses import dataclass

@dataclass
class HeatmapArguments:
    x_value: str = 'MONTH'
    y_value: str = 'YEAR'
    color_values: str = 'AVG_RIDES'
    facet_values: str = 'ROUTE'
    facet_columns: int = 3
    output_file: str = 'ridership_heatmap.png'

@dataclass
class HeatmapArguments_1999_2010(HeatmapArguments):
    output_file: str = 'ridership_heatmap_1999_2010.png'

@dataclass
class HeatmapArguments_2011_2022(HeatmapArguments):
    output_file: str = 'ridership_heatmap_2011_2022.png'
