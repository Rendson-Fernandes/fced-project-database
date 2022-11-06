query_athlete = ( "select birth_date, age_class, bib, event, place, net_time  "
                "from athlete "
                "join runner on athlete.id_athlete = runner.id_athlete "
                "join events on events.id_event = runner.id_event "
                "join event_ranking on event_ranking.id_runner = runner.id_runner "
                "where athlete.name = '$search'" 
                "order by birth_date" )

query_event = ( "select event_year, distance, count(distinct event_ranking.id_runner) as total_runner "
                "from events "
                "join event_ranking on event_ranking.id_event = events.id_event "
                "where events.event = '$search'" 
                "group by event_year, distance "
                "order by event_year")

query_team = ( "select team, event, event_year, name, place "
                "from teams "
                "join runner_teams on teams.id_team = runner_teams.id_team "
                "join runner on runner.id_runner = runner_teams.id_runner "
                "join events on events.id_event = runner.id_event "
                "join athlete on athlete.id_athlete = runner.id_athlete "
                "join event_ranking on event_ranking.id_event = events.id_event "
                "and runner.id_runner = event_ranking.id_runner "
                "where team = '$search' "
                "group by team, event, event_year, name, place "
                "order by team, event, name, place"
            )