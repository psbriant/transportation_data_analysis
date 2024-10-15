"""
Description: File for storing recurring settings
"""

from dataclasses import (dataclass, field)
from typing import TypedDict

viz_file_names = {
    'bar_chart_args': ['weekday_ridership_barchart_1999_2023.html',
                       'saturday_ridership_barchart_1999_2023.html',
                       'sunday_ridership_barchart_1999_2023.html',
                       'weekday_ridership_barchart_1999_2009.html',
                       'saturday_ridership_barchart_1999_2009.html',
                       'sunday_ridership_barchart_1999_2009.html',
                       'weekday_ridership_barchart_2010_2019.html',
                       'saturday_ridership_barchart_2010_2019.html',
                       'sunday_ridership_barchart_2010_2019.html',
                       'weekday_ridership_barchart_2020_2023.html',
                       'saturday_ridership_barchart_2020_2023.html',
                       'sunday_ridership_barchart_2020_2023.html'],
    'ridership_recovery_args': ['saturday_ridership_recovery_barchart.html',
                                'sunday_ridership_recovery_barchart.html',
                                'weekday_ridership_recovery_barchart.html'],
    'bump_chart_args': ['weekday_ridership_bump_chart.html',
                        'saturday_ridership_bump_chart.html',
                        'sunday_ridership_bump_chart.html'],
    'line_chart_args': ['weekday_ridership_time_series_analysis.html',
                        'saturday_ridership_time_series_analysis.html',
                        'sunday_ridership_time_series_analysis.html'],
    'heatmap_args': ['weekday_ridership_heatmap_1999_2023_medium.html',
                     'saturday_ridership_heatmap_1999_2023_medium.html',
                     'sunday_ridership_heatmap_1999_2023_medium.html',
                     'weekday_ridership_heatmap_1999_2023_low.html',
                     'saturday_ridership_heatmap_1999_2023_low.html',
                     'sunday_ridership_heatmap_1999_2023_low.html',
                     'weekday_ridership_heatmap_1999_2023_high.html',
                     'saturday_ridership_heatmap_1999_2023_high.html',
                     'sunday_ridership_heatmap_1999_2023_high.html',
                     'weekday_ridership_heatmap_1999_2009_medium.html',
                     'saturday_ridership_heatmap_1999_2009_medium.html',
                     'sunday_ridership_heatmap_1999_2009_medium.html',
                     'weekday_ridership_heatmap_1999_2009_low.html',
                     'saturday_ridership_heatmap_1999_2009_low.html',
                     'sunday_ridership_heatmap_1999_2009_low.html',
                     'weekday_ridership_heatmap_1999_2009_high.html',
                     'saturday_ridership_heatmap_1999_2009_high.html',
                     'sunday_ridership_heatmap_1999_2009_high.html',
                     'weekday_ridership_heatmap_2010_2023_medium.html',
                     'saturday_ridership_heatmap_2010_2023_medium.html',
                     'sunday_ridership_heatmap_2010_2023_medium.html',
                     'weekday_ridership_heatmap_2010_2023_low.html',
                     'saturday_ridership_heatmap_2010_2023_low.html',
                     'sunday_ridership_heatmap_2010_2023_low.html',
                     'weekday_ridership_heatmap_2010_2023_high.html',
                     'saturday_ridership_heatmap_2010_2023_high.html',
                     'sunday_ridership_heatmap_2010_2023_high.html'],
    'route_count_area_chart_args': ['route_count_1999_2023.html']}


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
    x_axis_title: str = 'Average rides'
    y_axis_title: str = 'Route'
    color_title: str = 'Year'
    color_values: str = 'YEAR'
    scheme: str = 'tableau20'
    title: str = "Number of rides per CTA bus route"


@dataclass
class BumpChartArguments:
    x_value: str = 'YEAR'
    y_value: str = 'RANK'
    x_value_type: str = 'ordinal'
    y_value_type: str = 'ordinal'
    x_axis_title: str = 'Year'
    y_axis_title: str = 'Rank'
    color_title: str = 'Route'
    color_values: str = 'ROUTE'
    title: str = "Chicago Transit Authority bus routes with the highest " \
                 "number of riders (1999-2023)"
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
    x_axis_title: str = 'Year'
    y_axis_title: str = 'Average rides'
    color_title: str = 'Route'
    color_values: str = 'ROUTE'
    title: str = "Chicago Transit Authority bus routes with the highest " \
                 "number of riders (1999-2023)"
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
    x_axis_title: str = 'Month'
    y_axis_title: str = 'Year'
    color_title: str = 'Average rides'
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
    x_value: str = 'YEAR'
    y_value: str = 'COUNT'
    x_value_type: str = 'ordinal'
    y_value_type: str = 'quantitative'
    x_axis_title: str = 'Year'
    y_axis_title: str = 'Count'
    color: str = '#8856a7'
    title: str = ("Trends in the number of CTA bus routes in operation from "
                  "1999 to 2023")


@dataclass
class RidershipRecoveryArguments:
    x_value: str = 'PERCENT_RECOVERED'
    y_value: str = 'ROUTE'
    x_value_type: str = 'quantitative'
    y_value_type: str = 'ordinal'
    x_axis_title: str = 'Percent recovered'
    y_axis_title: str = 'Route'
    color_title: str = 'Day type'
    color_values: str = 'DAY_TYPE'
    scheme: str = 'tableau20'
    title: str = ("Percent of ridership recovery between 2019 and 2023 by "
                  "CTA bus route")
