#! python3
# Opens all files inside a folder and searches for any line that matches an input from user

import os, sys


def readfile(file, filename, exists):
    output = ''
    try:
        for line in file:
            if search in line:
                exists = True
                output += '     ' + line.strip() + '\n'
        output = output.rstrip()
    except:
        pass
    if output != '':
        print('\033[94m Directory: ' + filename+ '\033[0m')
        print(output.replace(search, '\033[1m ' + search + '\033[0m'))
    return exists


if len(sys.argv) > 3:
    print('Too many arguments. "[filename.py] [search string] [path]"')
elif len(sys.argv) < 3:
    print('Too few arguments. "[filename.py] [search string] [path]"')
else:
    search = sys.argv[1]
    path = sys.argv[2]
    exists = False
    for subdir, dirs, files in os.walk(path):
        for file in files:
            fullfilename = subdir + os.sep + file
            try:
                fileread = open(fullfilename, 'r')
            except:
                pass
            exists = readfile(fileread, fullfilename, exists)

    if not exists:
        print('No hits')
        print('Remember - the string parameter is case sensitive')
