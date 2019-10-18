import pytest 

def test_test():
	assert 1==1, 'houston we have a problem'

def test_fail():
	assert 1==2, 'fail for testing documentation'
