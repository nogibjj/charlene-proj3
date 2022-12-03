import sqlite3
import pandas as pd

data = pd.read_csv(r'WorldCups.csv')
df = pd.DataFrame(data)

conn = None
conn = sqlite3.connect("worldcup.db")
cursor = conn.cursor()

DROP_TABLE = "DROP TABLE world_cup"
cursor.execute(DROP_TABLE)

CREATE_TABLE = """ CREATE TABLE world_cup (
                year integer PRIMARY KEY, 
                country text NOT NULL,
                winner text NOT NULL,
                runners_up text NOT NULL,
                third text NOT NULL,
                fourth text NOT NULL,
                goals_scored integer,
                qualified_teams integer,
                matches_played integer,
                attendance integer
                );"""
cursor.execute(CREATE_TABLE)
conn.commit()

df.to_sql('world_cup',conn, if_exists='append', index=False)

cursor.execute("SELECT * FROM world_cup")
print(cursor.fetchall())

conn.close()
