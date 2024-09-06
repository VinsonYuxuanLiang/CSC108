"""CSC108H1S: Functions for Assignment 3 - Airports and Routes.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 The CSC108 Team
"""
from flight_constants import AirportDict, RouteDict, OPENFLIGHTS_NULL_VALUE

import flight_example_data


################################################################################
# Part 2 - Querying the data
################################################################################

def is_direct_flight(routes: RouteDict, start: str, end: str) -> bool:
    '''return true iff start airport and end airport has direct flight base on
    routes dict
    
    >>> example_routes = flight_example_data.create_example_routes()
    >>> is_direct_flight(example_routes, 'GFN', 'TRO')
    True
    >>> is_direct_flight(example_routes, 'GFN', 'RCM')
    False
    '''
    k = routes.keys()
    for a in k:
        if a == start and end in routes[a].keys():
            return True
    return False


def is_valid_flight_sequence(routes: RouteDict, airports: list[str]) -> bool:
    '''return true iff adjacent airport in airports based on the routes data
    
    precondiction: len(airports) at least 2
    
    >>> example_routes = flight_example_data.create_example_routes()
    >>> flight = ['TRO', 'GFN', 'JCK']
    >>> is_valid_flight_sequence(example_routes, flight)
    False
    >>> flight = ['TRO', 'GFN']
    >>> is_valid_flight_sequence(example_routes, flight)
    True
    '''
    k = routes.keys()
    for a in k:
        index = 0
        while index < (len(airports) - 1):
            if a == airports[index] and airports[index + 1] in routes[a].keys():
                index += 1
            elif a == airports[index] and airports[index + 1]\
                 not in routes[a].keys():
                return False
            elif a != airports[index]:
                index += 1
    return True


def summarize_by_timezone(airports: AirportDict) -> dict[str, int]:
    '''summarize the airport in airports data by 'Tz' (timezone) 
    column in each airport
    
    >>> example_airports = flight_example_data.create_handout_airports()
    >>> summarize_by_timezone(example_airports)
    {'Australia/Sydney': 1, 'Australia/Brisbane': 1}
    >>> example_airports = flight_example_data.create_example_airports()
    >>> summarize_by_timezone(example_airports)
    {'Australia/Brisbane': 1, 'Australia/Sydney': 3}
    '''
    d = {}
    k = airports.keys()
    tz = []
    for a in k:
        if airports[a]['Tz'] != OPENFLIGHTS_NULL_VALUE:
            if airports[a]['Tz'] not in tz:
                tz += [airports[a]['Tz']]
                d[airports[a]['Tz']] = 1
            elif airports[a]['Tz'] in tz:
                d[airports[a]['Tz']] += 1
    return d
            
        
################################################################################
# Part 3 - Implementing useful algorithms
################################################################################

def find_reachable_destinations(routes: RouteDict, source: str, n: int) -> \
        list[str]:
    """Return the list of IATA airport codes that are reachable from source by
    taking at most n direct flights.

    The list should not contain an IATA airport code more than once. The airport
    codes in the list should appear in lexicographical order (use the
    list.sort method on a list of strings to achieve this).

    Preconditions:
        - n >= 1
        - (source in routes) is True

    >>> example_routes = flight_example_data.create_example_routes()
    >>> find_reachable_destinations(example_routes, 'GFN', 1)
    ['TRO']
    >>> find_reachable_destinations(example_routes, 'GFN', 2)
    ['GFN', 'SYD', 'TRO']
    """
    l = []
    a = n
    z = [source]
    while a != 0:
        l = check_list_in_dict_and_update(routes, z, l)
        z = l 
        a = a - 1
    l.sort()     
    return l


def check_list_in_dict_and_update(routes: RouteDict, z: list[str], 
                                  l: list[str]) -> list[str]:
    '''return updated list l after checking all elements in z list is in the 
    keys of routes dict and update list l with the elements' keys 
    in routes data.
    
    >>> l = []
    >>> z = ['GFN']
    >>> example_routes = flight_example_data.create_example_routes()
    >>> check_list_in_dict_and_update(example_routes, z, l)
    ['TRO']
    
    NOTE: this is a helper function
    '''
    for c in z:
        if c in routes.keys():
            for b in routes[c].keys():
                if b not in l:
                    l += [b]
    return l 
    

def decomission_plane(routes: RouteDict, plane: str) -> list[tuple[str, str]]:
    """Update routes by removing plane from all source-destination routes that
    use plane. Do not remove the source-destination pair, only the plane.

    In addition, return a sorted list of two-element tuples where the first
    index is source and the second index is destination (use the list.sort
    method on a list of tuples to achieve this). The list includes *all* routes
    that that have no planes that can be used.

    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'DH4')
    []
    >>> example_routes['TRO']['SYD']
    ['SF3']
    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'SF3')
    [('GFN', 'TRO'), ('JCK', 'RCM'), ('RCM', 'JCK'), ('TRO', 'GFN')]
    >>> example_routes['TRO']['SYD']
    ['DH4']
    """
    for a in list(routes.keys()):
        for b in list(routes[a].keys()):
            if plane in routes[a][b]:
                routes[a][b].remove(plane)
    l = []
    for a in list(routes.keys()):
        for b in list(routes[a].keys()):
            if routes[a][b] == []:
                l += [(a, b)]
    return l
            

if __name__ == '__main__':
    # On A3 we do not have a separate checker but instead include code that
    # performs the required checks.  This code requires python_ta to be
    # installed.  See the 'Completing the CSC108 Setup' section in the
    # Software Installation page on Quercus for details.

    # Uncomment the 3 lines below to have function type contracts checked
    # # Enable type contract checking for the functions in this file
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # Check the correctness of the doctest examples
    import doctest
    doctest.testmod()

    # Uncomment the 2 lines below to check your code style with python_ta
    # import python_ta
    # python_ta.check_all(config='pyta/a3_pyta.txt')
