class Subscription:

    def __init__(self,
                 city,
                 city_operator,
                 stationid,
                 stationid_operator,
                 temp=None,
                 temp_operator=None,
                 rain=None,
                 rain_operator=None,
                 wind=None,
                 wind_operator=None,
                 direction=None,
                 direction_operator=None,
                 date=None,
                 date_operator=None):

        self.city = city
        self.stationid = stationid
        self.temp = temp
        self.rain = rain
        self.wind = wind
        self.direction = direction
        self.date = date

        self.city_operator = city_operator
        self.stationid_operator = stationid_operator
        self.temp_operator = temp_operator
        self.rain_operator = rain_operator
        self.wind_operator = wind_operator
        self.direction_operator = direction_operator
        self.date_operator = date_operator

    def __repr__(self):
        subscription_details = f"{{(stationid,{self.stationid});(city,\"{self.city}\");"

        if self.temp is not None:
            subscription_details += f"(temp,{self.temp});"

        if self.rain is not None:
            subscription_details += f"(rain,{self.rain});"

        if self.wind is not None:
            subscription_details += f"(wind,{self.wind});"

        if self.direction is not None:
            subscription_details += f"(direction,\"{self.direction}\");"

        if self.date is not None:
            subscription_details += f"(date,{self.date})"

        subscription_details += "}"
        return subscription_details
