import psycopg2
import csv

con = psycopg2.connect(
  database="races",             # your database is the same as your username
  user="fced_diogo_cruz",                 # your username
  password="fced_diogo_cruz",             # your password
  host="dbm.fe.up.pt",             # the database host
  options='-c search_path=schema'  # use the schema you want to connect to
)

#events
cur = con.cursor()
with open('events.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO events VALUES (%s, %s, %s, %s)",
        row
    )
con.commit()

#ranking
cur = con.cursor()
with open('ranking.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO ranking VALUES (%s, %s, %s, %s, %s, %s, %s)",
        row
    )
con.commit()

#athelete
cur = con.cursor()
with open('athelete.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO athelete VALUES (%s, %s, %s, %s, %s)",
        row
    )
con.commit()

#team
cur = con.cursor()
with open('team.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO team VALUES (%s, %s)",
        row
    )
con.commit()

#runner_team
cur = con.cursor()
with open('runner_team.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO runner_team VALUES (%s, %s)",
        row
    )
con.commit()


#runner
cur = con.cursor()
with open('runner.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO runner VALUES (%s, %s, %s, %s, %s)",
        row
    )
con.commit()







"""
3- INSERT AND DELETE method
import psycopg2.extras

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn = None

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

#Remove data from tables (DELETE)
			delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('James',)
            cur.execute(delete_script, delete_record)

#Insert data on tables (INSERT)
			insert_script  = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D1'), (3, 'Xavier', 20000, 'D2')]
            for record in insert_values:
                cur.execute(insert_script, record)

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

"""
