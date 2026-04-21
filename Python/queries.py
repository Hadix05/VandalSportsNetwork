from Python.db_python import connect_to_db


def get_all_players():
    cnx = connect_to_db()
    cursor = cnx.cursor(dictionary=True)

    query = """
    SELECT NodeID, Name, Sport, Position, pts, reb, ast
    FROM Nodes
    WHERE NodeType = 'Player'
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    cnx.close()
    return results


def get_all_teammates(player_id):
    cnx = connect_to_db()
    cursor = cnx.cursor(dictionary=True)

    query = """
    SELECT n.NodeID, n.Name
    FROM Edges e
    JOIN Nodes n ON (
        (e.SourceNodeID = %s AND n.NodeID = e.TargetNodeID)
        OR
        (e.TargetNodeID = %s AND n.NodeID = e.SourceNodeID)
    )
    WHERE e.EdgeType = 'teammate_of'
    """

    cursor.execute(query, (player_id, player_id))
    results = cursor.fetchall()

    cursor.close()
    cnx.close()

    return results

def get_players_by_stats(min_pts=0, min_reb=0, min_ast=0):
    cnx = connect_to_db()
    cursor = cnx.cursor(dictionary=True)
    query = """
    SELECT NodeID, Name, Sport, pts, reb, ast
    FROM Nodes
    WHERE NodeType = 'Player'
      AND pts >= %s
      AND reb >= %s
      AND ast >= %s
    ORDER BY pts DESC
    """
    cursor.execute(query, (min_pts, min_reb, min_ast))
    results = cursor.fetchall()
    cursor.close()
    cnx.close()
    return results

def get_players_by_team(team_name):
    cnx = connect_to_db()
    cursor = cnx.cursor(dictionary=True)
    query = """
    SELECT n.NodeID, n.Name, n.Sport, n.pts, n.reb, n.ast
    FROM Nodes n
    JOIN Edges e ON n.NodeID = e.SourceNodeID
    JOIN Nodes team ON e.TargetNodeID = team.NodeID
    WHERE n.NodeType = 'Player'
      AND e.EdgeType = 'plays_for'
      AND team.NodeType = 'Team'
      AND team.Name = %s
    ORDER BY n.pts DESC
    """
    cursor.execute(query, (team_name,))
    results = cursor.fetchall()
    cursor.close()
    cnx.close()
    return results

def get_all_teams():
    cnx = connect_to_db()
    cursor = cnx.cursor(dictionary=True)
    query = """
    SELECT NodeID, Name, Sport
    FROM Nodes
    WHERE NodeType = 'Team'
    ORDER BY Name ASC
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    cnx.close()
    return results

