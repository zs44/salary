from unittest.mock import patch
import salary
import sys

@patch('builtins.pront')
def test_salary(printtest):
    salary(10)
    printtest.assert_called_with('poor')
    salary(10000)
    printtest.assert_called_with('rich')

    sys.stdout.write(str(printtest.call_arg)+'\n')
    sys.stdout.write(str(printtest.call_arg_list)+'\n')
