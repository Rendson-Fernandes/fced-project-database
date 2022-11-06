-- CREATE DATABASE races

-- GO

BEGIN;

        SET client_encoding = 'LATIN1';

        CREATE TABLE athlete (
        id_athlete integer PRIMARY KEY,
        name varchar NOT NULL,
        sex varchar NOT NULL,
        nation varchar NOT NULL,
        birth_date DATE NOT NULL
        );

        CREATE TABLE events (
                id_event integer PRIMARY KEY,
                event varchar NOT NULL,
                event_year varchar NOT NULL,
                distance varchar NOT NULL
        );

        CREATE TABLE runner (
                id_runner integer PRIMARY KEY,
                id_event integer,
                id_athlete integer,
                bib varchar,
                age_class varchar, 
                CONSTRAINT fk_id_event
                        FOREIGN KEY(id_event) 
                                REFERENCES events(id_event), 
                CONSTRAINT fk_id_athlete
                        FOREIGN KEY(id_athlete) 
                                REFERENCES athlete(id_athlete)
        );

        CREATE TABLE event_ranking (
                id_event integer,
                id_runner integer,
                place integer NOT NULL,
                place_in_class integer NOT NULL,
                official_time TIME NOT NULL, --timedelta64[ns]
                net_time TIME , --timedelta64[ns] TIMESTAMP/TIME
                CONSTRAINT pk_event_runner 
                        PRIMARY KEY (id_event, id_runner),
                CONSTRAINT fk_id_event
                        FOREIGN KEY(id_event) 
                                REFERENCES events(id_event),
                CONSTRAINT fk_id_runner
                        FOREIGN KEY(id_runner) 
                                REFERENCES runner(id_runner)
        );

        CREATE TABLE teams (
                id_team integer PRIMARY KEY,
                team varchar NOT NULL UNIQUE
        );

        CREATE TABLE runner_teams (
                id_runner integer,
                id_team integer,
                CONSTRAINT pk_runner_teams 
                        PRIMARY KEY (id_runner, id_team),
                CONSTRAINT fk_id_runner
                        FOREIGN KEY(id_runner) 
                                REFERENCES runner(id_runner),
                CONSTRAINT fk_id_team
                        FOREIGN KEY(id_team) 
                                REFERENCES teams(id_team)
        );
COMMIT;


