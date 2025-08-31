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
    # return just the names as a list
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # return only foods where heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # print with chili emojis repeated by heat_level
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # return first match for cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    # reuse the get_spiciest_foods helper
    for food in get_spiciest_foods(spicy_foods):
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_average_heat_level(spicy_foods):
    # compute average as integer
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # add the new food to the list
    spicy_foods.append(spicy_food)
    return spicy_foods