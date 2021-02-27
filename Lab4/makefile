PYTHON=python -m pytest -v
FILE=test_functions.py::

all: targ1.1 targ2 targ3 targ4 targ5

targ1: 
	$(PYTHON) $(FILE)test_addNumbers $(FILE)test_productNumbers $(FILE)test_addStrings $(FILE)test_productStrings $(FILE)tes_subtractNumbers $(FILE)test_skip

targ1.1: 
	$(PYTHON) $(FILE)test_addNumbers $(FILE)test_productNumbers $(FILE)test_addStrings $(FILE)test_productStrings $(FILE)test_subtractNumbers $(FILE)test_skip
    
targ2: 
	$(PYTHON) $(FILE)test_productNumbers
    
targ3: 
	$(PYTHON) -m strings
    
targ4: 
	$(PYTHON) -m numbers
    
targ5:
	$(PYTHON) --maxfail=2