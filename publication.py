from utils import (generate_city, generate_dir, generate_station_id,
                   generate_temp, generate_rain, generate_wind, generate_date)

class Publication:

    def __init__(self, city, station_id, temp, rain, wind, dir, date):
        self.city = generate_city()
        self.station_id = generate_station_id(self.city)
        self.temp = generate_temp()
        self.rain = generate_rain()
        self.wind = generate_wind()
        self.dir = generate_dir()
        self.date = generate_date()

    def __repr__(self):
        return f"{{(station_id, {self.station_id}); (city, '{self.city}'); (temp, {self.temp}); " \
               f"(rain, {self.rain}); (wind, {self.wind}); (dir, '{self.dir}'); (date, {self.date})}}"
