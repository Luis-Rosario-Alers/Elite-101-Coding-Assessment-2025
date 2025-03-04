from restaurantTables import restaurant_tables2
"""
REFERENCE
restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]
"""

def list_all_free_tables(time_slot: int, table_data: list) -> list:
    """
    LEVEL 1: this function is used to return the free tables in a specific time slot.
    """
    free = [] # create our output list, this will output our list of free tables
    for occupied_state in range(1, len(table_data)): # here we check make a for loop that skips the first index
        # of the chosen time slot because we know that will just contain the number of the time slot and not an actual
        # useful piece of data.
        if table_data[time_slot][occupied_state] == 'o': # if the table has, an occupied_state of false, then we go to the header
            # and find the table corresponding to that occupancy state and append it to the list of free tables.
            free.append(table_data[0][occupied_state])
    return free # return list of free tables.

print(list_all_free_tables(1, restaurant_tables2))

def list_one_free_table_under_party_size(time_slot: int, table_data: list, party_size: int) -> list:
    """
        LEVEL 2: this function is used to return one free table in a specific time slot and equal
        to or above the party size.
        """
    for occupied_state in range(1, len(table_data)):  # loop over the occupied state in given time slot
        if table_data[time_slot][occupied_state] == 'o':  # if the table is open
            if int(table_data[0][occupied_state][3]) >= party_size: # then we check if the table is bigger than or equal to party size, if it is, we return it.
                return table_data[0][occupied_state]
            else: # if the table isn't open or isn't big enough for the party, we continue the loop.
                continue

print(list_one_free_table_under_party_size(1, restaurant_tables2, 2))

def list_all_free_tables_under_party_size(time_slot: int, table_data: list, party_size: int) -> list:
    """
        LEVEL 3: this function is used to return the free tables in a specific time slot and equal
        to or above the party size.
        """
    free = [] # output list
    for occupied_state in range(1, len(table_data)):  # loop over the occupied state in given time slot
        if table_data[time_slot][occupied_state] == 'o':  # if the table is open
            if int(table_data[0][occupied_state][3]) >= party_size: # then we check if the table is bigger than or equal to party size, if it is, we return it.
                free.append(table_data[0][occupied_state])
            else: # if the table isn't open or isn't big enough for the party, we continue the loop.
                continue
    return free # output free tables

print(list_all_free_tables_under_party_size(4, restaurant_tables2, 2))


def list_all_free_tables_and_combined_tables(time_slot: int, table_data: list, party_size: int) -> list:
    """
        LEVEL 4: this function is used to return the free tables and adjacent tables in a specific time slot, equal
        to or above the party size.
        """
    free = [] # output list
    for occupied_state in range(1, len(table_data)):  # loop over the occupied state in given time slot
        if table_data[time_slot][occupied_state] == 'o':  # if the table is open
            if int(table_data[0][occupied_state][3]) >= party_size: # then we check if the table is bigger than or equal to party size, if it is, we append it
                free.append(table_data[0][occupied_state])
            elif occupied_state - 1 <= len(table_data[time_slot]):
                if table_data[time_slot][occupied_state - 1] == 'o' and table_data[time_slot][occupied_state + 1] == 'o': # if not, we check if the adjacent tables are free
                    if int(table_data[0][occupied_state - 1][3:-1]) + int(table_data[0][occupied_state + 1][3:-1]) >= party_size: # if they are, then we check if the adjacent tables together are bigger than or equal
                    # to the party size
                        group = [table_data[0][occupied_state - 1], table_data[0][occupied_state + 1]] # if they are, we append them into as list together
                    # and then append that list to the free output
                        free.append(group)
                        continue
                else: # if both if statement conditionals are false, then we continue to the next iteration of the loop
                    continue
    return free # output free tables

print(list_all_free_tables_and_combined_tables(1, restaurant_tables2, 4))
