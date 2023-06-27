def test_arithmetic():
	assert 1 == 1
	assert 2*3 == 6
	
def test_len_list():
	lst = ['a', 'b', 'c']
	assert len(lst) == 3
	
def test_sum():
	assert 1 + 2 == 3
	
from math import isclose
import numpy as np
from numpy.testing import assert_array_equal
	
def test_sumdecimals():
	assert isclose(1.1 + 2.2 , 3.3)
	assert isclose(1.1 + 2.2 , 3.3, abs_tol = 0.01 )

def test_numpy():
	x = np.array([1, 1])
	y = np.array([2, 2]) 
	z = np.array([3, 3])
	
	assert_array_equal(x + y, z)
