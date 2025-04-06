from utils import (generate_city, generate_direction, generate_stationid,
                   generate_temp, generate_rain, generate_wind, generate_date)

class Publication:

    def __init__(self, city, stationid, temp, rain, wind, direction, date):
        self.city = generate_city()
        self.stationid = generate_stationid(self.city)
        self.temp = generate_temp()
        self.rain = generate_rain()
        self.wind = generate_wind()
        self.direction = generate_direction()
        self.date = generate_date()

    def __repr__(self):
        return f"{{(stationid, {self.stationid}); (city, '{self.city}'); (temp, {self.temp}); " \
               f"(rain, {self.rain}); (wind, {self.wind}); (direction, '{self.direction}'); (date, {self.date})}}"
