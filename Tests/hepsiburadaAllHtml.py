import unittest
import HtmlTestRunner
import  os
from Tests import hepsiburadaAllTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Tests
hepsiburadaAll_test = unittest.TestLoader().loadTestsFromTestCase(hepsiburadaAllTest.HepsiburadaAllTest)

# create a test suite combining tests
test_suite = unittest.TestSuite([hepsiburadaAll_test])

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile, report_title="Test Report")

# run the suite using HtmlTestRunner
runner.run(test_suite)