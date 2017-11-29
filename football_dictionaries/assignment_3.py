from .assignment_1 import players_as_dictionaries

# Assignment 3: This function will return the players grouped by country, and per each country, grouped by position. 

# Note: this is similar to Assignment 2, with one additional layer of nesting. 


def players_by_country_and_position(squads_list):
    squad = players_as_dictionaries(squads_list)   # from assignment 1
    by_country = {}

    for player in squad:
        position = player["position"]
        country = player["country"]
        
        by_country.setdefault(country, {})
        by_country[country].setdefault(position, [])
        
        by_country[country][position].append(player)

    return by_country

