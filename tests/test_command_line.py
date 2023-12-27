from scraper import main
import pytest

# Due to each input param being a different file type, it should be easy to not care about the order and just check
filterPath = 'tests/filters/filter1.txt'
folderPath = 'tests/sample4'

# Standard use case of program
def test_standard():
    # Not sure how to do it, so making it so main() accepts a list of strings, which just parses in the cmdl args
    args = ['scraper.py', filterPath, folderPath]
    assert main(args) == True

# As long as args are valid, the order shouldn't matter
def test_reverse():
    args = ['scraper.py', filterPath, folderPath]
    r_args = ['scraper.py', folderPath, filterPath]

    assert main(args) == True
    with open('output.csv', 'r') as f:
        outA = f.read()
    
    assert main(r_args) == True
    with open('output.csv', 'r') as f:
        outB = f.read()

    assert outA == outB

# If there are excess arguments, should tell user
def test_extra_args():
    args = ['scraper.py', filterPath, folderPath, 'foo', 'bar']
    
    assert main(args) == False

# Standard error of no args provided
def test_empty_args():
    args = ['scraper.py']

    assert main(args) == False

# Missing the folder/file
def test_missing_args():
    args = ['scraper.py', filterPath]

    assert main(args) == False

# Ensures that a list of targets is input
def test_missing_check():
    args = ['scraper.py', folderPath]

    assert main(args) == False