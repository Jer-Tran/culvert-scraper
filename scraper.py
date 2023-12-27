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
    data = [ ('a', 1), ('b', 10), ('c', 100) ] 
    return data

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

    names.sort()

    # TODO: After image processing step is done, verify that handling of accent names doesn't cause issues of dup data
    # Check that all names are of fine format and for duplicates
    prev = None
    for name in names:
        if not valid_name(name):
            print("Name found which doesn't follow naming scheme: " + name)
            raise Exception("Invalid filter")
        elif prev == name:
            raise Exception("Duplicates Clause - " + name)
        prev = name

    return names

# In: string, list( duple(str, int) )
# Out: int
def get_index(string: str, items: list):
    print(items)
    for index, item in enumerate(items):
        print(item)
        print(index)
        if string == item[0]:
            return index

    return -1

# In cases where there is a truncated name in data, tries best effort to extend it
# In: list(str, int), list(str)
# Out: list(str, int)
def translate_names(data: list, filter: list):
    content = data[:] # Avoids modifying original and needs a copy for later
    index = 0
    used = []
    while index < len(content):
        entry = content[index]
        name = entry[0]

        # If name has been truncated in-game
        if name[-2:] == "..": # So far, it's been constant that it truncates to a '..' at the end
            full_name = name
            tr_name = name[:-2]

            # Tries to find its full ver in filters
            for field in filter:
                # gi
                if len(field) > len(tr_name) and tr_name == field[:len(tr_name)]:
                    # If there are multiple matches, we default to not translating
                    if full_name != name:
                        full_name = name
                        break
                    full_name = field
            
            # Used list is for here, if we find another value that uses the same full value, revert old one
            if get_index(full_name, used) != -1:
                i = get_index(full_name, used)
                content[i] = tuple(data[i])
            else:
                content[index] = (full_name, entry[1])
                used.append((full_name, index))

        index += 1

    return content

# In: list(str, int), list(str)
# Out: list(str, int)
def filter_names(data: list, filter: list):
    content = data[:]
    result = []
    missed = []
    seen = []
    for item in content:
        # If name seen before, remove from final results if needed
        if item[0] in seen:
            index = get_index(item[0], result)
            # Handles 3+ cases of duplicate names
            if index != -1:
                dupe = result.pop(index)
                missed.append(dupe)
        # If name passes filter, is added to final result
        elif item[0] in filter:
            result.append(item)
            seen.append(item[0])
        

        if item not in result:
            missed.append(item)
    
    return result

# In: list(str, int)
# Out: list(str, int)
def check_output(data: list, filter: list): 
    tl_data = translate_names(data, filter)
    fl_data = filter_names(tl_data, filter)

    return fl_data

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
            print("[Error] File contents could not be found: " + e)
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
    data = img_to_data(fileContent)

    # Additional processing to fit the guild
    #  Stuff where the truncated names will be translated to full
    #  Checks to compare what names showed up
    #  Filtering of what names check for - ensuring this is an opt-in system
    try:
        data = check_output(data, filterContent)
    except Exception as e:
        print("[Error] " + e)
        return False
    
    if data == []:
        print("No data obtained")
        return False

    # Open output file
    # Mabye can automate filename
    #  202X-Week-X, kind of folder
    #  or maybe just YYYY-MM-DD, monday to the sunday
    # write in csv format
    write_output(data)

    return True

if __name__ == '__main__':
    main(sys.argv)