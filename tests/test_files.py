from scraper import get_files
import pytest

# Using sample1 folder, which just contains images
@pytest.mark.skip(reason="currently unimplemented")
def test_standard():
    # Check imports work
    content = get_files('tests/sample1')
    assert content != None
    assert len(content) == 3

    # For each file in folder
    fileList = ['fileA.jpg', 'fileB.png', 'fileC.png']
    for count, fname in enumerate(fileList):
        
        # Check file names are
        pname = 'tests/sample1/' + fname
        with open(pname, 'r') as f:
            assert content[count] == f.read()

# A folder with a single file on it should work
@pytest.mark.skip(reason="currently unimplemented")
def test_individual_file():
    fname = 'tests/sample2/fileD.jpeg'
    content = get_files(fname)
    assert len(content) == 1

    with open(fname, 'r') as f:
        assert content[0] == f.read()

# Just inputting a single file should be fine
@pytest.mark.skip(reason="currently unimplemented")
def test_single_file():
    content = get_files('tests/sample2')
    assert len(content) == 1
    
    with open('tests/sample2/fileD.png', 'r') as f:
        assert content[0] == f.read()

# If any of the files are not an image, then it should raise an error
@pytest.mark.skip(reason="currently unimplemented")
def test_invalid_file_folder():
    with pytest.raises(Exception):
        get_files('tests/sample3')

@pytest.mark.skip(reason="currently unimplemented")
def test_invalid_file():
    with pytest.raises(Exception):
        get_files('tests/test_command_line.py')

# While technically doesn't cause problems, is a valid error for the user end
# TODO: Edit this test to create a tmp folder, which will be empty
# def test_empty():
#     with pytest.raises(Exception):
#         get_files('emptyfolder')

# Path doesn't exist
@pytest.mark.skip(reason="currently unimplemented")
def test_bad_path():
    with pytest.raises(Exception):
        get_files('tests/notafolder')