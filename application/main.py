from operation import BaseOperations


class Search():
    def __init__(self):
        self.operation = BaseOperations()
        self.search_layout = "select * from {} where {} = '{}'"
        self.msg = "\n What {} do you want to search: "
    
    def runner(self):
        input_opt = input(self.msg.format("runner"))
        sql = self.search_layout.format("city", "name", input_opt)
        self.execute(sql)

    def event(self):
        input_opt = input(self.msg.format("Event"))
        sql = self.search_layout.format("city", "name", input_opt)
        self.execute(sql)

    def team(self):
        input_opt = input(self.msg.format("Team"))
        sql = self.search_layout.format("city", "name", input_opt)
        self.execute(sql)

    def execute(self, sql):
        result = self.operation.search(sql)
        return self.result_parse(result)
    
    def result_parse(self, result):
        if result.rowcount > 0:
            for line in result:
                print(line)
        else:
            print("\nRegistry not Found!")
            
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
