from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

from AddComputerTest import AddComputerTest
from DeleteComputer import DeleteComputer
from SearchElements import SearchElements

addcoputertest = TestLoader().loadTestsFromTestCase(AddComputerTest)
search_test = TestLoader().loadTestsFromTestCase(SearchElements)
delete_element = TestLoader().loadTestsFromTestCase(DeleteComputer)

suite_test = TestSuite([search_test, addcoputertest])

kwargs={
    "output":'Suite-Test-report'

}

runner = HTMLTestRunner(**kwargs)
runner.run(suite_test)