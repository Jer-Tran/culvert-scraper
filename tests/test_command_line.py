from scraper import main
import pytest

# Due to each input param being a different file type, it should be easy to not care about the order and just check

# Standard use case of program
@pytest.mark.skip(reason="currently unimplemented")
def test_standard():
    # Not sure how to do it, so making it so main() accepts a list of strings, which just parses in the cmdl args
    args = ['scraper.py', 'tests/filters/filter1.txt', 'tests/sample1']
    main(args)

# As long as args are valid, the order shouldn't matter
@pytest.mark.skip(reason="currently unimplemented")
def test_reverse():
    args = ['scraper.py', 'tests/filters/filter1.txt', 'tests/sample1']
    r_args = ['scraper.py', 'tests/sample1', 'tests/filters/filter1.txt']

    main(args)
    with open('output.txt', 'r') as f:
        outA = f.read()
    
    main(r_args)
    with open('output.txt', 'r') as f:
        outB = f.read()

    assert outA == outB

# If there are excess arguments, should tell user
@pytest.mark.skip(reason="currently unimplemented")
def test_extra_args():
    args = ['scraper.py', 'filter1.txt', 'tests/sample1', 'foo', 'bar']
    with pytest.raises(Exception):
        main(args)

# Standard error of no args provided
@pytest.mark.skip(reason="currently unimplemented")
def test_empty_args():
    args = ['scraper.py']
    with pytest.raises(Exception):
        main(args)

# Missing the folder/file
@pytest.mark.skip(reason="currently unimplemented")
def test_missing_args():
    args = ['scraper.py', 'filter1.txt']
    with pytest.raises(Exception):
        main(args)

# Ensures that a list of targets is input
@pytest.mark.skip(reason="currently unimplemented")
def test_missing_check():
    args = ['scraper.py', 'tests/sample1']

    with pytest.raises(Exception):
        main(args)