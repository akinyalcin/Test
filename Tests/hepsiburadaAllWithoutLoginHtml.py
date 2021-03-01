import unittest
import HtmlTestRunner
import  os
from Tests import hepsiburadaAllWithoutLogin

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Tests
hepsiburadaAllWithoutLogin_test = unittest.TestLoader().loadTestsFromTestCase(hepsiburadaAllWithoutLogin.HepsiburadaAllTest)

# create a test suite combining tests
test_suite = unittest.TestSuite([hepsiburadaAllWithoutLogin_test])

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile, report_title="Test Report")

# run the suite using HtmlTestRunner
runner.run(test_suite)