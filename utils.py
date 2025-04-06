import config
import random
import datetime


def generate_city():
    return random.choice(list(config.SOURCES.keys()))


def generate_station_id(city):
    return random.choice(config.SOURCES[city])


def generate_temp():
    return round(random.uniform(-20, 40), 2)


def generate_rain():
    return round(random.uniform(0, 100), 2)


def generate_wind():
    return round(random.uniform(0, 100), 2)


def generate_dir():
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return random.choice(dirs)


def generate_date():
    start = datetime.datetime(2023, 1, 1)
    end = datetime.datetime(2025, 12, 31)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)
