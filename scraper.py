import cv2
import sys

# Input is restricted to either a single file or folder
def get_files(path: str):
    return

def img_to_data(files: list):
    return

# Expected output is just a list of strings
def get_filters(path: str):
    return

# There should be a scheme to this, so best to find the pattern
def translate_names(data: list, filter: list):
    return

def filter_names(data: list, filter: list):
    return

def check_output(data: list):
    return

def write_output(data: list):
    return

def main(args: list):
    # command-line args
    print("hello world")

    # Get file path
    # Preferrably get as a array of files, to handle batch uploads
    get_files()
    # Get contents, image or whatever file

    # Process file, get into contents into array
    # This is the core of the program, and will likely be the majority of the work
    # pair (name, score)
    img_to_data()

    # Additional processing to fit the guild
    #  Stuff where the truncated names will be translated to full
    #  Checks to compare what names showed up
    #  Filtering of what names check for - ensuring this is an opt-in system
    check_output()

    # Open output file
    # Mabye can automate filename
    #  202X-Week-X, kind of folder
    #  or maybe just YYYY-MM-DD, monday to the sunday
    # write in csv format
    write_output()

if __name__ == '__main__':
    main(sys.argv)