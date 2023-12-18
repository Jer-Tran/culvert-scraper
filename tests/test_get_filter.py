from scraper import get_filters
import pytest

# May change this funciton to accept csv files as well, since it would be reasonably to produce the contents on excel then export

def test_standard():
    filters = get_filters('tesst/filters/filter1.txt')
    assert filters == ['a', 'b', 'c']
    assert sorted(filters) == filters

    filters = get_filters('tests/filters/filter2.txt')
    assert filters == ['d', 'e', 'f']
    assert sorted(filters) == filters

    # Etc for each produced filter

# file doesn't exist
def test_bad_path():
    with pytest.raises(Exception):
        get_filters('notapath')

# If specific file not specified
def test_folder():
    with pytest.raises(Exception):
        get_filters('tests/filters')

# Gets a text file that can be read, but the contents aren't in a valid format
# Maybe this would get expanded upon further
def test_invalid_format():
    with pytest.raises(Exception):
        get_filters('tests/filtes/badfilter.txt')

