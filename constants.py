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
        'October'])

@dataclass
class WeekdayBarChartArguments_2022(BarChartArguments_2022):
    output_file: str = 'weekday_ridership_barchart_2022.png'

@dataclass
class SaturdayBarChartArguments_2022(BarChartArguments_2022):
    output_file: str = 'saturday_ridership_barchart_2022.png'

@dataclass
class SundayBarChartArguments_2022(BarChartArguments):
    output_file: str = 'sunday_ridership_barchart_2022.png'

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
class WeekdayBarChartArguments_1999_2009(BarChartArguments):
    output_file: str = 'weekday_ridership_barchart_1999_2009.png'

@dataclass
class SaturdayBarChartArguments_1999_2009(BarChartArguments):
    output_file: str = 'saturday_ridership_barchart_1999_2009.png'

@dataclass
class SundayBarChartArguments_1999_2009(BarChartArguments):
    output_file: str = 'sunday_ridership_barchart_1999_2009.png'

@dataclass
class WeekdayBarChartArguments_2010_2019(BarChartArguments):
    output_file: str = 'weekday_ridership_barchart_2010_2019.png'

@dataclass
class SaturdayBarChartArguments_2010_2019(BarChartArguments):
    output_file: str = 'saturday_ridership_barchart_2010_2019.png'

@dataclass
class SundayBarChartArguments_2010_2019(BarChartArguments):
    output_file: str = 'sunday_ridership_barchart_2010_2019.png'

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
class BumpChartArguments:
    x_value: str = 'YEAR'
    y_value: str = 'RANK'
    color_values: str = 'ROUTE'
    title: str = "Highest performing CTA bus routes by number of rides " \
                 "(1999-2022)"
    scheme: str = 'category20'

@dataclass
class WeekdayBumpChartArguments(BumpChartArguments):
    output_file: str = 'weekday_ridership_bump_chart.png'

@dataclass
class SaturdayBumpChartArguments(BumpChartArguments):
    output_file: str = 'saturday_ridership_bump_chart.png'

@dataclass
class SundayBumpChartArguments(BumpChartArguments):
    output_file: str = 'sunday_ridership_bump_chart.png'

@dataclass
class LineChartArguments:
    x_value: str = 'YEAR'
    y_value: str = 'AVG_RIDES'
    color_values: str = 'ROUTE'
    title: str = "Highest performing CTA bus routes by number of rides " \
                 "(1999-2022)"
    scheme: str = 'category20'

@dataclass
class WeekdayLineChartArguments(LineChartArguments):
    output_file: str = 'weekday_ridership_time_series_analysis.png'

@dataclass
class SaturdayLineChartArguments(LineChartArguments):
    output_file: str = 'saturday_ridership_time_series_analysis.png'

@dataclass
class SundayLineChartArguments(LineChartArguments):
    output_file: str = 'sunday_ridership_time_series_analysis.png'

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
class WeekdayHeatmapArguments_1999_2010(HeatmapArguments):
    output_file: str = 'weekday_ridership_heatmap_1999_2010.png'

@dataclass
class SaturdayHeatmapArguments_1999_2010(HeatmapArguments):
    output_file: str = 'saturday_ridership_heatmap_1999_2010.png'

@dataclass
class SundayHeatmapArguments_1999_2010(HeatmapArguments):
    output_file: str = 'sunday_ridership_heatmap_1999_2010.png'


@dataclass
class WeekdayHeatmapArguments_2011_2022(HeatmapArguments):
    output_file: str = 'weekday_ridership_heatmap_2011_2022.png'

@dataclass
class SaturdayHeatmapArguments_2011_2022(HeatmapArguments):
    output_file: str = 'saturday_ridership_heatmap_2011_2022.png'

@dataclass
class SundayHeatmapArguments_2011_2022(HeatmapArguments):
    output_file: str = 'sunday_ridership_heatmap_2011_2022.png'

@dataclass
class WeekdayHeatmapArguments_1999_2022(HeatmapArguments):
    output_file: str = 'weekday_ridership_heatmap_1999_2022.png'

@dataclass
class SaturdayHeatmapArguments_1999_2022(HeatmapArguments):
    output_file: str = 'saturday_ridership_heatmap_1999_2022.png'

@dataclass
class SundayHeatmapArguments_1999_2022(HeatmapArguments):
    output_file: str = 'sunday_ridership_heatmap_1999_2022.png'
