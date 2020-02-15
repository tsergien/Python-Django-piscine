#!/usr/bin/env python3

from local_lib import path

def f():
    d = path.Path('awesome_directory')
    d.mkdir_p()
    my_file = path.Path('awesome_directory/awesome_file').touch()
    my_file.write_bytes(b'Hey handsome')
    print(f'File content: {my_file.bytes().decode()}')


if __name__ == '__main__':
    f()


