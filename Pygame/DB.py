import psycopg2

try:
    conn = psycopg2.connect("dbname='battleport' user='postgres' password='root'")
except:
    print("I am unable to connect to the database.")

cur = conn.cursor()
try:
    cur.execute("""SELECT * from highscore""")
    cur.execute("""SELECT * FROM highscore ORDER BY wins DESC LIMIT 10;""")
except:
    print("I can't SELECT from bar")

rows = cur.fetchall()
for row in rows:
    result = (row[1],row[2],row[3])
