import sensors_main
import unittest
import sys # needed for setting the command line parameters for test cases
from unittest.mock import patch # needed for the integration test case

# Unit tests implemented with Python's built-in unittest need to be classes,
# so here we use TestSensors class for the tests.
class TestSensors(unittest.TestCase):
    ###################
    # Unit test cases #
    ###################

    # Test case test_check_limits1 (UT1) that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # Test case test_check_limits2 (UT2) that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect.
    def test_check_limits2(self):
        pass
        # TODO: implement the actual test case code
    
    # TODO: Implement Test case test_check_limits3 (UT3) according to your
    # plan here. 

    ##########################
    # Integration test cases #
    ##########################

    # TODO: Complete test case test_check_limits_integration1 code so
    # that tests the check_limits function from main function.

    # NOTE: Redirect console output to sys.stdout in order to check it
    # from the test cases (here, from the integration test case). Also, use
    # mock_print as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        pass
        # 1. set command line parameters, since they are where main gets the
        # min and max temperature settings

        # 2. call main with the command line parameters set up

        # 3. check that the console output is the expected error message

        # 4. If you want to see what is in mock_print, you can use the following
        # (requires that there is import sys (as this module has) because this
        # test case sets the command line arguments that are in sys.argv)
        #
        # sys.stdout.write(str(mock_print.call_args) + "\n")
        # sys.stdout.write(str(mock_print.call_args_list) + "\n")

if __name__ == '__main__':
    unittest.main()
