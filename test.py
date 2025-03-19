import sys
sys.path.append('./')
from sub import sub_number

def test_sub():
    assert(sub_number(10,5)) == 5