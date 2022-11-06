--a) Who run the fastest 10K race ever (name, birthdate, time)?

select a.name, a.birth_date as birthdate
from events as e
join event_ranking as rank on rank.id_event = e.id_event
join runner as r on r.id_event = e.id_event
join athlete as a on a.id_athlete = r.id_athlete 
where cast(e.distance as int) = 10
and rank.net_time = (select min(net_time) from event_ranking)

--b) What 10K race had the fastest average time (event, event date)?

select e.event, e.event_year
from events as e
join event_ranking as rank on rank.id_event = e.id_event
group by e.event, e.event_year 
having avg(rank.net_time) <= ALL (
	select avg(rank.net_time)
	from events as e
	join event_ranking as rank on rank.id_event = e.id_event
	where cast(e.distance as int) = 10
	group by e.event, e.event_year
)

--c) What teams had more than 3 participants in the 2016 maratona (team)?

select t.team, count(r.id_runner) as total_runners
from teams as t
join runner_teams as rt on rt.id_team = t.id_team
join runner as r on r.id_runner = rt.id_runner
join events as e on e.id_event = r.id_event
where e.event_year = '2016'
group by t.team
having count(r.id_runner) > 3



--d) What are the 5 runners with more kilometers in total (name, birthdate, kms)?

select a.name, sum(cast(e.distance as integer)) as total_distance
from athlete as a
join runner as r on r.id_athlete = a.id_athlete
join events as e on e.id_event = r.id_event
join event_ranking er on er.id_runner = r.id_runner 
and er.id_event = e.id_event 
group by a.name
order by total_distance desc 
limit 5


--e) What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?

select  table_1.name, 
		table_1.birth_date, 
		(table_2.net_time - table_1.net_time) as improvement
from (
	select e.event as name_event, a.id_athlete, a.name, a.birth_date, er.net_time, e.event, e.event_year 
	from athlete a 
	join runner r using(id_athlete) 
	join events e using(id_event)
	join event_ranking er using(id_runner, id_event)
	) as table_1
join (
	select e.event as name_event, a.id_athlete, a.name, a.birth_date, er.net_time, e.event, e.event_year 
	from athlete a 
	join runner r using(id_athlete) 
	join events e using(id_event)
	join event_ranking er using(id_runner, id_event)
	) as table_2
on table_1.id_athlete = table_2.id_athlete 
	and table_1.name_event = table_2.name_event
where table_1.net_time > table_2.net_time 
and  cast(table_1.event_year as int)+1 = cast(table_2.event_year as int)


