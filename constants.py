# league information
current_season = '2025-26'
league_id = '00'
season_type = 'Regular Season'

# PLAYER AVERAGES INFORMATION
# team information
team_info = ['TEAM_ID', 'TEAM_ABBREVIATION']

# player info
player_info = ['PLAYER_ID', 'PLAYER_NAME']

# stats to include
included_stats = [
    'GP', 'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A',
    'FTM', 'FTA', 'REB', 'AST', 'TOV', 'STL',
    'BLK', 'PTS'
    ]

# combine to use in player_averages file
player_stats_cols = team_info + player_info + included_stats