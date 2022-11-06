from operation import BaseOperations
from model import TeamModel
import sql_features

class Search():
    def __init__(self):
        self.operation = BaseOperations()
        self.search_layout = "select * from {table} where {filter} = '{item}'"
        self.msg = "\n What {} do you want to search: "
    
    def runner(self):
        input_opt = input(self.msg.format("runner"))
        query = sql_features.query_athlete.replace("$search", input_opt)
        result = self.execute(query)
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
        query = sql_features.query_event.replace("$search", input_opt)
        result = self.execute(query)
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
        query = sql_features.query_team.replace("$search", input_opt)
        result = self.execute(query)
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
