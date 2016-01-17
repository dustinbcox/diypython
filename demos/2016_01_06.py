#!/usr/bin/python

"""
Hello this is a file that was created on Jan 6, 2016 at golug.org Topic: Python Tricks and Tweaks

This demos some of the "meta" aspects of Python 3, python debugging with pdb and argument parsing

This file uses pacman on Arch Linux since that was the laptop I had while running this demo

"""

import subprocess
import argparse
import __main__
import dis
import inspect


class Foo(object):
    def __init__(self):
        pass
    def name(self):
        return 'foo'
    def bar(self):
        print('bar')


def packages():
    """Get packages on Arch using pacman"""
    pacman = subprocess.Popen(['/usr/bin/pacman', '-Q'], stdout = subprocess.PIPE)
    packages = pacman.communicate()[0]
    if packages is not None:
        packages = packages.splitlines()

    for package in packages:
        name, ver = package.decode('utf-8').split(' ')
        print ("Package name: {0} ver: {1}".format(name, ver))

def intro():
    """Print out the main docstring"""
    print(__main__.__doc__)

def something_special():
    """This is auto discovered by main"""
    print ("Something special")

def something_else_special():
    print("this is cool")

if __name__ == "__main__":
    """Do the main thing"""
    parser = argparse.ArgumentParser(description ='Hello this is the name of this thing')
    parser.add_argument('-p', '--packages', help = 'list packages on Arch', action = 'store_true')
    parser.add_argument('-i', '--intro', help = 'print out file docstring', action = 'store_true')
    parser.add_argument('-d', '--debug', help = 'break out the debugger', action = 'store_true')
    parser.add_argument('-f', '--foo', help = 'Do the foo thing', action = 'store_true')

    for method in [(m, getattr(__main__, m)) for m in dir() if m.startswith('something_') and callable(getattr(__main__, m))]:
        name = method[0]
        method_call = method[1]
        parser.add_argument('--' + name, help = "Some help for {0}".format(name), action= "store_true")

    args = parser.parse_args()
    if args.debug:
        import pdb
        pdb.set_trace()

    if args.packages:
        packages()
    elif args.intro:
        intro()
    elif args.foo:
        print(inspect.getsource(Foo))
        print(dis.dis(Foo))
        print(dir(Foo))

    #parser.print_help()
