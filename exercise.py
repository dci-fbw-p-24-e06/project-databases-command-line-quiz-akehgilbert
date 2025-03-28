from config import config
import psycopg2 as pg

conn = pg.connect(**config)
conn.autocommit = True
cur = conn.cursor()
cur.execute('SELECT usename FROM pg_user;')
user_list = cur.fetchall()
print(user_list)
