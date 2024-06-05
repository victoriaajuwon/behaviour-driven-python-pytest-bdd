@service @restfulbookerbooking
Feature: DuckDuckGo Instant Answer API
    As an application developer,
    I want to get instant answers for search terms via a REST API,
    So that my app can get answers anywhere.

    Scenario Outline: Basic RestfulBooker Booking API Query
        Given the RestfulBooker bookings API is queried with "<id>"
        Then the response status code is "200"
        And the response contains "<firstname>"

        Examples: Animals
            | id | firstname  |
            | 4  | Jim  |
            | 69  | Josh  |
            | 9  | Mary  |
            | 15  | Josh  |
            | 20  | John  |
            | 136  | Josh  |