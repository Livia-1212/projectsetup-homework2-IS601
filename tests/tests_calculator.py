'''My Calculator Test'''
import sys
from calculator import add, subtract
sys.path.append('/Users/liviali/Documents/NJIT/' +
                'Fall_2024/WebSystemDev_IS601853/GitHubHomework/' +
                'Projects2/myproject')

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
