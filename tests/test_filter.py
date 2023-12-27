from scraper import filter_names
import pytest

# Assumes all truncated names have been translated where possible

# From list of data, only certain names are output
# @pytest.mark.skip(reason="currently unimplemented")
def test_standard():
    data = [('a', 1), ('b', 2), ('c', 3)]
    filter = ['a', 'c']
    output = filter_names(data, filter)

    assert output != data
    assert output == [('a', 1), ('c', 3)]

# In case, where user does not have an input file, thus not filtering
# Will have to consider more about a 'no filter' functionality for this, maybe it'll just be implemented to skip this function in the parent function
# def test_no_filter():
#     filters = ['a', 'b']
#     data = [('name', 1)]
#     output = filter_names(data, filters)

#     assert output == data

# @pytest.mark.skip(reason="currently unimplemented")
def test_exact_match():
    data = [('a', 1), ('B', 2)]
    filter = ['a', 'b']
    output = filter_names(data, filter)

    assert output != data
    assert output == [('a', 1)]

# @pytest.mark.skip(reason="currently unimplemented")
def test_substring():
    data = [('a', 1), ('bb', 2)]
    filter = ['a', 'b']
    output = filter_names(data, filter)

    assert output != data
    assert output == [('a', 1)]

# Exact match check -> Ignores truncation
# @pytest.mark.skip(reason="currently unimplemented")
def test_truncated():
    data = [('a', 1), ('b..', 2)]
    filter = ['a', 'balance', 'b']
    output = filter_names(data, filter)

    assert output != data
    assert output == [('a', 1)]

# Filter file contains names that do not appear in data
# @pytest.mark.skip(reason="currently unimplemented")
def test_extra_filter():
    filters = ['a', 'b']
    data = [('name', 1)]
    output = filter_names(data, filters)

    assert len(output) < len(data)
    assert output == []

# Filter file contains no names
# @pytest.mark.skip(reason="currently unimplemented")
def test_empty_filter():
    filters = []
    data = [('name', 1)]
    output = filter_names(data, filters)

    assert output == []

# With empty data, output is empty data
# @pytest.mark.skip(reason="currently unimplemented")
def test_empty():
    filters = ['a', 'b']
    data = []
    output = filter_names(data, filters)

    assert output == []

# The data produced contains no members that are specified to be output
# @pytest.mark.skip(reason="currently unimplemented")
def test_no_out():
    filters = ['a', 'b']
    data = [('name', 1)]
    output = filter_names(data, filters)

    assert output == []

# Potentially possible, and is a case of requiring user intervention
# @pytest.mark.skip(reason="currently unimplemented")
def test_duplicate_data():
    filters = ['a', 'b']
    data = [('a', 1), ('a', 2), ('a', 3)]
    output = filter_names(data, filters)

    assert output == [] # There is uncertainty, and thus we cannot accept it
    # TODO: Again, check that user is notified if this happens

# Shouldn't happen, but must be considered
# @pytest.mark.skip(reason="currently unimplemented")
def test_duplicate_filter():
    filters = ['a', 'a', 'b']
    data = [('a', 1), ('b', 2)]
    output = filter_names(data, filters)

    assert output == data
