Student #:  0954174
Name:       Miriam Snow
Date:       Nov 8, 2019
Assignment: CIS 4150 Lab 4


-----------------------------------------------------------------------------------------

Question One:

The tes_subtractNumbers() function does not get processed by pytest because all functions used by pytest must start with test_

Since this creates an error for my first target in my makefile, I have added another target that fixes this issue so that all tests run
The target to run test_subtractNumbers() is called targ1.1, the target to run tes_subtractNumbers() is called targ1


------------------------------------------------------------------------------------------

Question Two: 

The markers and maxfail commands do not work because pytest is looking for files that start with test_
