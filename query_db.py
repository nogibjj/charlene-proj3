import sqlite3

conn = sqlite3.connect("worldcup.db")
cursor = conn.cursor()

#query 1: get the year and host country when Argentina entered semi-final
QUERY1 = """
        SELECT year, country FROM world_cup
        WHERE winner='Argentina' OR runners_up='Argentina' 
        OR third='Argentina' OR fourth='Argentina';
        """
cursor.execute(QUERY1)
print("Query 1 result: when Argentina entered semi-final")
print(cursor.fetchall())
print("------")

#query 2: Get top 10 world cups with highest attendance
QUERY2 = """
        SELECT year, country FROM world_cup
        ORDER BY Attendance DESC 
        LIMIT 10;
        """
cursor.execute(QUERY2)
print("Query 2 result: top 10 world cups with highest attendance")
print(cursor.fetchall())
print("------")

#query 3: Get the final info of world cups with more than 16 teams and 115 goals
QUERY3 = """
        SELECT year, winner, runners_up FROM world_cup
        WHERE qualified_teams > 16 AND goals_scored>=115
        ORDER BY qualified_teams;
        """
cursor.execute(QUERY3)
print("Query 3 result: the final info of world cups with more than 16 teams and 115 goals")
print(cursor.fetchall())
print("------")

conn.close()