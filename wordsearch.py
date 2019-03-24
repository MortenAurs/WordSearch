#! python3
# Opens all files inside a folder and searches for any line that matches an input from user

import os, sys

os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607
bold = '\033[1m'
white = '\033[0m'
blue = '\033[94m'


def readfile(file, filename, exists):
    output = ''
    try:

        for line in file:
            if search in line:
                exists = True
                output = line.replace(search, bold + search + white)

                print(blue + filename, ' ', white + output.strip())

    except:
        pass
    return exists


if len(sys.argv) > 3:
    print('Too many arguments. "[filename.py] [search string] [path]"')
elif len(sys.argv) < 3:
    print('Too few arguments. "[filename.py] [search string] [path]"')
else:

    search = sys.argv[1]
    path = sys.argv[2]
    if os.path.exists(path):
        exists = False
        for subdir, dirs, files in os.walk(path):
            for file in files:
                fullfilename = subdir + os.sep + file
                fileread = ''
                try:

                    fileread = open(fullfilename, 'r')
                except:
                    pass
                exists = readfile(fileread, fullfilename, exists)

        if not exists:
            print('No hits')
            print('Remember - the string parameter is case sensitive')
    else:
        print('Path does not exist')