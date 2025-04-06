class Subscription:

    def __init__(self,
                 city,
                 city_op,
                 station_id,
                 station_id_op,
                 temp=None,
                 temp_op=None,
                 rain=None,
                 rain_op=None,
                 wind=None,
                 wind_op=None,
                 dir=None,
                 dir_op=None,
                 date=None,
                 date_op=None):

        self.city = city
        self.station_id = station_id
        self.temp = temp
        self.rain = rain
        self.wind = wind
        self.dir = dir
        self.date = date

        self.city_op = city_op
        self.station_id_op = station_id_op
        self.temp_op = temp_op
        self.rain_op = rain_op
        self.wind_op = wind_op
        self.dir_op = dir_op
        self.date_op = date_op

    def __repr__(self):
        subscription_details = f"{{(station_id,{self.station_id});(city,\"{self.city}\");"

        if self.temp is not None:
            subscription_details += f"(temp,{self.temp});"

        if self.rain is not None:
            subscription_details += f"(rain,{self.rain});"

        if self.wind is not None:
            subscription_details += f"(wind,{self.wind});"

        if self.dir is not None:
            subscription_details += f"(dir,\"{self.dir}\");"

        if self.date is not None:
            subscription_details += f"(date,{self.date})"

        subscription_details += "}"
        return subscription_details
