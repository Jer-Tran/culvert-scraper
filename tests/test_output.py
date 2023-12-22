from scraper import main
import pytest
from os.path import isfile 

# Because function produces output file in cmd, have to be careful
@pytest.mark.skip(reason="currently unimplemented")
def test_invalid_path():
    args = ['scraper.py', 'filter1.txt', 'notafile']
    main(args)

    assert not isfile('output.csv')

# When the images are not valid format, and thus produce an error
@pytest.mark.skip(reason="currently unimplemented")
def test_invalid_image():
    args = ['scraper.py', 'filter1.txt', '']
    main(args)

    assert not isfile('output.csv')

# When no users are produced as result of filter, thus no file needs to be produced
@pytest.mark.skip(reason="currently unimplemented")
def test_empty_by_filter():
    args = ['scraper.py', 'filter2.txt', 'tests/sample4']
    main(args)

    assert not isfile('output.csv')

@pytest.mark.skip(reason="currently unimplemented")
def test_standard():
    args = ['scraper.py', 'filter1.txt', 'tests/sample4']
    main(args)

    assert isfile('output.csv')
    with open('output.csv', 'r') as f:
        output = f.read()
    
    # TODO: Insert full expected file contents
    assert output == ''' '''

    