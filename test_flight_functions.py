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
import pytest

from flight_functions import summarize_by_timezone, is_valid_flight_sequence
from flight_example_data import create_example_airports, create_example_routes
from flight_constants import OPENFLIGHTS_NULL_VALUE


################################################################################
# Part 4 - Writing unit tests
################################################################################

"""Unit tests for the summarize_by_timezone function."""


def test_no_airports() -> None:
    """Test that an empty dictionary is returned when there are no airports
    given.

    This test case is done for you. Consider using it as a reference.
    """

    # No airports is an empty dictionary
    no_airports = {}
    # We expect an empty dictionary in return
    expected = {}
    # Call the function we are testing and save a reference to the result
    actual = summarize_by_timezone(no_airports)
    # Check whether what we expected was the same as the returned result
    assert actual == expected


def test_only_null_airports() -> None:
    """Test that an empty dictionary is returned when every airport in the
    input dictionary has a Null value (i.e., OPENFLIGHTS_NULL_VALUE) for
    their timezone.
    """

    # Create a dictionary with at least two airports, where every
    # airport has a value of OPENFLIGHTS_NULL_VALUE for their 'Tz' key.
    # The provided code starts with an empty dictionary. Modify this statement
    # to create a dictionary with at least two airports.
    airports = {'TRO':{
                    'Name': 'abc',
                    'City': 'abc',
                    'Country': 'abc',
                    'Latitude': 'abc',
                    'Longitude': 'abc',
                    'Tz': OPENFLIGHTS_NULL_VALUE}, 
                'RCM':{
                    'Name': 'def',
                    'City': 'def',
                    'Country': 'def',
                    'Latitude': 'def',
                    'Longitude': 'def',
                    'Tz': OPENFLIGHTS_NULL_VALUE}
                }

    # We expect an empty dictionary in return
    expected = {}
    actual = summarize_by_timezone(airports)

    # Finish the test case below.
    assert actual == expected


def test_no_mutation() -> None:
    """Test that the airports given as an argument *is not* mutated.
    """

    airports = create_example_airports()

    # Call the function we are testing. We don't need to save the result
    # because we are not checking the value. We are testing that the argument
    # was not mutated.
    actual = summarize_by_timezone(airports)

    # Finish the test case below to check whether the argument airports
    # was mutated
    expected = {'Australia/Brisbane': 1, 'Australia/Sydney': 3}
    assert actual == expected


"""Unit tests for the is_valid_flight_sequence function."""


def test_one_valid_direct_flight() -> None:
    """Test that the function returns True when the flight sequence is a
    valid direct flight.

    This test case is done for you. Consider using it as a reference.
    """

    routes = create_example_routes()
    expected = True
    sequence = ['GFN', 'TRO']

    actual = is_valid_flight_sequence(routes, sequence)
    assert actual == expected


# Add test functions below to create a complete set of tests. Based on
# what you have learned in Week 8, you may want to consider:
#       - size
#       - dichotomies
#       - boundaries
#       - order
def test_two_valid_direct_flight() -> None:
    '''test that the function returns True when the flight sequence is a
    valid direct flight.
    '''
    routes = create_example_routes()
    expected = True
    sequence = ['GFN', 'TRO', 'SYD']

    actual = is_valid_flight_sequence(routes, sequence)
    assert actual == expected
    

def test_not_valid_direct_flight() -> None:
    '''test that the function returns False when the flight sequence is not a
    valid direct flight.
    '''
    routes = create_example_routes()
    expected = False
    sequence = ['GFN', 'SYD']

    actual = is_valid_flight_sequence(routes, sequence)
    assert actual == expected
    

def test_first_one_valid_direct_flight() -> None:
    '''test that the function returns True when the flight sequence is a
    valid direct flight.
    '''
    routes = create_example_routes()
    expected = False
    sequence = ['GFN', 'TRO', 'RCM']

    actual = is_valid_flight_sequence(routes, sequence)
    assert actual == expected
    

def test_lase_one_valid_direct_flight() -> None:
    '''test that the function returns True when the flight sequence is a
    valid direct flight.
    '''
    routes = create_example_routes()
    expected = False
    sequence = ['RCM', 'TRO', 'SYD']

    actual = is_valid_flight_sequence(routes, sequence)
    assert actual == expected
    
    
if __name__ == '__main__':
    # # Uncomment the 2 lines below to check your code style with python_ta
    import python_ta
    python_ta.check_all(config='pyta/a3_pyta.txt')

    # Perform the unit tests using pytest
    pytest.main(['test_flight_functions.py'])
