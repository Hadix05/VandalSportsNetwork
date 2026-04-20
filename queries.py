from db_python import connect_to_db


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
