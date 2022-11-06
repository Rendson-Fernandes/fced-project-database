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
        event varchar NOT NULL,
        event_year varchar NOT NULL,
        distance varchar NOT NULL
);

CREATE TABLE event_ranking (
        --id_event integer REFERENCES events ON DELETE CASCADE --(Good option)
        FOREIGN KEY id_event REFERENCES events
        place integer NOT NULL,
        place_in_class integer NOT NULL,
        official_time TIME NOT NULL, --timedelta64[ns]
        net_time TIME , --timedelta64[ns] TIMESTAMP/TIME
        FOREIGN KEY id_runner REFERENCES runner
);

CREATE TABLE runner_teams (

        FOREIGN KEY id_team REFERENCES teams,
        FOREIGN KEY id_runner REFERENCES runner
);

CREATE TABLE teams (
        id_team integer PRIMARY KEY,
        team varchar NOT NULL
);
