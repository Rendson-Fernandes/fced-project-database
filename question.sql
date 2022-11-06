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
