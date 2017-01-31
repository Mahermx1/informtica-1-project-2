import psycopg2

try:
    conn = psycopg2.connect("dbname='battleport' user='postgres' password='root'")
except:
    print("I am unable to connect to the database.")

cur = conn.cursor()
try:
    cur.execute("""SELECT * from highscore""")
except:
    print("I can't SELECT from bar")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print("   ", row[1])
