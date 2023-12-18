from scraper import main
import pytest

# Standard use case of program
def test_standard():
    # Not sure how to do it, so making it so main() accepts a list of strings, which just parses in the cmdl args
    args = ['scraper.py', 'filter1.txt', 'tests/sample1']
    main(args)

# As long as args are valid, the order shouldn't matter
def test_reverse():
    args = ['scraper.py', 'filter1.txt', 'tests/sample1']

    r_args = args.reverse()

    main(args)
    with open('output.txt', 'r') as f:
        outA = f.read()
    
    main(r_args)
    with open('output.txt', 'r') as f:
        outB = f.read()

    assert outA == outB

# If there are excess arguments, should tell user
def test_extra_args():
    args = ['scraper.py', 'filter1.txt', 'tests/sample1', 'foo', 'bar']
    with pytest.raises(Exception):
        main(args)

# Standard error of no args provided
def test_empty_args():
    args = ['scraper.py']
    with pytest.raises(Exception):
        main(args)

# Missing the folder/file
def test_missing_args():
    args = ['scraper.py', 'filter1.txt']
    with pytest.raises(Exception):
        main(args)

# Ensures that a list of targets is input
def test_missing_check():
    args = ['scraper.py', 'tests/sample1']

    with pytest.raises(Exception):
        main(args)