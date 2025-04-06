from utils import (generate_city, generate_dir, generate_station_id,
                   generate_subscription_field, generate_operation,
                   generate_temp, generate_rain, generate_wind, generate_date)


class Subscription:

    def __init__(self):

        self.station_id = generate_station_id()
        self.station_id_op = generate_operation("station_id")

        self.city = generate_city(self.station_id)
        self.city_op = generate_operation("city")

        if generate_subscription_field("temp"):
            self.temp = generate_temp()
            self.temp_op = generate_operation("temp")
        else:
            self.temp = None
            self.temp_op = None

        if generate_subscription_field("rain"):
            self.rain = generate_rain()
            self.rain_op = generate_operation("rain")
        else:
            self.rain = None
            self.rain_op = None

        if generate_subscription_field("wind"):
            self.wind = generate_wind()
            self.wind_op = generate_operation("wind")
        else:
            self.wind = None
            self.wind_op = None

        if generate_subscription_field("dir"):
            self.dir = generate_dir()
            self.dir_op = generate_operation("dir")
        else:
            self.dir = None
            self.dir_op = None

        if generate_subscription_field("date"):
            self.date = generate_date().strftime("%d.%m.%Y")
            self.date_op = generate_operation("date")
        else:
            self.date = None
            self.date_op = None

    def __repr__(self):
        subscription_details = "{"

        if self.station_id is not None and self.station_id_op is not None:
            subscription_details += f"(station_id,{self.station_id_op},{self.station_id});"

        if self.city is not None and self.city_op is not None:
            subscription_details += f"(city,{self.city_op},\"{self.city}\");"

        if self.temp is not None and self.temp_op is not None:
            subscription_details += f"(temp,{self.temp_op},{self.temp});"

        if self.rain is not None and self.rain_op is not None:
            subscription_details += f"(rain,{self.rain_op},{self.rain});"

        if self.wind is not None and self.wind_op is not None:
            subscription_details += f"(wind,{self.wind_op},{self.wind});"

        if self.dir is not None:
            subscription_details += f"(dir,{self.dir_op},\"{self.dir}\");"

        if self.date is not None:
            subscription_details += f"(date,{self.date_op},{self.date})"

        subscription_details += "}"
        return subscription_details
