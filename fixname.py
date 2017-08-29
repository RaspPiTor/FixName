import argparse
import os
import re

def fix(directory):
    for i in os.scandir(directory):
        if i.is_file():
            print(i.name, end=' ')
            with open(i.path, 'rb') as file:
                data = file.read(100)
                if data.startswith(b'\x89PNG'):
                    print('PNG', end=' ')
                    os.rename(i.path, i.path.rstrip('.png') + '.png')
                elif data.startswith(b'\xff\xd8\xff'):
                    print('JPG', end=' ')
                    os.rename(i.path, i.path.rstrip('.jpg') + '.jpg')
                elif data.startswith(b'\x1f\x8b\x08'):
                    print('GZIP', end=' ')
                    os.rename(i.path,
                              i.path.rstrip('.gzip').rstrip('.gz') + '.gzip')
                elif data.startswith(b'GIF'):
                    print('GIF', end=' ')
                    os.rename(i.path, i.path.rstrip('.gif') + '.gif')
                elif data.startswith(b'SQLite format 3'):
                    print('SQLite3', end=' ')
                    os.rename(i.path, i.path.rstrip('.db').rstrip('.sqlite3')
                              + '.sqlite3')
                elif data.startswith(b'<?xml'):
                    print('XML', end=' ')
                    os.rename(i.path, i.path.rstrip('.xml') + '.xml')
                elif data.lower().startswith(b'<!doctype html'):
                    print('HTML', end=' ')
                    os.rename(i.path,
                              i.path.rstrip('.html').rstrip('.htm') + '.html')
            print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Directory to fix files in')
    args = parser.parse_args()
    fix(args.directory) 
    

if __name__ == '__main__':
    main()
