from operation import BaseOperations
from model import TeamModel

class Search():
    def __init__(self):
        self.operation = BaseOperations()
        self.search_layout = "select * from {table} where {filter} = '{item}'"
        self.msg = "\n What {} do you want to search: "
    
    def runner(self):
        input_opt = input(self.msg.format("runner"))
        sql = ( "select birth_date, age_class, bib, event, place, net_time  "
                "from athlete "
                "join runner on athlete.id_athlete = runner.id_athlete "
                "join events on events.id_event = runner.id_event "
                "join event_ranking on event_ranking.id_runner = runner.id_runner "
                f"where athlete.name = '{input_opt}'" 
                "order by birth_date"
                )
        result = self.execute(sql)
        if result.rowcount > 0:
            print(f"\n\nHere are the races where {input_opt} has run:")
            print("=" * 100)
            for line in result: 
                print(
                    "--> Birth Date:", str(line.birth_date), 
                    " - Class:", line.age_class, 
                    " - Event:", line.event, 
                    " - BIB:", line.bib, 
                    " - Ranking:", line.place, 
                    " - Net Time:", line.net_time
                    )
        else:
            print("\nRegistry not Found!")

    def event(self):
        input_opt = input(self.msg.format("Event"))
        sql = ( "select event_year, distance, count(distinct event_ranking.id_runner) as total_runner "
                "from events "
                "join event_ranking on event_ranking.id_event = events.id_event "
                f"where events.event = '{input_opt}' " 
                "group by event_year, distance "
                "order by event_year")
        result = self.execute(sql)
        if result.rowcount > 0:
            print(f"\n\nHere are the informations about {input_opt}:")
            print("=" * 100)
            for line in result: 
                print(
                    "--> Year of Run:", line.event_year, 
                    " - Distance:", line.distance, 
                    " - Total of Runners:", line.total_runner
                    )
        else:
            print("\nRegistry not Found!")

    def team(self):
        input_opt = input(self.msg.format("Event"))
        sql = ( "select team, event, event_year, name, place "
                "from teams "
                "join runner_teams on teams.id_team = runner_teams.id_team "
                "join runner on runner.id_runner = runner_teams.id_runner "
                "join events on events.id_event = runner.id_event "
                "join athlete on athlete.id_athlete = runner.id_athlete "
                "join event_ranking on event_ranking.id_event = events.id_event "
                "and runner.id_runner = event_ranking.id_runner "
                f"where team = '{input_opt}' "
                "group by team, event, event_year, name, place "
                "order by team, event, name, place"
            )
        result = self.execute(sql)
        if result.rowcount > 0:
            print(f"\n\nHere are the informations about Team {input_opt}:")
            print("=" * 100)
            for line in result: 
                print(
                    "--> Year of Run:", line.event_year, 
                    " - Event:", line.event, 
                    " - Member:", line.name, ", Position: ", line.place
                    )
            print("=" * 100)
        else:
            print("\nRegistry not Found!")

    def execute(self, sql):
        return self.operation.search(sql)
    
    def result_parse(self, result):
        parse_result = []
        if result.rowcount > 0:
            for line in result:
                print(line)
                parse_result.append(line)
        else:
            print("\nRegistry not Found!")
        return result
            
    def quit(self):
        exit()


if __name__ == "__main__":
    search = Search()
    
    opt = { 
        "1": search.event,
        "2": search.runner,
        "3": search.team,
        "4": search.quit
    }

    while True:
        msg = \
            '''\n ====== Runner Registry ======
            Please choose an option:
            1. Search Events
            2. Search Runner
            3. Search Teams
            4. Exit
            '''
        print(msg)
        input_opt = input("Enter your choice: ")
        if input_opt in opt.keys():
            opt.get(input_opt)()
        else:
            print("Invalid Option!")
