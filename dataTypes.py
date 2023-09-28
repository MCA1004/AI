# In python there are Different kind of data types define.

# String
# int, float, complex
# list, tuple, frozenset
# dict, set
# Range
# boolean

# Note : complex number always written with 'J'
# Note : complex number never be typecast.

""" String """
x = "Welcome in Python"

""" int, float, complex """
x = 10  # int
x = 10.5  # float
x = 1j  # complex
x = -4j + 5j  # complex

""" list, tuple, frozenset """
x = ["a", "b", "c"]  # list
x = ("a", "b", "c")  # tuple
x = {"a", "b", "c"}  # frozenset

""" dict, set """
x = dict(A="Welcome", B="Python", C=10)  # dict
x = set(("Welcome", "Python", "Programming"))  # set

""" Range """
x = range(10)

""" boolean """
x = bool(12)

import random
print(random.randrange(1,10))
