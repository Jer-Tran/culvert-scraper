from scraper import get_files, img_to_data
import pytest

# TODO: Fill in the test asserts with appropraite expected output once images are made

# Handling a single file that fits format
@pytest.mark.skip(reason="currently unimplemented")
def test_standard():
    content = get_files('tests/sample4/example.PNG')
    output = img_to_data(content)

    assert output == []

# Handling of multiple files
@pytest.mark.skip(reason="currently unimplemented")
def test_multiple():
    content = get_files('tests/sample5')
    output = img_to_data(content)

    assert output == []

# Handling of multiple files, with some data overlapping
@pytest.mark.skip(reason="currently unimplemented")
def test_multiple_overlap():
    content = get_files('tests/sample6')
    output = img_to_data(content)

    assert output == []

# Where the contents of one image are just a subset of another
@pytest.mark.skip(reason="currently unimplemented")
def test_multiple_subset():
    content = get_files('tests/sample7')
    outA = img_to_data(content)

    content = get_files('test/sample6/major.png')
    outB = img_to_data(content)

    assert outA == outB

# This set of tests require the making of images, which I am not bothered to consider at the moment
# # In a case where image is edited but important content is not obscured
# def test_edited_image():
#     fname = 'tbd'
#     content = get_files(fname)
#     output = img_to_data(content)

#     assert output == [('data', 'set')]

# # In a case where image is edited such that important content is obscured, should raise error
# def test_corrupted_image():
#     fname = 'tbd'
#     content = get_files(fname)

#     with pytest.raises(Exception):
#         img_to_data(content)

# # If the image includes the head of the table, should be ignored
# def test_include_headers():
#     # Row looks like Name, Job, Level, Title, WeeklyMission, Culvert, Flag Race
#     # The pair would look like (Name, Culvert), but probably raise an error in trying to interpret the number
#     fname = 'tbd'
#     content = get_files(fname)
#     output = img_to_data(content)

#     assert output == [('data', 'set')]

# If image does not suit format, e.g. random image, then error should be thrown
@pytest.mark.skip(reason="currently unimplemented")
def test_invalid_img():
    fname = 'tests/sample2'
    content = get_files(fname)
    with pytest.raises(Exception):
        img_to_data(content)

# Empty list as input, would never happen, but should be handled
@pytest.mark.skip(reason="currently unimplemented")
def test_no_inputs():
    empty_list = []
    with pytest.raises(Exception):
        img_to_data(empty_list)