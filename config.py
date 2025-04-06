SOURCES = {
    "Bucuresti": [1, 2, 3],
    "Cluj-Napoca": [4, 5],
    "Timisoara": [6],
    "Iasi": [7, 8],
    "Brasov": [9],
    "Constanta": [10, 11],
    "Craiova": [12],
    "Galati": [13],
    "Ploiesti": [14],
    "Braila": [15],
    "Oradea": [16, 17],
    "Arad": [18],
    "Pitesti": [19],
    "Bacau": [20],
    "Sibiu": [21],
    "Miercurea Ciuc": [22],
    "Deva": [23],
    "Bistrita": [24],
    "Ramnicu Valcea": [25],
    "Suceava": [26]
}

PUBLICATIONS_COUNT = 10
SUBSCRIPTIONS_COUNT = 5

SUBSCRIPTIONS_FIELDS_WEIGHTS = {
    "temp": 0.8,
    "rain": 0.5,
    "wind": 0.27,
    "dir": 0.4,
    "date": 0.9
}

OPERATIONS_WEIGHTS = {
    "city": { "=": 0.7, "!=": 0.3 },
    "station_id": { "=": 0.7, "!=": 0.3 },
    "temp": { "=": 0.2, "!=": 0.1, ">=": 0.35, "<=": 0.35 },
    "rain": { "=": 0.2, "!=": 0.1, ">=": 0.35, "<=": 0.35 },
    "wind": { "=": 0.2, "!=": 0.1, ">=": 0.35, "<=": 0.35 },
    "dir": { "=": 0.8, "!=": 0.2 },
    "date": { "=": 0.35, "!=": 0.05, ">=": 0.3, "<=": 0.3 }
}