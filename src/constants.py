"""
Description: File for storing recurring settings
"""

from dataclasses import (dataclass, field)
from typing import TypedDict

viz_file_names = {
    'bar_chart_args': ['weekday_ridership_barchart_2001_2022.png',
                       'saturday_ridership_barchart_2001_2022.png',
                       'sunday_ridership_barchart_2001_2022.png',
                       'weekday_ridership_barchart_2001_2010.png',
                       'saturday_ridership_barchart_2001_2010.png',
                       'sunday_ridership_barchart_2001_2010.png',
                       'weekday_ridership_barchart_2011_2019.png',
                       'saturday_ridership_barchart_2011_2019.png',
                       'sunday_ridership_barchart_2011_2019.png',
                       'weekday_ridership_barchart_2020_2022.png',
                       'saturday_ridership_barchart_2020_2022.png',
                       'sunday_ridership_barchart_2020_2022.png'],
    'bar_chart_args_2022': ['weekday_ridership_barchart_2022.png',
                            'saturday_ridership_barchart_2022.png',
                            'sunday_ridership_barchart_2022.png'],
    'bump_chart_args': ['weekday_ridership_bump_chart.png',
                        'saturday_ridership_bump_chart.png',
                        'sunday_ridership_bump_chart.png'],
    'line_chart_args': ['weekday_ridership_time_series_analysis.png',
                        'saturday_ridership_time_series_analysis.png',
                        'sunday_ridership_time_series_analysis.png'],
    'heatmap_args': ['weekday_ridership_heatmap_2001_2010.png',
                     'saturday_ridership_heatmap_2001_2010.png',
                     'sunday_ridership_heatmap_2001_2010.png',
                     'weekday_ridership_heatmap_2011_2022.png',
                     'saturday_ridership_heatmap_2011_2022.png',
                     'sunday_ridership_heatmap_2011_2022.png',
                     'weekday_ridership_heatmap_2001_2022.png',
                     'saturday_ridership_heatmap_2001_2022.png',
                     'sunday_ridership_heatmap_2001_2022.png']}

@dataclass
class Months(TypedDict):
   name_numeric: str
   name_alpha: str

@dataclass
class DateTypes(TypedDict):
    long_numeric: str
    short_numeric: str

@dataclass
class DayTypes(TypedDict):
   type_sort: str
   type_long: str

@dataclass
class BusDataArguments:
    sort_form_to_long_form_numeric_dates: DateTypes = field(
        default_factory=lambda: {
            '01': '1',
            '02': '2',
            '03': '3',
            '04': '4',
            '05': '5',
            '06': '6',
            '07': '7',
            '08': '8',
            '09': '9'})
    alpha_to_numeric_months: Months = field(default_factory=lambda: {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'})
    sort_form_to_long_form_day_types: DayTypes = field(
        default_factory=lambda: {
            'W': 'Weekday',
            'A': 'Saturday',
            'U': 'Sunday - Holiday'})

@dataclass
class BarChartArguments:
    x_value: str = 'RIDES'
    y_value: str = 'ROUTE'
    x_value_type: str = 'quantitative'
    y_value_type: str = 'ordinal'
    color_values: str = 'YEAR'
    scheme: str = 'tableau20'
    title: str = "Number of rides per CTA bus route"

@dataclass
class BarChartArguments_2022(BarChartArguments):
    color_values: str = 'MONTH'
    sort_order: list[str] = field(default_factory=lambda:[
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
class BumpChartArguments:
    x_value: str = 'YEAR'
    y_value: str = 'RANK'
    x_value_type: str = 'ordinal'
    y_value_type: str = 'ordinal'
    color_values: str = 'ROUTE'
    title: str = "Chicago Transit Authority bus routes with the highest " \
                 "number of riders (2001-2022)"
    scheme: str = 'category20'
    value_col: str = 'RIDES'
    rank_col: str = 'RANK'
    group_col: list[str] = field(default_factory=lambda:['YEAR'])
    num_rankings: int = 10

@dataclass
class LineChartArguments:
    x_value: str = 'YEAR'
    y_value: str = 'RIDES'
    x_value_type: str = 'ordinal'
    y_value_type: str = 'quantitative'
    color_values: str = 'ROUTE'
    title: str = "Chicago Transit Authority bus routes with the highest " \
                 "number of riders (2001-2022)"
    scheme: str = 'category20'
    value_col: str = 'RIDES'
    rank_col: str = 'RANK'
    group_col: list[str] = field(default_factory=lambda:['YEAR'])
    num_rankings: int = 10

@dataclass
class HeatmapArguments:
    x_value: str = 'MONTH'
    x_value_type: str = 'ordinal'
    y_value: str = 'YEAR'
    y_value_type: str = 'ordinal'
    color_values: str = 'RIDES'
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
