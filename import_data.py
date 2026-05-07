import csv
from db_python import connect_db

def import_nba_players(csv_file):
    cnx = connect_db()
    cursor = cnx.cursor()

    added_teams = {} 
    added_players = {}
    added_leagues = {}
    added_seasons = {}

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            Pname = 'player'
            Lname = 'lg'
            team = 'team'
            total_points = 'pts'
            
            