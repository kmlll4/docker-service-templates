import psycopg

DATABASE_URL='postgresql://postgres:postgres@ex11-db:5432/postgres'

# dbに接続し、pg_userテーブルの内容を表示する
with psycopg.connect(DATABASE_URL) as conn:
  with conn.cursor() as cur:
    cur.execute('SELECT * FROM pg_user')
    print(cur.fetchall())
