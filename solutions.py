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
    free = []  # create our output list, this will output our list of free tables
    for occupied_state in range(1, len(table_data[time_slot])):  # here we check make a for loop that skips the first index
        # of the chosen time slot because we know that will just contain the number of the time slot and not an actual
        # useful piece of data.
        if table_data[time_slot][
            occupied_state] == 'o':  # if the table has, an occupied_state of false, then we go to the header
            # and find the table corresponding to that occupancy state and append it to the list of free tables.
            free.append(table_data[0][occupied_state])
    return free  # return list of free tables.


print(list_all_free_tables(1, restaurant_tables2))

def list_one_free_table_under_party_size(time_slot: int, table_data: list, party_size: int):
    """
        LEVEL 2: this function is used to return one free table in a specific time slot and equal
        to or above the party size.
        """
    for occupied_state in range(1, len(table_data[time_slot])):  # loop over the occupied state in given time slot
        if table_data[time_slot][occupied_state] == 'o':  # if the table is open
            if int(table_data[0][occupied_state][
                       3]) >= party_size:  # then we check if the table is bigger than or equal to party size, if it is, we return it.
                return table_data[0][occupied_state]
            else:  # if the table isn't open or isn't big enough for the party, we continue the loop.
                continue


print(list_one_free_table_under_party_size(1, restaurant_tables2, 2))

def list_all_free_tables_under_party_size(time_slot: int, table_data: list, party_size: int) -> list:
    """
        LEVEL 3: this function is used to return the free tables in a specific time slot and equal
        to or above the party size.
        """
    free = []  # output list
    for occupied_state in range(1, len(table_data[time_slot])):  # loop over the occupied state in given time slot
        if table_data[time_slot][occupied_state] == 'o':  # if the table is open
            if int(table_data[0][occupied_state][
                       3]) >= party_size:  # then we check if the table is bigger than or equal to party size, if it is, we return it.
                free.append(table_data[0][occupied_state])
            else:  # if the table isn't open or isn't big enough for the party, we continue the loop.
                continue
    return free  # output free tables


print(list_all_free_tables_under_party_size(4, restaurant_tables2, 2))


def list_all_free_tables_and_combined_tables(time_slot: int, table_data: list, party_size: int) -> list:
    """
        LEVEL 4: this function is used to return the free tables and adjacent tables in a specific time slot, equal
        to or above the party size.
        """
    free = []  # output list
    for occupied_state in range(1, len(table_data[time_slot])):  # loop over the occupied state in given time slot
        if table_data[time_slot][occupied_state] == 'o' and int(table_data[0][occupied_state][3]) >= party_size:  # if the table is open and can fit the party, we append it to the free tables list.
            free.append(table_data[0][occupied_state])
        elif (occupied_state - 1 >= 1 and occupied_state + 1 < len(table_data[time_slot]) and # elif both adjacent tables are free and both combined would be bigger than or equal to the party size, we append that combination to the free tables list.
              table_data[time_slot][occupied_state - 1] == 'o' and table_data[time_slot][
                  occupied_state + 1] == 'o' and
              int(table_data[0][occupied_state - 1][3]) + int(
                    table_data[0][occupied_state + 1][3]) >= party_size):
            free.append([table_data[0][occupied_state - 1], table_data[0][occupied_state + 1]])

    return free  # output free tables


print(list_all_free_tables_and_combined_tables(1, restaurant_tables2, 8))


def list_all_free_tables_and_combines_tables_friendly(time_slot: int, table_data: list, party_size: int):
    """
    BONUS: this function is used to return the free tables and adjacent tables in a specific time slot, equal
    to or above the party size. Also, gives a user-friendly response.
    """
    # this is a helper function to make the code more readable.
    def get_table_capacity(table_name: str):
        start = table_name.find('(') + 1
        end = table_name.find(')')
        return int(table_name[start:end])

    free = [] # free tables and combination of tables list
    for occupied_state in range(1, len(table_data[time_slot])):  # loop over the occupied state in given time slot
        is_open = table_data[time_slot][occupied_state] == 'o' # define is_open for better readability
        current_table = table_data[0][occupied_state] # define current_table for quick access to current table

        if is_open and get_table_capacity(current_table) >= party_size:  # if table is open and has a capacity larger or equal to party size, we append it to the free tables list.
            free.append(current_table)
        elif occupied_state - 1 >= 1 and occupied_state + 1 < len(table_data[time_slot]): # else if the adjacent tables are not out of bounds
            prev_table = table_data[0][occupied_state - 1]
            next_table = table_data[0][occupied_state + 1]
            prev_is_open = table_data[time_slot][occupied_state - 1] == 'o'
            next_is_open = table_data[time_slot][occupied_state + 1] == 'o'
            if prev_is_open and next_is_open and (get_table_capacity(prev_table) + get_table_capacity(next_table)) >= party_size: # if the capacities of both adjacent tables are bigger
                # than or equal to the party size,
                # we append it to the free list inside a list to represent it is a combo of 2 tables.
                free.append([prev_table, next_table])

    for tables in free: # looping through all the free tables
        if isinstance(tables, list): # if the element is a list, it means it is a combo of 2 tables
            table1 = tables[0][tables[0].find('T') + 1:tables[0].find('(')]
            table2 = tables[1][tables[1].find('T') + 1:tables[1].find('(')]
            print(f"combining table {table1} + table {table2} will be enough to fit your party size.") # we then print to the user both tables combined will accommodate their party size
        else: # else we just print the table and say its free
            print(f"table {tables[tables.find('T') + 1:tables.find('(')]} is free and big enough for your party.")


list_all_free_tables_and_combines_tables_friendly(1, restaurant_tables2, 8)
