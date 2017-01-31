import psycopg2

try:
    conn = psycopg2.connect("dbname='battleport' user='postgres' password='root'")
except:
    print("I am unable to connect to the database.")

cur = conn.cursor()
try:
    cur.execute("""SELECT * from highscore""")
    cur.execute("""SELECT * FROM public.highscore ORDER BY wins DESC """)
except:
    print("I can't SELECT from bar")

rows = cur.fetchall()
print("Resultaten:")
for row in rows:
    result = (row[1],row[2],row[3])
    #print(result)

