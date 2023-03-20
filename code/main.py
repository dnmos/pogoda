import config, scrape, sql.db


def main():

  sql.db.drop()
  sql.db.create()
  values = scrape.pogoda_detailed()
  sql.db.insert(query=sql.db.parse_sql(config.INSERT_POGODA_DETAILED_PATH)[0], 
                values = values)
  values = scrape.pogoda_additional()
  sql.db.insert(query=sql.db.parse_sql(config.INSERT_POGODA_ADDITIONAL_PATH)[0], 
                values = values)


if __name__ == "__main__":
  main()