from scraper import get_filters
import pytest

# May change this funciton to accept csv files as well, since it would be reasonably to produce the contents on excel then export
filterPath = 'tests/filters/'

def test_standard(): # If the filters are changed to work better with the output tests, don't forget to change here
    filters = get_filters(filterPath + 'filter1.txt')
    assert filters == ['a', 'b', 'c']
    assert sorted(filters) == filters
    assert len(set(filters)) == len(filters)

def test_order():
    filters = get_filters(filterPath + 'filter2.txt')
    assert filters == ['diogenes', 'europa', 'french']
    assert sorted(filters) == filters
    assert len(set(filters)) == len(filters)

# file doesn't exist
def test_bad_path():
    with pytest.raises(Exception):
        get_filters('notapath')

# If specific file not specified
def test_folder():
    with pytest.raises(Exception):
        get_filters('culvert-scraper/tests/filters')

# Gets a text file that can be read, but the contents aren't in a valid format
# Maybe this would get expanded upon further

# Names in-game have restrictions, and we are checking similar restrictions also as a sanity check
def test_invalid_content():
    with pytest.raises(Exception):
        get_filters(filterPath + 'badcontent.txt')

# Accented chars are allowed
def test_accented_chars():
    filters = get_filters(filterPath + 'filter3.txt')
    assert filters == ['Addréss', 'BrÎlliant', 'Cât']

# A filter with dupliate names
def test_dupe_name():
    with pytest.raises(Exception):
        get_filters(filterPath + 'filter4.txt')