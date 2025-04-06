import config
import random
import datetime


def generate_city(id):
    return config.STATION_TO_CITY[id]


def generate_station_id():
    return random.randint(1, len(config.STATION_TO_CITY))


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


def generate_operation(field):
    weights = config.OPERATIONS_WEIGHTS[field]
    operations = list(weights.keys())
    weights = list(weights.values())
    chance_array = [weights[0]]

    for i in range(1, len(weights)):
        chance_array.append(weights[i] + chance_array[i - 1])

    random_value = random.uniform(0, 1)
    for i in range(len(chance_array)):
        if random_value <= chance_array[i]:
            return operations[i]

    return operations[-1]


def generate_subscription_field(field):
    weight = config.SUBSCRIPTIONS_FIELDS_WEIGHTS[field]
    if random.uniform(0, 1) <= weight:
        return True
    return False
