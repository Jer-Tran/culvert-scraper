from scraper import translate_names
import pytest

# Given how diff the functionality is, considering splitting functionality with filter, or at least partitioning it

# Translates truncated names to full, using file
def test_standard(): # TODO: fill in data later
    filters = [('a', 'aa')]
    data = [('name', 'value')]
    output = translate_names(data, filters)
    expected = []

    assert output != data
    assert output == expected

# Tr doesn't exist for an abbreviated name
def test_missing_tr(): # TODO: fill in data later
    filters = ['a', 'b']
    data = [('name', 1)]
    output = translate_names(data, filters)

    # Reasoning - If it doesn't show up in the filter, it will get filtered out later
    assert output == data

# When the input image has no truncated names
def test_no_trs(): # TODO: fill in data later
    filters = ['a', 'b']
    data = [('name', 1)]
    output = translate_names(data, filters)

    assert output == data

# Tr exists for data points that don't exist
def test_extra_trs():# TODO: fill in data later
    filters = ['a', 'b']
    data = [('name', 1)]
    output = translate_names(data, filters)

    assert output == data
    assert output == [('name', 'value')]

# Empty list as input
def test_no_data(): # TODO: fill in data later
    filters = ['a', 'b']
    data = []
    output = translate_names(data, filters)

    assert output == []

# No overlap between
def test_no_match(): # TODO: fill in data later
    filters = ['a', 'b']
    data = [('name', 1)]
    output = translate_names(data, filters)

    assert output == data

# Filter var is empty, so nothing is needed to be translated
def test_empty_filter():
    filters = []
    data = [('name', 1)]
    output = translate_names(data, filters)

    assert output == data

# Rare case, when two truncated names look identical
# Handling here is to skip, safer to be unsure and require manual input
def test_uncertainty(): # TODO: fill in data later
    filters = ['a', 'b']
    data = [('name', 1)]
    output = translate_names(data, filters)

    assert output == data
    assert output == [('name', 1)]
