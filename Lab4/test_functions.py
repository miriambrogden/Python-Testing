import functions
import pytest

@pytest.mark.numbers
def test_addNumbers():
    assert functions.add(2, 3) == 5
    
@pytest.mark.numbers
def test_productNumbers():
    assert functions.product(2, 3) == 6

def test_addNumbersFail():
    assert functions.add(2, 3) == 9

def test_productNumbersFail():
    assert functions.product(2, 3) == 9

@pytest.mark.strings
def test_addStrings():
    assert functions.add("Mary", "Lou") == "MaryLou"

@pytest.mark.strings
def test_productStrings():
    assert functions.product("Mary", 3) == "MaryMaryMary"

def tes_subtractNumbers():
    assert functions.subtract(6, 4) == 2
    
def test_skip():
    return

#fixed tes_SubtractNumbers() so that the makefile would execute. 
#run targ1 to use tes_SubstractNumbers()
#run targ1.1 to use test_SubtractNumbers()
def test_subtractNumbers():
    assert functions.subtract(6, 4) == 2


    


