import sensors_main
import unittest
from unittest.mock import patch # needed for the example integration test case
import sys # needed for setting the command line parameters for test cases

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):
    ###############################
    # Examples of unit test cases #
    ###############################

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # The test case test_check_limits2 that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect.
    def test_check_limits2(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

    # The test case test_check_limits3 that tests the check_limits
    # with incorrect inputs that are equal (lower limit 18 and higher
    # limit 18) and expects the method to return False, since the
    # limits are incorrect. 
    def test_check_limits3(self):
        limits = [18, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

    #######################################
    # Example of an integration test case #
    #######################################

    # The test case test_check_limits_integration1 that tests
    # the check_limits from main.

    # Redirect console output to sys.stdout in order to
    # check it from the test cases (here, from the example
    # integration test case). Notice the use of mock_print
    # as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [22], [18]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

        # If you want to see what is in mock_print, you can use the following
        # (requires that there is import sys as this module has because this
        # test case sets the command line arguments that are in sys.argv)
        #
        # sys.stdout.write(str(mock_print.call_args) + "\n")
        # sys.stdout.write(str(mock_print.call_args_list) + "\n")

if __name__ == '__main__':
    unittest.main()