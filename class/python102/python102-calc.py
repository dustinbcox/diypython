from __future__ import print_function

import argparse
import urllib


"""Output

$ python python102-calc.py --help
usage: python102-calc.py [-h] [--debug] [--add | --sub] i n [n ...]

Welcome to python102

positional arguments:
  i           Initial Value
  n           Integers

optional arguments:
  -h, --help  show this help message and exit
  --debug     Let's add some debug
  --add       Add integers
  --sub       Subtract integers
Dustins-MBP-2:diypython dcox$ python python102-calc.py --add 2 3 4 5
14
Dustins-MBP-2:diypython dcox$ python python102-calc.py --sub 2 3 4 5
-10
Dustins-MBP-2:diypython dcox$ python python102-calc.py --sub 20 3 4 5
8
"""




class Calc(object):
    def __init__(self, start_value):
        self._total = start_value

    def add(self, numbers):
        for number in numbers:
            self._total += number
        return self._total

    def sub(self, numbers):
        for number in numbers:
            self._total -= number
        return self._total


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Welcome to python102")
    parser.add_argument('--debug', action = "store_true", help = "Let's add some debug")
    parser.add_argument('i', type = int, help = "Initial Value")
    parser.add_argument('n', nargs='+', type = int, help = "Integers")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--add', action = "store_true", help = "Add integers")
    group.add_argument('--sub', action = "store_true", help = "Subtract integers")

    args = parser.parse_args()
    if args.debug:
        print(args)
        print("Exit for now")
        exit()

    calc = Calc(args.i)
    if args.add:
        print (calc.add(args.n))
    elif args.sub:
        print (calc.sub(args.n))
    else:
        print ("Nothing")

