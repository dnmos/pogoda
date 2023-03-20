INSERT INTO `wpvi_pogoda_detailed` (
  `calendar month`,
  `dom`,
  `month`,
  `dow`,
  `img`,
  `temp_day`,
  `temp_night`,
  `temp_feels_like`,
  `pressure`,
  `humidity`,
  `airflow`,
  `airflow_direction`,
  `temp_water`
  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

