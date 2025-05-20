DOMAIN = "pollen_dk"
POLLEN_URL = "https://www.astma-allergi.dk/umbraco/Api/PollenApi/GetPollenFeed"

POLLEN_TYPES = {
    44: "Alternaria",
    7: "Birk",
    31: "Bynke",
    45: "Cladosporium",
    1: "El",
    4: "Elm",
    28: "Græs",
    2: "Hassel",
}

REGION_IDS = {
    "west": 48,
    "east": 49,
}

POLLEN_LEVEL_INTERVALS = {
    44: [0, 20, 100, 500],
    7: [0, 30, 100, 550],
    31: [0, 10, 50, 60],
    45: [0, 2000, 6000, 7000],
    1: [0, 10, 50, 200],
    4: [0, 10, 50, 80],
    28: [0, 10, 50, 150],
    2: [0, 5, 15, 40],
}

POLLEN_LEVEL_DESCRIPTION_IDS = {
    "": "",
    "1": "low",
    "2": "medium",
    "3": "high"
}