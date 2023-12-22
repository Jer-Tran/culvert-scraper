from scraper import main
import pytest

# Due to each input param being a different file type, it should be easy to not care about the order and just check

# Standard use case of program
def test_standard():
    # Not sure how to do it, so making it so main() accepts a list of strings, which just parses in the cmdl args
    args = ['scraper.py', 'tests/filters/filter1.txt', 'tests/sample1']
    assert main(args) == True

# As long as args are valid, the order shouldn't matter
def test_reverse():
    args = ['scraper.py', 'tests/filters/filter1.txt', 'tests/sample1']
    r_args = ['scraper.py', 'tests/sample1', 'tests/filters/filter1.txt']

    assert main(args) == True
    with open('output.csv', 'r') as f:
        outA = f.read()
    
    assert main(r_args) == True
    with open('output.csv', 'r') as f:
        outB = f.read()

    assert outA == outB

# If there are excess arguments, should tell user
def test_extra_args():
    args = ['scraper.py', 'filter1.txt', 'tests/sample1', 'foo', 'bar']
    # with pytest.raises(Exception):
    #     main(args)
    assert main(args) == False

# Standard error of no args provided
def test_empty_args():
    args = ['scraper.py']

    assert main(args) == False

# Missing the folder/file
def test_missing_args():
    args = ['scraper.py', 'filter1.txt']

    assert main(args) == False

# Ensures that a list of targets is input
def test_missing_check():
    args = ['scraper.py', 'tests/sample1']

    assert main(args) == False