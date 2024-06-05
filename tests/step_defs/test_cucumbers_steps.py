from functools import partial
from pytest_bdd import scenario, parsers, given, scenarios, when, then

from cucumbers import CucumberBasket

scenarios('../features/radish.feature')

EXTRA_TYPES ={
    'Number': int,
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}

parse_num = partial(parsers.cfparse, converters= CONVERTERS)

@given(
  parsers.cfparse('the basket has "{initial}" cucumbers'),
  target_fixture='basket',
  converters=CONVERTERS)
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.parse('"{some}" cucumbers are added to the basket'),
  converters=CONVERTERS)
def add_cucumbers(basket, some):
    basket.add(some)
    
    
@when(parsers.parse('"{some}" cucumbers are removed from the basket'),
  converters=CONVERTERS)
def remove_cucumbers(basket, some):
    basket.remove(some)
    
    
@then(parsers.parse('the basket contains "{total}" cucumbers'),
  converters=CONVERTERS)
def basket_has_total(basket, total):
    assert basket.count == total