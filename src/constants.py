"""
Description: File for storing recurring settings
"""

from dataclasses import (dataclass, field)
from typing import TypedDict

viz_file_names = {
    'bar_chart_args': ['weekday_ridership_barchart_1999_2022.png',
                       'saturday_ridership_barchart_1999_2022.png',
                       'sunday_ridership_barchart_1999_2022.png',
                       'weekday_ridership_barchart_1999_2009.png',
                       'saturday_ridership_barchart_1999_2009.png',
                       'sunday_ridership_barchart_1999_2009.png',
                       'weekday_ridership_barchart_2010_2019.png',
                       'saturday_ridership_barchart_2010_2019.png',
                       'sunday_ridership_barchart_2010_2019.png',
                       'weekday_ridership_barchart_2020_2022.png',
                       'saturday_ridership_barchart_2020_2022.png',
                       'sunday_ridership_barchart_2020_2022.png'],
    'bump_chart_args': ['weekday_ridership_bump_chart.png',
                        'saturday_ridership_bump_chart.png',
                        'sunday_ridership_bump_chart.png'],
    'line_chart_args': ['weekday_ridership_time_series_analysis.png',
                        'saturday_ridership_time_series_analysis.png',
                        'sunday_ridership_time_series_analysis.png'],
    'heatmap_args': ['weekday_ridership_heatmap_1999_2022_medium.png',
                     'saturday_ridership_heatmap_1999_2022_medium.png',
                     'sunday_ridership_heatmap_1999_2022_medium.png',
                     'weekday_ridership_heatmap_1999_2022_low.png',
                     'saturday_ridership_heatmap_1999_2022_low.png',
                     'sunday_ridership_heatmap_1999_2022_low.png',
                     'weekday_ridership_heatmap_1999_2022_high.png',
                     'saturday_ridership_heatmap_1999_2022_high.png',
                     'sunday_ridership_heatmap_1999_2022_high.png',
                     'weekday_ridership_heatmap_1999_2009_medium.png',
                     'saturday_ridership_heatmap_1999_2009_medium.png',
                     'sunday_ridership_heatmap_1999_2009_medium.png',
                     'weekday_ridership_heatmap_1999_2009_low.png',
                     'saturday_ridership_heatmap_1999_2009_low.png',
                     'sunday_ridership_heatmap_1999_2009_low.png',
                     'weekday_ridership_heatmap_1999_2009_high.png',
                     'saturday_ridership_heatmap_1999_2009_high.png',
                     'sunday_ridership_heatmap_1999_2009_high.png',
                     'weekday_ridership_heatmap_2010_2022_medium.png',
                     'saturday_ridership_heatmap_2010_2022_medium.png',
                     'sunday_ridership_heatmap_2010_2022_medium.png',
                     'weekday_ridership_heatmap_2010_2022_low.png',
                     'saturday_ridership_heatmap_2010_2022_low.png',
                     'sunday_ridership_heatmap_2010_2022_low.png',
                     'weekday_ridership_heatmap_2010_2022_high.png',
                     'saturday_ridership_heatmap_2010_2022_high.png',
                     'sunday_ridership_heatmap_2010_2022_high.png'],
    'route_count_bar_chart_args': ['route_count_1999_2022.png']}

@dataclass
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
    x_value_type: str = 'quantitative'
    y_value_type: str = 'ordinal'
    color_values: str = 'YEAR'
    scheme: str = 'tableau20'
    title: str = "Number of rides per CTA bus route"

@dataclass
class BumpChartArguments:
    x_value: str = 'YEAR'
    y_value: str = 'RANK'
    x_value_type: str = 'ordinal'
    y_value_type: str = 'ordinal'
    color_values: str = 'ROUTE'
    title: str = "Chicago Transit Authority bus routes with the highest " \
                 "number of riders (1999-2022)"
    scheme: str = 'category20'
    value_col: str = 'AVG_RIDES'
    rank_col: str = 'RANK'
    group_col: list[str] = field(default_factory=lambda: ['YEAR'])
    num_rankings: int = 10

@dataclass
class LineChartArguments:
    x_value: str = 'YEAR'
    y_value: str = 'AVG_RIDES'
    x_value_type: str = 'ordinal'
    y_value_type: str = 'quantitative'
    color_values: str = 'ROUTE'
    title: str = "Chicago Transit Authority bus routes with the highest " \
                 "number of riders (1999-2022)"
    scheme: str = 'category20'
    value_col: str = 'AVG_RIDES'
    rank_col: str = 'RANK'
    group_col: list[str] = field(default_factory=lambda: ['YEAR'])
    num_rankings: int = 10

@dataclass
class HeatmapArguments:
    x_value: str = 'MONTH'
    x_value_type: str = 'ordinal'
    y_value: str = 'YEAR'
    y_value_type: str = 'ordinal'
    color_values: str = 'AVG_RIDES'
    facet_values: str = 'ROUTE'
    facet_columns: int = 3
    scheme: str = 'yelloworangebrown'
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
class RouteCountArguments:
    route_dims: list[str] = field(default_factory=lambda: ['ROUTE', 'YEAR'])
    count_dim: str = 'YEAR'
    count_col: str = 'COUNT'

# @dataclass
# class WaterFallChartArguments:
#     x_value: str = 'YEAR'
#     y_value: str = 'COUNT'
