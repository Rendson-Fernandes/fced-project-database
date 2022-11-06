import json 
from sqlalchemy import engine, create_engine
from model import ConfigDatabase

class BaseOperations:
    
    def search(self, sql: str) -> engine.Result:
        try:
            conn = self.connection()
            result = conn.execute(sql)
        except:
            raise ConnectionError("Database not found!")
        
        return result

    def connection(self) -> engine.Connection:
        config = self.load_config()
        connection_string = f"postgresql://{config.user}:{config.password}@{config.host}:{config.port}/{config.name}"
        return create_engine(connection_string)

    def load_config(self) -> ConfigDatabase:
        config = open("application/config_database.json")
        return ConfigDatabase(**json.load(config))
