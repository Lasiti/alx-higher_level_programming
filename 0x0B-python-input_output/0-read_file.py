#!/usr/bin/python3
'''A module containing IO functions.
'''


def read_file(filename=""):
    '''Reads a UTF-8 encoded text file and prints it to stdout.
    Args:
        filename (str): The name of the file to read.
    '''
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            print(line, end='')
