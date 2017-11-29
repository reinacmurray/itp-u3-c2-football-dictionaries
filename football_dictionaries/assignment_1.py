# Assignment 1: Transform lists to dictionaries

def players_as_dictionaries(squads_list):
    new_list = []
    
    for each_list in squads_list:
        player_dictionary = {
            "number": each_list[0],
            "position": each_list[1],
            "name": each_list[2], 
            "date_of_birth": each_list[3], 
            "caps": each_list[4], 
            "club": each_list[5], 
            "country": each_list[6], 
            "club_country": each_list[7], 
            "year": each_list[8]
        }
        new_list.append(player_dictionary)
        
    return new_list