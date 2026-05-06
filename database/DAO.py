from database.DB_connect import DBConnect
from model.Airport import Airport


class DAO():
    @staticmethod
    def get_all_nodes():
        """Recupera tutti gli aeroporti come potenziali nodi"""
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesPesati(distanza_min):
        """Calcola la media delle distanze e filtra per distanza_min."""
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        #La query raggruppa per coppie di aeroporti e calcola la media
        query = """
            SELECT ORIGIN_AIRPORT_ID as u, DESTINATION_AIRPORT_ID as v, AVG(DISTANCE) as peso
            FROM flights
            GROUP BY u, v
            HAVING peso > %s
        """
        cursor.execute(query, (distanza_min,))
        for row in cursor:
            result.append((row["u"], row["v"], row["peso"]))
        cursor.close()
        conn.close()
        return result
