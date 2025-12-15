import pandas as pd
point_values = {
    "FGM": {"long_name": "Field Goals Made", "point_value": 2},
    "FGMS": {"long_name": "Field Goals Attempted", "point_value": -1},
    "FTM": {"long_name": "Free Throws Made", "point_value": 1},
    "FTMS": {"long_name": "Free Throws Attempted", "point_value": -1},
    "FG3M": {"long_name": "Three Pointers Made", "point_value": 1},
    "REB": {"long_name": "Rebounds", "point_value": 1},
    "AST": {"long_name": "Assists", "point_value": 2},
    "STL": {"long_name": "Steals", "point_value": 4},
    "BLK": {"long_name": "Blocks", "point_value": 4},
    "TOV":  {"long_name": "Turnovers", "point_value": -2},
}
scoring_rules_df = pd.DataFrame(point_values)