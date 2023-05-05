"""
Description: File for storing recurring settings
"""

from dataclasses import (dataclass, field)
from typing import TypedDict


class Months(TypedDict):
   name_numeric: int
   name_alpha: str

@dataclass
class BusDataArguments:
    alpha_to_numeric_months: Months = field(default_factory=lambda: {
        1: 'January',
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

@dataclass
class BarChartArguments:
    x_value: str = 'AVG_RIDES'
    y_value: str = 'ROUTE'
    color_values: str = 'YEAR'


@dataclass
class WeekdayBarChartArguments_2022(BarChartArguments):
    output_file: str = 'weekday_ridership_barchart_2022.png'
    color_values: str = 'MONTH'

@dataclass
class SaturdayBarChartArguments_2022(BarChartArguments):
    output_file: str = 'saturday_ridership_barchart_2022.png'
    color_values: str = 'MONTH'

@dataclass
class SundayBarChartArguments_2022(BarChartArguments):
    output_file: str = 'sunday_ridership_barchart_2022.png'
    color_values: str = 'MONTH'

@dataclass
class WeekdayBarChartArguments_1999_2022(BarChartArguments):
    output_file: str = 'weekday_ridership_barchart_1999_2022.png'

@dataclass
class SaturdayBarChartArguments_1999_2022(BarChartArguments):
    output_file: str = 'saturday_ridership_barchart_1999_2022.png'

@dataclass
class SundayBarChartArguments_1999_2022(BarChartArguments):
    output_file: str = 'sunday_ridership_barchart_1999_2022.png'


@dataclass
class WeekdayBarChartArguments_2020_2022(BarChartArguments):
    output_file: str = 'weekday_ridership_barchart_2020_2022.png'

@dataclass
class SaturdayBarChartArguments_2020_2022(BarChartArguments):
    output_file: str = 'saturday_ridership_barchart_2020_2022.png'

@dataclass
class SundayBarChartArguments_2020_2022(BarChartArguments):
    output_file: str = 'sunday_ridership_barchart_2020_2022.png'

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
