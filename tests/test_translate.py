from scraper import translate_names
import pytest

# Given how diff the functionality is, considering splitting functionality with filter, or at least partitioning it
# In-game, it appears to truncate based on length, so this will be a bit difficult to standardise

# Translates truncated names to full, using file
# @pytest.mark.skip(reason="currently unimplemented")
def test_standard():
    filters = ['boshi', 'defenestration', 'pryce']
    data = [('boshi', 10), ('defenestr..', 11), ('pryce', 12)]
    output = translate_names(data, filters)
    expected = [('boshi', 10), ('defenestration', 11), ('pryce', 12)]

    assert output != data
    assert output == expected

# Both that order does not affect the translation, and order is preserved
# @pytest.mark.skip(reason="currently unimplemented")
def test_order():
    filters = ['boshi', 'hendrix', 'cordialisation']
    data = [('cordialis..', 11), ('boshi', 12), ('hendrix', 13)]
    output = translate_names(data, filters)
    expected = [('cordialisation', 11), ('boshi', 12), ('hendrix', 13)]

    assert output != data
    assert output == expected

# The length of the truncation shouldn't matter, in accordance to in-game variance
# @pytest.mark.skip(reason="currently unimplemented")
def test_varied_tr_length():
    filters = ['boshi', 'hendrix', 'cordialisation']
    data = [('cordialis..', 11), ('bo..', 12), ('hen..', 13)]
    output = translate_names(data, filters)
    expected = [('cordialisation', 11), ('boshi', 12), ('hendrix', 13)]

    assert output != data
    assert output == expected

# Tr doesn't exist for an abbreviated name
# @pytest.mark.skip(reason="currently unimplemented")
def test_missing_tr():
    filters = ['birdy', 'philip']
    data = [('anasta..', 1), ('phil..', 2)]
    output = translate_names(data, filters)
    expected = [('anasta..', 1), ('philip', 2)]

    # Reasoning - If it doesn't show up in the filter, it will get filtered out later
    assert output != data
    assert output == expected

# Where one name is a substring of one in the filter
# @pytest.mark.skip(reason="currently unimplemented")
def test_substr():
    filters = ['abcd', 'focal']
    data = [('abcdef..', 11), ('focal..', 12)]
    output = translate_names(data, filters)

    assert output == data

# Matches require case sensitivity
# @pytest.mark.skip(reason="currently unimplemented")
def test_case_sensitive():
    filters = ['alan', 'furina']
    data = [('Ala..', 11), ('Furi..', 12)]
    output = translate_names(data, filters)

    assert output == data

# When the input image has no truncated names
# @pytest.mark.skip(reason="currently unimplemented")
def test_no_trs():
    filters = ['alan', 'smithee']
    data = [('alan', 1), ('smithee', 2)]
    output = translate_names(data, filters)

    assert output == data

# Empty list as input
# @pytest.mark.skip(reason="currently unimplemented")
def test_no_data():
    filters = ['a', 'b']
    data = []
    output = translate_names(data, filters)

    assert output == []

# No overlap between
# @pytest.mark.skip(reason="currently unimplemented")
def test_no_match():
    filters = ['a', 'b']
    data = [('name', 1)]
    output = translate_names(data, filters)

    assert output == data

# Filter var is empty, so nothing is needed to be translated
# @pytest.mark.skip(reason="currently unimplemented")
def test_empty_filter():
    filters = []
    data = [('name', 1)]
    output = translate_names(data, filters)

    assert output == data

# Rare case, when two truncated names look identical
# Handling here is to skip, safer to be unsure and require manual input
# @pytest.mark.skip(reason="currently unimplemented")
def test_uncertainty_double_filter():
    filters = ['immolation', 'immolate', 'fred']
    data = [('immo..', 2), ('fred', 14)]
    output = translate_names(data, filters)

    assert output == data

# @pytest.mark.skip(reason="currently unimplemented")
def test_uncertain_double_data():
    filters = ['fragment', 'force']
    data = [('fragm..', 2), ('frag..', 3)]
    output = translate_names(data, filters)

    assert output == data

# @pytest.mark.skip(reason="currently unimplemented")
def test_uncertain_double_data_filter():
    filters = ['fragment', 'fragments']
    data = [('fragm..', 2), ('frag..', 3)]
    output = translate_names(data, filters)

    assert output == data
