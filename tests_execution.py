from nrt_unittest_soft_asserts.test.tests_suite import TestsSuite

test_suite = TestsSuite(True)
test_suite.run_tests()
test_suite.create_report()
test_suite.erase_data()
