"""Test rv file
"""
from rv import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-2-12"

def test():
	"""Tests the rv function in the rv class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert rv.rv() == "rv", "test failed"
	#assert rv.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
