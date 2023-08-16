"""
def calcule(a,b):

    return a+b
"""

import sys
sys.path.append("C:\Users\msi\tutoMLops\src\app")
from app import calcule

def test_calcul():
    assert int(calcule( 2,3)) == 5 


print(test_calcul())
print(calcule( 2 , 3))