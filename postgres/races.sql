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
