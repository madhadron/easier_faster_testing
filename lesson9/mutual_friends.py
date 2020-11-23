from typing import List

def mutual_friends(
        conn,
        id1: int, id2: int
    ) -> List[int]:
    with conn.cursor() as cur:
        cur.execute('''
            SELECT DISTINCT lf.id2 
            FROM friends AS lf 
            INNER JOIN friends AS rf 
            ON lf.id2 = rf.id1
            WHERE lf.id1 = %s and rf.id2 = %s
        ''', (id1, id2))
        return [x[0] for x in cur.fetchall()]