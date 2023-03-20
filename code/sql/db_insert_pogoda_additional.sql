INSERT INTO `wpvi_pogoda_additional` (
  `month`,
  `month_card`,
  `img_card`,
  `temp_card`,
  `month_additional`, 
  `clear_days`, 
  `days_with_long_precipitation`, 
  `days_with_variable_clouds`, 
  `air_humidity`, 
  `wind`, 
  `wind_direction`, 
  `mm_of_precipitation`, 
  `mm_of_precipitation_description`, 
  `water_temperature`
  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

