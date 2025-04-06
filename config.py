STATION_TO_CITY = {
    1: "Bucuresti",
    2: "Bucuresti",
    3: "Bucuresti",
    4: "Cluj-Napoca",
    5: "Cluj-Napoca",
    6: "Cluj-Napoca",
    7: "Timisoara",
    8: "Timisoara",
    9: "Iasi",
    10: "Iasi",
    11: "Brasov",
    12: "Constanta",
    13: "Craiova",
    14: "Galati",
    15: "Ploiesti",
    16: "Braila",
    17: "Oradea",
    18: "Arad",
    19: "Pitesti",
    20: "Bacau",
    21: "Bacau",
    22: "Sibiu",
    23: "Miercurea Ciuc",
    24: "Deva",
    25: "Bistrita",
    26: "Ramnicu Valcea",
    27: "Suceava"
}

PUBLICATIONS_COUNT = 10
SUBSCRIPTIONS_COUNT = 5

SUBSCRIPTIONS_FIELDS_WEIGHTS = {
    # station_id and city are always present
    "station_id": 1,
    "city": 1,
    "temp": 0.8,
    "rain": 0.5,
    "wind": 0.27,
    "dir": 0.4,
    "date": 0.9
}

OPERATIONS_WEIGHTS = {
    "city": {
        "=": 0.7,
        "!=": 0.3
    },
    "station_id": {
        "=": 0.7,
        "!=": 0.3
    },
    "temp": {
        "=": 0.2,
        "!=": 0.1,
        ">=": 0.35,
        "<=": 0.35
    },
    "rain": {
        "=": 0.2,
        "!=": 0.1,
        ">=": 0.35,
        "<=": 0.35
    },
    "wind": {
        "=": 0.2,
        "!=": 0.1,
        ">=": 0.35,
        "<=": 0.35
    },
    "dir": {
        "=": 0.8,
        "!=": 0.2
    },
    "date": {
        "=": 0.35,
        "!=": 0.05,
        ">=": 0.3,
        "<=": 0.3
    }
}
