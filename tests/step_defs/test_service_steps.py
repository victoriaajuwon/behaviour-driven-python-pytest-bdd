"""
This module contains step definitions for service.features.
It uses the requests packages:
http://docs.python-requests.org
"""

import requests

from pytest_bdd import scenarios, parsers, given, then

# Shared variables
RESTFUL_BOOKER_BOOKING_API = 'https://restful-booker.herokuapp.com/booking/'

# Scenarios
scenarios('../features/service.feature')

CONVERTERS = {
    'code': int,
    'id': int,
    'firstname': str,
}

# Given steps

@given(
    parsers.parse('the RestfulBooker bookings API is queried with "{id}"'),
    target_fixture='rbb_response',
    converters=CONVERTERS
)
def rbb_response(id):
    url = f"{RESTFUL_BOOKER_BOOKING_API}{id}"
    response = requests.get(url)
    print(response.url)
    return response


#Then Steps
@then(
    parsers.parse('the response contains "{firstname}"'),
    converters=CONVERTERS
)
def rbb_response_contents(rbb_response, firstname):
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    print(rbb_response)
    assert firstname.lower() == rbb_response.json()['firstname'].lower()
    
    
@then(
    parsers.parse('the response status code is "{code}"'),
    converters=CONVERTERS
)
def rbb_response_code(rbb_response, code):
    assert rbb_response.status_code == code