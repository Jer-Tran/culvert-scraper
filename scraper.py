import cv2
import sys

def get_files():
    return

def img_to_data():
    return

def check_output():
    return

def write_output():
    return

def main(args):
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