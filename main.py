#! python3
# Opens all files inside a folder and searches for any line that matches an input from user

import os


print('Write the path to the directory:')
path = '/home/morten/Dropbox/App/' #input()

print('Type in the string you want to search for:')
search = input()


def readfile(file, filename):
    output = ''
    while file.readline():
        line = file.readline().strip()
        if search.upper() in line.upper():

            output += '     ' + line + '\n'
    output = output.rstrip()
    if output != '':
        print('Directory: ' + filename)
        print(output.replace(search.lower(), '\033[1m ' + search + '\033[0m'))


for subdir, dirs, files in os.walk(path):
    for file in files:
        fullfilename = subdir + os.sep + file
        fileread = open(fullfilename, 'r')
        if not fullfilename.endswith('.jpg') and not fullfilename.endswith('.pdf'):
            readfile(fileread, fullfilename)








