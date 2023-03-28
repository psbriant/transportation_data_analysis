"""
Description: File for storing recurring settings
"""

from dataclasses import dataclass

@dataclass
class HeatmapArguments:
    index: str = 'MONTH'
    columns: str = 'YEAR'
    values: str = 'AVG_RIDES'
    output_file: str = 'ridership_heatmap.png'
