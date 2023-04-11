import mysql.connector

class registerDaten():
    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='produktdatenbank',
                                            user = 'root',
                                            password ='12345')

    def produktHinzufugen(self, produktCode, produktName, produktModell, produktPreis, produktMenge):
        cur = self.conexion.cursor()
        query = '''INSERT INTO produkte (code, name, modell, preis, menge) VALUES (%s , %s , %s , %s , %s)'''
        cur.execute(query, (produktCode, produktName, produktModell, produktPreis, produktMenge,))
        self.conexion.commit()
        cur.close()
    def produktAlleAufliste(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM produkte"
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def produktSuche(self, produktCode):
        try:
            cur = self.conexion.cursor()
            query = "SELECT * FROM produkte WHERE code = %s"
            cur.execute(query, (produktCode,))
            results = cur.fetchall()
            cur.close()
            return results
        except Exception as e:
            print("Error while fetching data from MySQL", e)
            return None

    def produktDelete(self, ID):
        cur = self.conexion.cursor()
        query = "DELETE FROM produkte WHERE ID= %s"
        cur.execute(query, (ID,))
        nom = cur.rowcount
        self.conexion.commit()
        cur.close()
        return nom

    def produktUpdate(self, preisCode, preisName, preisModell, preisPreis, preisMenge, ID):
        cur = self.conexion.cursor()
        query = "UPDATE produkte SET code = %s, name = %s, modell = %s, preis = %s, menge = %s where ID = %s"
        cur.execute(query, (preisCode, preisName, preisModell, preisPreis, preisMenge, ID,))
        act = cur.rowcount
        self.conexion.commit()
        cur.close()
        return act