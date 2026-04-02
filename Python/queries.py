from Python.db_python import connect_to_db

def get_all_players():
    cnx = connect_to_db()
    cursor = cnx.cursor(dictionary=True)

    query = """

    SELECT NodeID, Name
    FROM Node
    WHERE NodeType = 'Player'

    """

    cursor.execute(query)
    results = cursor.fetchall()

    cnx.close()

    return results



def get_all_teammates(player):
    cnx = connect_to_db
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


    cursor.execute(query, (player, player))
    results = cursor.fetchall

    cnx.close()
    return results