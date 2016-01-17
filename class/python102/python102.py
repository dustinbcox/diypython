from __future__ import print_function

import argparse
import urllib

#class Calc(object):
#    def __init__(self, start_value):
#        self._total = start_value
#
#    def add(self, numbers):
#        for number in numbers:
#            self._total += number
#        return self._total
#
#    def sub(self, numbers):
#        for number in numbers:
#            self._total -= number
#        return self._total

class Web(object):
    """this is actually __doc__"""
    def get(self, url):
        """do inline documentation"""
        response = urllib.urlopen(url)
        data = response.read()
        import pdb; pdb.set_trace()
        print ("response is:", response)
        print ("data is:", data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Welcome to python102")
    parser.add_argument('--debug', action = "store_true", help = "Let's add some debug")
#    parser.add_argument('i', type = int, help = "Initial Value")
#    parser.add_argument('n', nargs='+', type = int, help = "Integeres")
#    group = parser.add_mutually_exclusive_group()
#    group.add_argument('--add', action = "store_true", help = "Add integers")
#    group.add_argument('--sub', action = "store_true", help = "Subtract integers")

    # Web scrape
    parser.add_argument("--web", help = "Grab a page and return the output")

    args = parser.parse_args()
    if args.debug:
        print(args)
        print("Exit for now")
        exit()

    if args.web is not None:
        web = Web()
        web.get(args.web)

#    calc = Calc(args.i)
#    if args.add:
#        print (calc.add(args.n))
#    elif args.sub:
#        print (calc.sub(args.n))
#    else:
#        print ("Nothing")

