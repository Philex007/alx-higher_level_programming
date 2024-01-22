100-safe_print_integer_err.py
#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
