from scraper import main
import pytest

def test_standard():
    # Not sure how to do it, so making it so main() accepts a list of strings, which just parses in the cmdl args
    args = ['scraper.py', 'filter1.txt', 'sample1']
    main(args)

def test_reverse():
    args = ['scraper.py', 'filter1.txt', 'sample1']

    r_args = args.reverse()

    main(args)
    with open('output.txt', 'r') as f:
        outA = f.read()
    
    main(r_args)
    with open('output.txt', 'r') as f:
        outB = f.read()

    assert outA == outB

def test_empty():
    args = ['scraper.py']
    with pytest.raises(Exception):
        main(args)

def test_missing_check():
    args = ['scraper.py', 'filter1.txt', 'sample1']

    with pytest.raises(Exception):
        main(args)