![alt text](https://sigarra.up.pt/feup/pt/imagens/LogotipoSI)
# Database Project (FCED Project 2022)

Brief explanation of how create a database through a csv file. We had to represent an UML, ER, create database and respective tables (races.sql), as well an INSERT and DELETE method script to change tables (load_races.py). At the end we create a User Interaction script in python that allow users to interact with database (races.py).

This project was made by Bárbara Zanetti, Diogo Cruz and Rendson Fernandes

## UML
[uml](https://lucid.app/lucidchart/48aa113e-50a4-4fdc-8b27-3902b3a72421/edit?viewport_loc=-141%2C-396%2C1880%2C1034%2C0_0&invitationId=inv_e575e21d-d189-4e1e-bc62-f36aba3fce48)

![alt text](https://i.ibb.co/f0S8SGx/Captura-de-ecra-2022-11-06-a-s-13-44-30.png)

## ER
athlete	(id_athlete, name, sex, nation, birth_date)

runner (id_runner, id_event, bib, id_athlete, age_class)

events (id_event, event, event_year,	distance)

event_ranking (id_event, id_runner,	place,	place_in_class, official_time,	net_time, (bib)) 

runner_teams (id_team--> teams, id_runner-->runner)

teams (id_team, team)

## Python script: Prepare dataframes to create tables on database
We clean duplicated rows and split data between 6 dataframes: athlete, runner, events, event_ranking, runner_teams, teams
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

"""# Reading the Dataset"""

df = pd.read_csv("/content/drive/MyDrive/Feup/FCED/Database/all_races.csv",sep=",", low_memory=False)

"""# Preprossesing and Cleaning the data"""

#identify on the line 146929 an header duplicate in the middle of the dataset
df = df.drop(axis=0, labels=146929)

df.describe()

#counting duplicated
print('# of duplicates:',len(df)-len(df.drop_duplicates()))
print('size of df:',len(df))

#removing the duplicates
df = df.drop_duplicates()
#writing file without duplicates
df.to_csv('/content/drive/MyDrive/Feup/FCED/Database/all_races_no_duplicates.csv', index=False)
#Checking the types of the colunms
df.dtypes

#checking the nulls in the df
sns.heatmap(df.isnull(),cbar=False,
            cmap='rocket',yticklabels=False)
plt.title('Missing values on the split dataset');

#treating the nulls in the net time. When net time is null, net_time = official_time
df.loc[df['net_time'].isnull(), 'net_time'] = df[df['net_time'].isnull()]['official_time']

#treating the nulls in the team. When net team is null, team= Individual
df.loc[df['team'].isnull(), 'team'] = 'Individual'

#Converting columns type
df['birth_date'] = pd.to_datetime(df['birth_date'])
df['net_time'] = pd.to_timedelta(df['net_time'])
df['official_time'] = pd.to_timedelta(df['official_time'])

# Team: team name, team id.
df_team = pd.DataFrame([])
df_team['team'] = df['team'].unique()
df_team.insert(0, 'id_team', range(0, 0 + len(df_team)))

# Athlete: id, name, sex, nation, birth_date
df_athlete = df[['name', 'sex','nation','birth_date']].drop_duplicates()
df_athlete.insert(0, 'id_athlete', range(0, 0 + len(df_athlete)))
print(len(df))

#df_athlete.groupby(['name','birth_date','sex']).nunique().sort_values(by=['sex','nation'], ascending=False)

# Events: event_id, event, event_year, distance
df_events = df[['event', 'event_year', 'distance']].drop_duplicates()
df_events.insert(0, 'id_event', range(0, 0 + len(df_events)))

print(len(df))

# populate id_athlete on df
df = pd.merge(df,df_athlete[['name','birth_date','sex','nation','id_athlete']], how='left', on=['name','birth_date','sex','nation'])
print(len(df))

#populate id_team on df
df = pd.merge(df,df_team[['team','id_team']], how='left', on=['team'])
print(len(df))

#populate id_event on df
df = pd.merge(df,df_events[['event','event_year', 'distance','id_event']], how='left', on=['event', 'event_year', 'distance'])
print(len(df))

# Runner: id_runner, bib, age_class, id_event, id_athlete
df_runner = df[['bib','age_class','id_athlete','id_event']].drop_duplicates()
df_runner.insert(0, 'id_runner', range(0, 0 + len(df_runner)))
print(len(df))

# populate runner_id
df = pd.merge(df,df_runner[['bib','age_class','id_athlete','id_event','id_runner']], how='left', on=['bib','age_class','id_athlete','id_event'])
print(len(df))

df_runner_team = df[['id_team','id_runner']].drop_duplicates()

print(len(df))

# Event_ranking: id_event, id_runner, place, place_in_class, official_time, net_time
df_ranking = df[['place','place_in_class', 'official_time', 'net_time','id_runner','id_event']].drop_duplicates()
df_ranking.insert(0, 'athlete_id', range(0, 0 + len(df_ranking)))

df_ranking.to_csv("/content/drive/MyDrive/Feup/FCED/Database/ranking.csv")
df_runner_team.to_csv("/content/drive/MyDrive/Feup/FCED/Database/runner_team.csv")
df_runner.to_csv("/content/drive/MyDrive/Feup/FCED/Database/runner.csv")
df_events.to_csv("/content/drive/MyDrive/Feup/FCED/Database/events.csv")
df_athlete.to_csv("/content/drive/MyDrive/Feup/FCED/Database/athlete.csv")
df_team.to_csv("/content/drive/MyDrive/Feup/FCED/Database/team.csv")
```
## Create database races.sql file
```sql
CREATE DATABASE races

GO

CREATE TABLE athlete (
  id_athlete integer PRIMARY KEY,
  name varchar NOT NULL,
  sex varchar NOT NULL,
  nation varchar NOT NULL,
  birth_date DATE NOT NULL --datetime64[ns]
);

CREATE TABLE runner (
        id_runner INTEGER PRIMARY KEY
        bib varchar ,
        id_event INTEGER REFERENCES events(id_event),
        id_athlete INTEGER REFERENCES athlete(id_athlete),
        age_class varchar
);

CREATE TABLE events (
        id_event integer PRIMARY KEY,
        event varchar ,
        event_year varchar,
        distance varchar
);

CREATE TABLE event_ranking (
        FOREIGN KEY id_event REFERENCES events,
        place varchar ,
        place_in_class varchar ,
        official_time TIMESTAMP , --timedelta64[ns]
        net_time TIMESTAMP , --timedelta64[ns] 
        FOREIGN KEY id_runner REFERENCES runner
);

CREATE TABLE runner_teams (
        FOREIGN KEY id_team REFERENCES teams,
        FOREIGN KEY id_runner REFERENCES runner
);

CREATE TABLE teams (
        id_team integer PRIMARY KEY,
        team varchar UNIQUE
); 
```


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install psycopg2.

```bash
pip install psycopg2
```


## load_races.py file
```python
#load_races.py
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
```

## races.py file
```python
print("Menu of options:
1- Search runner
2-Search race
3-Search team
4-Search event")
```
## question.sql file
```sql
--a) Who run the fastest 10K race ever (name, birthdate, time)?

select a.name, a.birth_date as birthdate, rank.time
from event as e
join event_ranking as rank on rank.id_event = e.id_event
join runner as r on r.id_event = e.id_event
join athelete as a on a.id_athlete = e.id_athlete
where e.distance >= 10
order by rank.time desc


--b) What 10K race had the fastest average time (event, event date)?

select e.event, e.event_year as event date
from event as e
join event_ranking as rank on rank.id_event = e.id_event
where e.distance = 10
group by e.event
order by average(rank.time) desc

--c) What teams had more than 3 participants in the 2016 maratona (team)?

select t.team
from teams as t
join runner_team as rt on rt.id_team = t.id_team
join runner as r on r.id_runner = rt.id_runner
join event as e on e.id_event = r.id_event
where e.event = '2016' and count(e.id_runner) > 3
group by t.team


--d) What are the 5 runners with more kilometers in total (name, birthdate, kms)?

select a.name, a.birth_date as birthdate, sum(e.distance) kms
from athelete as a
join runner as r on r.id_athelete = a.id_athelete
join event as e on e.id_event = r.id_event
order by kms desc
limit 5


--e) What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?

select a.name, a.birth_date as birthdate, improvement
from
```

## Repository
[Github](https://github.com/Rendson-Fernandes/fced-project-database)
