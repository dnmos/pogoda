from bs4 import BeautifulSoup
import config


def get_soup(source) -> object():
  """ Get bs4-lxml soup from file """

  with open(source) as file:
    content = file.read()
  soup = BeautifulSoup(content, "lxml")
  return soup


def pogoda_detailed() -> list():
  """ Scrape yandex pogoda detailed"""

  pogoda_detailed = []
  MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "novenber", "december"]
  for month in MONTHS:

    source = f"data/yandex.ru/pogoda/{config.CITY}/month/{month}.html"
    soup = get_soup(source=source)

    calendar = soup.find_all("div", class_="climate-calendar-day__detailed-container-center")
    for day in calendar:
      dom = day.find("h6").text.split(" ")[0]
      month_detailed = day.find("h6").text.split(" ")[1].split(",")[0]
      dow = day.find("h6").text.split(" ")[2]
      img = day.find_all("img", class_="icon")[0].attrs["src"].split("/")[-1]
      temp_day = day.find_all("div", class_="climate-calendar-day__detailed-basic-temp-day")[0].find("span").text
      temp_night = day.find_all("div", class_="climate-calendar-day__detailed-basic-temp-night")[0].find("span").text
      temp_feels_like = day.find_all("div", class_="climate-calendar-day__detailed-feels-like")[0].find("span").text
      pressure = day.find_all("table", class_="climate-calendar-day__detailed-data-table")[0].find_all("td")[1].text
      humidity = day.find_all("table", class_="climate-calendar-day__detailed-data-table")[0].find_all("td")[3].text
      airflow = day.find_all("table", class_="climate-calendar-day__detailed-data-table")[0].find_all("td")[5].text.split("м/с")[0] + "м/с"
      airflow_direction = day.find_all("table", class_="climate-calendar-day__detailed-data-table")[0].find_all("td")[5].find("abbr").text
      try:
        temp_water = day.find_all("table", class_="climate-calendar-day__detailed-data-table")[0].find_all("td")[7].text
      except IndexError:
        temp_water = ""

      pogoda_detailed.append((month, dom, month_detailed, dow, img, temp_day, temp_night, temp_feels_like, pressure, 
                              humidity, airflow, airflow_direction, temp_water))

  return pogoda_detailed


def pogoda_climate_card() -> list():
  """ Scrape yandex pogoda climat card """

  source = f"data/yandex.ru/pogoda/{config.CITY}.html"
  soup = get_soup(source=source)

  pogoda_climate_card = []
  climate_card = soup.find_all("div", class_="climate-card__layout")[0].find_all("a")
  for item in climate_card:
    month_card = item.find("div", class_="climate-card__item-name").text
    img_card = item.find_all("img")[0].attrs["src"].split("/")[-1]
    temp_card = item.find("div", class_="climate-card__item-temp").text
    pogoda_climate_card.append({
      "month_card": month_card,
      "img_card": img_card,
      "temp_card": temp_card})

  return pogoda_climate_card


def pogoda_additional() -> list():
  """ Scrape yandex pogoda additional """

  climat_card = pogoda_climate_card()

  pogoda_additional = []
  MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "novenber", "december"]
  for nom, month in enumerate(MONTHS):

    source = f"data/yandex.ru/pogoda/istanbul/month/{month}.html"
    soup = get_soup(source=source)

    additional = soup.find_all("div", class_="climate-month-additional")[0]
    month_additional = additional.find("h2").text.split(" ")[0]
    legend_item = additional.find_all("div", class_="climate-month-additional-diagram__legend-item")
    clear_days = legend_item[0].find_all("div")[0].text
    days_with_long_precipitation = legend_item[1].find_all("div")[0].text
    days_with_variable_clouds = legend_item[2].find_all("div")[0].text
    additional_param = additional.find_all("div", class_="climate-month-additional-param")
    air_humidity = additional_param[0].find("span").text
    wind = additional_param[1].find("span").text
    wind_direction = additional_param[1].find("abbr").text
    mm_of_precipitation = additional_param[2].find("span").text
    mm_of_precipitation_description = additional_param[2].find_all("div", class_="climate-month-additional-param__description-name")[0].text
    water_temperature = additional_param[3].find("span").text

    pogoda_additional.append((month,
                              climat_card[nom]["month_card"], climat_card[nom]["img_card"], climat_card[nom]["temp_card"],
                              month_additional, clear_days, days_with_long_precipitation, days_with_variable_clouds, air_humidity, 
                              wind, wind_direction, mm_of_precipitation, mm_of_precipitation_description, water_temperature))

  return pogoda_additional
