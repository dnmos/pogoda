import os
from dotenv import load_dotenv


load_dotenv()


# DB connect
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# PATH 
CREATE_TABLES_QUERY_PATH = "code/sql/db_create_tables.sql"
DROP_TABLES_QUERY_PATH = "code/sql/db_drop_tables.sql"
INSERT_POGODA_DETAILED_PATH = "code/sql/db_insert_pogoda_detailed.sql"
INSERT_POGODA_ADDITIONAL_PATH = "code/sql/db_insert_pogoda_additional.sql"


