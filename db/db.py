from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from dotenv import load_dotenv
import os

load_dotenv()

_engine = None 

class SessionMaker:
    def get_engine(self):
        global _engine

        if _engine is None:
            user = os.environ['MYSQL_USER']
            password = os.environ['MYSQL_PASSWORD']
            host = os.environ['MYSQL_HOST']
            port = os.environ['MYSQL_PORT']
            database = os.environ['MYSQL_DB']

            conn_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

            if not database_exists(conn_str):
                create_database(conn_str)

            _engine = create_engine(conn_str,pool_size=50,echo=True)

        return _engine

    def get_session(self):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)
        return Session
