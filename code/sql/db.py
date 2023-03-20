import pymysql.cursors
import config


def parse_sql(filename):
  data = open(filename, "r").readlines()
  queries = []
  DELIMITER = ";"
  query = ""

  for line in data:

    if not line.strip():
      continue

    if line.startswith("--"):
      continue

    if (DELIMITER not in line):
      query += line.replace(DELIMITER, ";")
      query.strip()
      continue

    if query:
      query += line
      queries.append(query.strip())
      query = ""
    else:
      queries.append(line.strip())
  return queries


def connect(): 
  connection = pymysql.connect(host = config.DB_HOST,
                               user = config.DB_USER,
                               database = config.DB_NAME,
                               password = config.DB_PASSWORD,
                               cursorclass = pymysql.cursors.DictCursor)
  return connection


def create():
  try:  
    connection = connect()
    queries = parse_sql(config.CREATE_TABLES_QUERY_PATH)
    with connection.cursor() as cursor:
      for query in queries:
        cursor.execute(query)
        print("Query is executed")
      connection.commit()
  finally:
    connection.close()
    print("Сonnection is disconnected")


def drop():
  try:  
    connection = connect()
    queries = parse_sql(config.DROP_TABLES_QUERY_PATH)
    with connection.cursor() as cursor:
      for query in queries:
        cursor.execute(query)
        print("Query is executed")
      connection.commit()
  finally:
    connection.close()
    print("Сonnection is disconnected")


def insert(query, values):
  """ Insert values in db with query"""
  try:  
    connection = connect()
    print("Connect successful")
    cursor = connection.cursor()
    cursor.executemany(query, values)
    print("Query is executed")
    connection.commit()
  except Exception as e:
    print(e)
  finally:
    connection.close()
    print("Сonnection is disconnected")


def fetchall():
  table_name = "_".join(filter.split("-"))
  try:
    connection = connect()
    print("Connect successful")
    cursor = connection.cursor()
    sql = f"SELECT * FROM `{table_name}`"
    cursor.execute(sql)
    print("Query is executed")
    result = cursor.fetchall()
    print(result)
  except pymysql.err.ProgrammingError as e:
    if e.args[0] in (1146,):
      print('Невозможно выполнить запрос:', e.args)
      return None
    else:
      raise
  finally:
    connection.close()
    print("Сonnection is disconnected")
