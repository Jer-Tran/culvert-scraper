from scraper import get_files
import pytest
import cv2

testPath = 'tests/'

# Using sample1 folder, which just contains images
def test_standard():
    # Check imports work
    content = get_files(testPath + 'sample1')
    assert content != None
    assert len(content) == 3

    # For each file in folder
    fileList = ['fileA.jpg', 'fileB.png', 'fileC.png']
    for count, fname in enumerate(fileList):
        
        # Check file names are
        pname = testPath + 'sample1/' + fname
        img = cv2.imread(pname, cv2.IMREAD_GRAYSCALE)
        assert content[count].all() == img.all() # Needs the .all() property to compare that the same image is being read properly

# Just inputting a single file should be fine
def test_individual_file():
    fname = testPath + 'sample2/fileD.jpeg'
    content = get_files(fname)
    assert len(content) == 1

    img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    assert content[0].all() == img.all()

# A folder with a single file on it should work
def test_single_file():
    content = get_files(testPath + 'sample2')
    assert len(content) == 1
    
    img = cv2.imread(testPath + 'sample2/fileD.jpeg', cv2.IMREAD_GRAYSCALE)
    assert content[0].all() == img.all()

# If any of the files are not an image, then it should raise an error
def test_invalid_file_folder():
    with pytest.raises(Exception):
        get_files(testPath + 'sample3')

def test_invalid_file():
    with pytest.raises(Exception):
        get_files(testPath + 'test_files.py')

# While technically doesn't cause problems, is a valid error for the user end
# TODO: Edit this test to create a tmp folder, which will be empty
# def test_empty():
#     with pytest.raises(Exception):
#         get_files('emptyfolder')

# Path doesn't exist
def test_bad_path():
    
    with pytest.raises(Exception):
        get_files('culvert-scraper/tests/notafolder')
