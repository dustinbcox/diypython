from __future__ import print_function

""" Welcome to python 101 """

# Globals
a_list = ['one', 'two', 'three', True, False]
b_dict = {'one': 1, 'two': 2, 'three': 3, 'key': 'mike', 'key2': 4321}
c_tuple = (1, 2, 3)
d_foo = 123.12
e_string = "this is a string"
f_none = None
g_multiline_string = '''
this is a multiline
string'''


def say_hi():
    """This method will say hi"""
    print("Hi")

def example_dict_by_key():
    print('I want to say b_dict', b_dict)
    for thing in b_dict:
        print(type(thing), thing, "that was a key which it's value is", b_dict[thing])
    print (thing, type(thing))

def example_list_by_value():
    for index, thing in enumerate(a_list):
        print(index, thing)

def example_key_value_from_dict():
    for k,v in b_dict.iteritems():
        print("key:", k, "value:", v)

def do_things():
    """Method"""
    # Comments
    print("Hello world")
    for thing in (a_list, b_dict, c_tuple, d_foo, e_string, f_none, g_multiline_string):
        print(type(thing))
        print("value of thing", thing)
print("The name of this", __name__)
print("The filename is ", __file__)

if __name__ == "__main__": # running file directly
    #do_things()
    example_list_by_value()
    exit()
    example_dict_by_key()
    exit()
    internal_range = range(10)
    for i in internal_range: 
        say_hi()
