import csv
from db_python import connect_to_db

CSV_FILE = "nba_players.csv"

def import_nba_data():
    cnx = connect_to_db()
    cursor = cnx.cursor()

    cursor.execute("""
        INSERT INTO Nodes (NodeType, Name, Sport, Tier)
        SELECT 'League', 'NBA', 'NBA', 1
        WHERE NOT EXISTS (
            SELECT 1 FROM Nodes WHERE NodeType = 'League' AND Name = 'NBA'
        )
    """)

    cursor.execute("SELECT NodeID FROM Nodes WHERE NodeType = 'League' AND Name = 'NBA'")
    league_id = cursor.fetchone()[0]

    teams_added = {}
    players_added = {}
    imported = 0

    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            player_name = row['player_name'].strip()
            team_abbr = row['team_abbreviation'].strip()

            # Parse stats — average them across seasons later
            try:
                pts = float(row['pts'])
            except:
                pts = None
            try:
                reb = float(row['reb'])
            except:
                reb = None
            try:
                ast = float(row['ast'])
            except:
                ast = None

            if player_name in players_added:
                continue

            if team_abbr not in teams_added:
                cursor.execute("""
                    INSERT INTO Nodes (NodeType, Name, Sport)
                    VALUES ('Team', %s, 'NBA')
                """, (team_abbr,))
                team_id = cursor.lastrowid
                teams_added[team_abbr] = team_id

                cursor.execute("""
                    INSERT INTO Edges (SourceNodeID, TargetNodeID, EdgeType)
                    VALUES (%s, %s, 'competes_in')
                """, (team_id, league_id))

            team_id = teams_added[team_abbr]

            cursor.execute("""
                INSERT INTO Nodes (NodeType, Name, Sport, pts, reb, ast)
                VALUES ('Player', %s, 'NBA', %s, %s, %s)
            """, (player_name, pts, reb, ast))
            player_id = cursor.lastrowid
            players_added[player_name] = player_id

            cursor.execute("""
                INSERT INTO Edges (SourceNodeID, TargetNodeID, EdgeType)
                VALUES (%s, %s, 'plays_for')
            """, (player_id, team_id))

            cursor.execute("""
                INSERT INTO GraphMembership (GraphID, NodeID, GraphName)
                VALUES (1, %s, 'NBA')
            """, (player_id,))

            imported += 1

    cnx.commit()
    print(f"Done! Imported {imported} players, {len(teams_added)} teams.")
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    import_nba_data()