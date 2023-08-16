"""
def calcule(a,b):
    return a+b
"""

import sys
sys.path.append("D:\a\tutoMLops\tutoMLops\src")
from app import calcule

def test_calcul():
    assert int(calcule( 2,3)) == 5 


print(test_calcul())
print(calcule( 2 , 3))