from scraper import filter_names
import pytest

# From list of data, only certain names are output
def test_standard():
    data = [('a', 1), ('b', 2)]
    filter = ['a', 'b']
    output = filter_names(data, filter)

    assert output != data
    assert output == [('a', 1)]

# In case, where user does not have an input file, thus not filtering
# Will have to consider more about a 'no filter' functionality for this, maybe it'll just be implemented to skip this function in the parent function
# def test_no_filter():
#     filters = ['a', 'b']
#     data = [('name', 1)]
#     output = filter_names(data, filters)

#     assert output == data

# Filter file contains names that do not appear in data
def test_extra_filter():
    filters = ['a', 'b']
    data = [('name', 1)]
    output = filter_names(data, filters)

    assert len(output) < len(data)
    assert output == [('name', 2)]
    # Need to check somewhere that these missed filters are showed to user
    # Maybe as a function that gets the list of names, and that's checked

# Filter file contains no names
def test_empty_filter():
    filters = ['a', 'b']
    data = [('name', 1)]
    output = filter_names(data, filters)

    assert output == []

# With empty data, output is empty data
def test_empty():
    filters = ['a', 'b']
    data = []
    output = filter_names(data, filters)

    assert output == []

# The data produced contains no members that are specified to be output
def test_no_out():
    filters = ['a', 'b']
    data = [('name', 1)]
    output = filter_names(data, filters)

    assert output == []