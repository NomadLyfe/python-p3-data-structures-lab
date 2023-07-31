spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = [obj['name'] for obj in spicy_foods]
    return name_list

def get_spiciest_foods(spicy_foods):
    spiciest_list = [obj for obj in spicy_foods if obj['heat_level'] > 5]
    return spiciest_list

def print_spicy_foods(spicy_foods):
    for obj in spicy_foods:
        print(f'{obj["name"]} ({obj["cuisine"]}) | Heat Level: {"🌶" * obj["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for obj in spicy_foods:
        if obj["cuisine"] == cuisine:
            return dict(obj)

def print_spiciest_foods(spicy_foods):
    for obj in spicy_foods:
        if obj["heat_level"] > 5:
            print(f'{obj["name"]} ({obj["cuisine"]}) | Heat Level: {"🌶" * obj["heat_level"]}')

def get_average_heat_level(spicy_foods):
    count = 0
    total = 0
    for obj in spicy_foods:
        count += 1
        total += obj['heat_level']
    return total/count

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
