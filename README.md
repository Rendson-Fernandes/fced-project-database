README.MD
![alt text](https://sigarra.up.pt/feup/pt/imagens/LogotipoSI)
# Database Project (FCED Project 2022)

Brief explanation of how create a database through a csv file. We had to represent an UML, ER, create database and respective tables (races.sql), as well an INSERT and DELETE method script to change tables (load_races.py). At the end we create a User Interaction script in python that allow users to interact with database (races.py).

This project was made by Bárbara Zanetti, Diogo Cruz and Rendson Fernandes

## UML
[uml](https://lucid.app/lucidchart/48aa113e-50a4-4fdc-8b27-3902b3a72421/edit?viewport_loc=-141%2C-396%2C1880%2C1034%2C0_0&invitationId=inv_e575e21d-d189-4e1e-bc62-f36aba3fce48
)

![alt text](https://drive.google.com/file/d/1LTED-SxJZh7cBmfGktx9fplCUxOcrAFd/view?usp=share_link)

## ER
athlete	(id_athlete, name, sex, nation, birth_date)

runner (bib,id_event, id_athlete, age_class)

events (id_event, event, event_year,	distance)

event_ranking (id_event, bib,	place,	place_in_class, official_time,	net_time) 

runner_teams (id_team--> teams, id_athlete-->athlete)

teams (id_team, team)

## Python script: Prepare dataframes to create tables on database
We clean duplicated rows and split data between 6 dataframes: athlete, runner, events, event_ranking, runner_teams, teams
```python
import pandas as pd

# read all_races.csv file
df = pd.read_csv('~/all_races.csv')

# drop dupplicated rows
df = df.drop_duplicates()

# drop wrong row
update_df = df.drop(146929)

# split data through different df to create tables on database
athlete = 
runner = 
events = 
event_ranking = 
runner_teams = 
teams = 

```
## Create database races.sql file
```sql
CREATE DATABASE races

GO

CREATE TABLE airport (
  airportcod integer PRIMARY KEY,
  name varchar,
  city varchar,
  country varchar
);

CREATE TABLE model (
        modelcod integer PRIMARY KEY,
        make varchar,
        version varchar,
        engines integer
);

CREATE TABLE plane (
        planecod integer PRIMARY KEY,
        name character varying(30),
        modelcod integer REFERENCES model
);
```


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install psycopg2.

```bash
pip install psycopg2
```


## load_races.py file
```python
import psycopg2
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
```

## races.py file
```python
print("Menu of options:
1- Search runner
2-Search race
3-Search team
4-Search event")```
## License
[MIT](https://choosealicense.com/licenses/mit/)
