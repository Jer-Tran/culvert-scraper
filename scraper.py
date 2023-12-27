import cv2
import sys
import os

# Input is restricted to either a single file or folder
# In: str
# Out: list( file content )
def get_files(path: str):
    contents = []
    paths = []
    print("got in " + path)
    
    # Is a valid path check
    if not os.path.isfile(path) and not os.path.isdir(path):
        print("not found file")
        raise Exception("File not Found")

    # handling of dir and specified files differently
    if os.path.isdir(path):
        # Iteratively, only 1 depth for now, maybe do recursive later
        files = os.listdir(path)
        if files == []: raise Exception("Empty folder")
        for file in files:
            paths.append(path + '/' + file)

    else:
        paths.append(path)

    print("checking paths ")
    print(paths)

    # For each possible file, get their contents into an array
    for p in paths:
        img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
        
        # Happens when the file is not an image
        if img is None: raise Exception("Invalid file found")
        
        contents.append(img)

    return contents

# In: list(str)
# Out: list(str, int)
def img_to_data(files: list):
    return []

def valid_name(name: str):
    # Main thing is ensuring the file being read in uses utf-8 encoding
    # à á â ä å æ è é ê ë ì í î ï ò ó ô ö ø ù ú û ü ý ÿ, list of known valid chars
    if not name.isalnum():
        return False
    
    return True

# Expected output is just a list of strings
# In: str
# Out: list(str)
def get_filters(path: str):
    names = []
    print("Filter check now")
    # If path doesn't exist or file cannot be read, raise exception
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            names = content.split()
    except Exception as e:
        raise e

    # Basic check that all names are of fine format
    for name in names:
        # Need a better check so that it accepts accented characters
        if not valid_name(name):
            print("Name found which doesn't follow naming scheme: " + name)
            raise Exception("Invalid filter")

    names.sort()

    return names

# There should be a scheme to this, so best to find the pattern
# In: list(str, int), list(str)
# Out: list(str, int)
def translate_names(data: list, filter: list):
    return []

# In: list(str, int), list(str)
# Out: list(str, int)
def filter_names(data: list, filter: list):
    return []

# In: list(str, int)
# Out: list(str, int)
def check_output(data: list): 
    return []

# In: list(str, int)
# Out: Bool
def write_output(data: list):
    with open ('output.csv', 'w', encoding='utf-8') as f:
        f.write("test,a,b,c")
    return True

def main(args: list):
    # command-line args
    print(args) # remove
    if len(args) == 3:
        imgPath = args[1]
        filterPath = args[2]
    else:
        print(f"Usage: {args[0]} <content file> <list of names>")
        return False

    # Get file path
    # Preferrably get as a array of files, to handle batch uploads

    # Try to get one, if it fails, switch params around, and if fails again, then paths are invalid
    print("Checkpoint A") # remove
    try:
        fileContent = get_files(imgPath)
        print("Got files 1")
    except Exception as e:
        try:
            imgPath, filterPath = filterPath, imgPath
            fileContent = get_files(imgPath)
        except Exception as e:
            print("Could not find stuff")
            return False

    print("Checkpoint B") # remove
    print(fileContent)

    # Get contents of filters now
    try:
        filterContent = get_filters(filterPath)
    except Exception as e:
        print(e)
        return False
    
    print("Checkpoint C") # remove
    print(filterContent)

    # Process file, get into contents into array
    # This is the core of the program, and will likely be the majority of the work
    # pair (name, score)
    # img_to_data()

    # Additional processing to fit the guild
    #  Stuff where the truncated names will be translated to full
    #  Checks to compare what names showed up
    #  Filtering of what names check for - ensuring this is an opt-in system
    # check_output()

    # Open output file
    # Mabye can automate filename
    #  202X-Week-X, kind of folder
    #  or maybe just YYYY-MM-DD, monday to the sunday
    # write in csv format
    write_output([])

    return True

if __name__ == '__main__':
    main(sys.argv)