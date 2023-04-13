"""
Description: File for storing recurring settings
"""

from dataclasses import dataclass
from dataclasses import field

@dataclass
class HeatmapArguments:
    x_value: str = 'MONTH'
    y_value: str = 'YEAR'
    color_values: str = 'AVG_RIDES'
    facet_values: str = 'ROUTE'
    facet_columns: int = 3
    output_file: str = 'ridership_heatmap.png'
    x_axis_sort_order: list[str] = field(default_factory=lambda: [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'])

@dataclass
class HeatmapArguments_1999_2010(HeatmapArguments):
    output_file: str = 'ridership_heatmap_1999_2010.png'

@dataclass
class HeatmapArguments_2011_2022(HeatmapArguments):
    output_file: str = 'ridership_heatmap_2011_2022.png'
