CREATE TABLE IF NOT EXISTS `wpvi_pogoda_detailed` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `calendar month` VARCHAR(10) NOT NULL,
  `dom` VARCHAR(2) NOT NULL,
  `month` VARCHAR(10) NOT NULL,
  `dow` VARCHAR(2) NOT NULL,
  `img` VARCHAR(16) NOT NULL,
  `temp_day` VARCHAR(3) NOT NULL,
  `temp_night` VARCHAR(3) NOT NULL,
  `temp_feels_like` VARCHAR(3) NOT NULL,
  `pressure` VARCHAR(16) NOT NULL,
  `humidity` VARCHAR(3) NOT NULL,
  `airflow` VARCHAR(16) NOT NULL,
  `airflow_direction` VARCHAR(3) NOT NULL,
  `temp_water` VARCHAR(3) NOT NULL,
  `created_at` TIMESTAMP DEFAULT current_timestamp NOT NULL,
  PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

CREATE TABLE IF NOT EXISTS `wpvi_pogoda_additional` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `month` VARCHAR(10) NOT NULL,
  `month_card` VARCHAR(10) NOT NULL, 
  `img_card` VARCHAR(20) NOT NULL, 
  `temp_card` VARCHAR(10) NOT NULL,
  `month_additional` VARCHAR(10) NOT NULL,
  `clear_days` VARCHAR(2) NOT NULL,
  `days_with_long_precipitation` VARCHAR(2) NOT NULL,
  `days_with_variable_clouds` VARCHAR(2) NOT NULL,
  `air_humidity` VARCHAR(2) NOT NULL,
  `wind` VARCHAR(10) NOT NULL,
  `wind_direction` VARCHAR(3) NOT NULL,
  `mm_of_precipitation` VARCHAR(10) NOT NULL,
  `mm_of_precipitation_description` VARCHAR(20) NOT NULL,
  `water_temperature` VARCHAR(3) NOT NULL,
  `created_at` TIMESTAMP DEFAULT current_timestamp NOT NULL,
  PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;