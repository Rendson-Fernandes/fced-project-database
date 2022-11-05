CREATE DATABASE races

GO

CREATE TABLE athlete (
  id_athlete integer PRIMARY KEY,
  name varchar,
  sex varchar,
  nation varchar,
  birth_date varchar
);

CREATE TABLE runner (
        bib integer PRIMARY KEY,
        id_event varchar,
        id_athlete varchar,
        age_class integer,
        id_runner integer
);

CREATE TABLE events (
        id_event integer PRIMARY KEY,
        event character varying(30),
        event_year integer REFERENCES model,
        distance integer REFERENCES model
);

CREATE TABLE event_ranking (
        id_event integer PRIMARY KEY,
        bib character varying(30),
        place integer REFERENCES model,
        place_in_class integer REFERENCES model,
        official_time integer REFERENCES model,
        net_time integer REFERENCES model,
        id_runner integer REFERENCES model
);

CREATE TABLE runner_teams (
        id_team integer PRIMARY KEY,
        id_runner character varying(30)
);

CREATE TABLE teams (
        id_team integer PRIMARY KEY,
        team character varying(30)
);
