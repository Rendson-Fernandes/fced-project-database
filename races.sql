#create database and tables races.sql

"""
https://dbm.fe.up.pt/phppgadmin/
User: fced_diogo_cruz
Pass: fced_diogo_cruz
"""
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
        bib varchar PRIMARY KEY,
        --id_event integer,
        id_event INTEGER REFERENCES events(id_event)
        --id_athlete integer,
        id_athlete INTEGER REFERENCES athlete(id_athlete)
        age_class varchar,
        --id_runner integer
        id_runner INTEGER REFERENCES runner_teams(id_runner)
);

CREATE TABLE events (
        id_event integer PRIMARY KEY,
        event varchar ,
        event_year varchar REFERENCES model,
        distance float REFERENCES model
);

--id_event INTEGER REFERENCES events(id_event)
--FOREIGN KEY (id_event, athlete_id) REFERENCES events (id_event, id_runner)
--FOREIGN KEY (id_event, athlete_id) REFERENCES events
--PRIMARY KEY (id_event, id_runner)

CREATE TABLE event_ranking (
        --id_event integer PRIMARY KEY,
        id_event INTEGER REFERENCES events(id_event)
        --athlete_id/bib integer,
        id_athlete INTEGER REFERENCES athlete(id_athlete)
        place varchar ,
        place_in_class varchar ,
        official_time TIMESTAMP , --timedelta64[ns]
        net_time TIMESTAMP , --timedelta64[ns] TIMESTAMP/TIME
        --id_runner integer 
        id_runner INTEGER REFERENCES runner_teams(id_runner)
);

CREATE TABLE runner_teams (
        id_team integer PRIMARY KEY,
        id_runner integer
        --id_team INTEGER REFERENCES teams(id_runner)
        --id_runner INTEGER REFERENCES runner(id_team)
);

CREATE TABLE teams (
        id_team integer PRIMARY KEY,
        team varchar UNIQUE
);

