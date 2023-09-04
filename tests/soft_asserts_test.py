import logging

from nrt_unittest_soft_asserts.soft_asserts import SoftAsserts


message = None


class SoftAssertsTests(SoftAsserts):

    ERROR_MESSAGE_1 = 'Error message 1'

    STEP_1 = 'Step 1'
    STEP_2 = 'Step 2'
    STEP_3 = 'Step 3'

    is_init_failure_steps = True

    def setUp(self) -> None:
        self.unset_step()
        self.unset_logger()
        self.unset_print_method()
        self.soft_assert_all()

        if self.is_init_failure_steps:
            self.init_failure_steps()

    def test_soft_assert_true(self):
        assert self.soft_assert_true(True)
        assert self.soft_assert_true(True, self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_false(self):
        assert self.soft_assert_false(False)
        assert self.soft_assert_false(False, self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_equal(self):
        assert self.soft_assert_equal(1, 1)
        assert self.soft_assert_equal('a', 'a', self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_not_equal(self):
        assert self.soft_assert_not_equal(1, 2)
        assert self.soft_assert_not_equal('a', 'b', self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_is(self):
        assert self.soft_assert_is(1, 1)
        assert self.soft_assert_is('a', 'a', self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_is_not(self):
        assert self.soft_assert_is_not(1, 2)
        assert self.soft_assert_is_not('a', 'b', self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_is_none(self):
        assert self.soft_assert_is_none(None)
        assert self.soft_assert_is_none(None, self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_is_not_none(self):
        assert self.soft_assert_is_not_none(1)
        assert self.soft_assert_is_not_none('a', self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_in(self):
        assert self.soft_assert_in(1, [1, 2, 3])
        assert self.soft_assert_in('a', ['a', 'b', 'c'], self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_not_in(self):
        assert self.soft_assert_not_in(1, [2, 3, 4])
        assert self.soft_assert_not_in('a', ['b', 'c', 'd'], self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_is_instance(self):
        assert self.soft_assert_is_instance(1, int)
        assert self.soft_assert_is_instance('a', str, self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_not_is_instance(self):
        assert self.soft_assert_not_is_instance(1, str)
        assert self.soft_assert_not_is_instance('a', int, self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_almost_equal(self):
        assert self.soft_assert_almost_equal(1.0, 1.1, 0.15)
        assert self.soft_assert_almost_equal(
            1.01, 1.02, 0.015, self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_not_almost_equal(self):
        assert self.soft_assert_not_almost_equal(1.0, 1.2, 0.1)
        assert self.soft_assert_not_almost_equal(
            1.01, 1.02, 0.001, self.ERROR_MESSAGE_1)
        self.soft_assert_all()

    def test_soft_assert_raises(self):
        assert self.soft_assert_raises(ValueError, self.__raise_value_error)
        self.soft_assert_all()

    def test_soft_assert_raises_with(self):
        with self.soft_assert_raises_with(ValueError):
            _ = int('a')

        with self.soft_assert_raises_with(ValueError, self.ERROR_MESSAGE_1):
            _ = int('a')

        self.soft_assert_all()

    def test_soft_assert_true_fail(self):
        assert not self.soft_assert_true(False)
        assert len(self.failures) == 1
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_false_fail(self):
        assert not self.soft_assert_false(True)
        assert len(self.failures) == 1
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_equal_fail(self):
        assert not self.soft_assert_equal(1, 2)
        assert not self.soft_assert_equal('a', 'b', self.ERROR_MESSAGE_1)
        self.soft_assert_equal(1, 1)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_not_equal_fail(self):
        assert not self.soft_assert_not_equal(1, 1)
        assert not self.soft_assert_not_equal('a', 'a', self.ERROR_MESSAGE_1)
        self.soft_assert_not_equal(1, 2)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_is_fail(self):
        assert not self.soft_assert_is(1, 2)
        assert not self.soft_assert_is('a', 'b', self.ERROR_MESSAGE_1)
        assert self.soft_assert_is(1, 1)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_is_not_fail(self):
        assert not self.soft_assert_is_not(1, 1)
        assert not self.soft_assert_is_not('a', 'a', self.ERROR_MESSAGE_1)
        assert self.soft_assert_is_not(1, 2)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_is_none_fail(self):
        assert not self.soft_assert_is_none(1)
        assert not self.soft_assert_is_none('a', self.ERROR_MESSAGE_1)
        assert self.soft_assert_is_none(None)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_is_not_none_fail(self):
        assert not self.soft_assert_is_not_none(None)
        assert not self.soft_assert_is_not_none(None, self.ERROR_MESSAGE_1)
        assert self.soft_assert_is_not_none(1)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_in_fail(self):
        assert not self.soft_assert_in(1, [2, 3, 4])
        assert not self.soft_assert_in('a', ['b', 'c', 'd'], self.ERROR_MESSAGE_1)
        assert self.soft_assert_in(1, [1, 2, 3])
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_not_in_fail(self):
        assert not self.soft_assert_not_in(1, [1, 2, 3])
        assert not self.soft_assert_not_in('a', ['a', 'b', 'c'], self.ERROR_MESSAGE_1)
        assert self.soft_assert_not_in(1, [2, 3, 4])
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_is_instance_fail(self):
        assert not self.soft_assert_is_instance(1, str)
        assert not self.soft_assert_is_instance('a', int, self.ERROR_MESSAGE_1)
        assert self.soft_assert_is_instance(1, int)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_not_is_instance_fail(self):
        assert not self.soft_assert_not_is_instance(1, int)
        assert not self.soft_assert_not_is_instance('a', str, self.ERROR_MESSAGE_1)
        assert self.soft_assert_not_is_instance(1, str)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_almost_equal_fail(self):
        assert not self.soft_assert_almost_equal(1.0, 1.2, 0.1)
        assert not self.soft_assert_almost_equal(
            1.01, 1.02, 0.001, self.ERROR_MESSAGE_1)
        assert self.soft_assert_almost_equal(1.0, 1.1, 0.15)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_not_almost_equal_fail(self):
        assert not self.soft_assert_not_almost_equal(1.0, 1.1, 0.15)
        assert not self.soft_assert_not_almost_equal(
            1.01, 1.02, 0.015, self.ERROR_MESSAGE_1)
        assert self.soft_assert_not_almost_equal(1.0, 1.2, 0.1)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_raises_fail(self):
        assert not self.soft_assert_raises(ValueError, self.__not_raise_exception)
        assert not self.soft_assert_raises(TypeError, self.__raise_value_error)
        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_soft_assert_raises_with_fail(self):
        with self.soft_assert_raises_with(ValueError):
            _ = 1

        with self.soft_assert_raises_with(ConnectionError, self.ERROR_MESSAGE_1):
            self.__raise_value_error()

        assert len(self.failures) == 2
        self.__verify_assert_all_raised_exception()

    def test_fail_with_print_message(self):
        self.set_print_method(self.__print_message)
        self.soft_assert_true(False, self.ERROR_MESSAGE_1)
        assert message == f'False is not true : {self.ERROR_MESSAGE_1}'
        self.__verify_assert_all_raised_exception()

    def test_fail_with_logger(self):
        logger = logging.getLogger('test')
        self.set_logger(logger)
        self.soft_assert_true(False, self.ERROR_MESSAGE_1)
        self.__verify_assert_all_raised_exception()

    def test_fail_with_logger_and_print_message_negative(self):
        logger = logging.getLogger('test')
        self.set_logger(logger)
        self.set_print_method(self.__print_message)

        try:
            self.soft_assert_true(False, self.ERROR_MESSAGE_1)
            assert False
        except ValueError as e:
            assert e.args[0] == 'Cannot set both logger and print_method'

        with self.assertRaises(AssertionError):
            self.soft_assert_all()

    def test_steps_01(self):
        self.set_step(self.STEP_1)
        self.soft_assert_true(True, self.ERROR_MESSAGE_1)
        self.set_step(self.STEP_2)
        self.soft_assert_true(False, self.ERROR_MESSAGE_1)
        self.set_step(self.STEP_3)
        self.soft_assert_true(False, self.ERROR_MESSAGE_1)

        assert len(self.failures) == 2

        with self.assertRaises(AssertionError):
            self.soft_assert_all()

        assert not self.is_step_in_failure_steps(self.STEP_1)
        assert self.is_step_in_failure_steps(self.STEP_2)
        assert self.is_step_in_failure_steps(self.STEP_3)

        SoftAssertsTests.is_init_failure_steps = False

    def test_steps_02(self):

        assert not self.is_step_in_failure_steps(self.STEP_1)
        assert self.is_step_in_failure_steps(self.STEP_2)
        assert self.is_step_in_failure_steps(self.STEP_3)

        SoftAssertsTests.is_init_failure_steps = True

        self.init_failure_steps()

        assert not self.is_step_in_failure_steps(self.STEP_2)
        assert not self.is_step_in_failure_steps(self.STEP_3)

    def test_unset_step(self):
        self.set_step(self.STEP_1)
        self.unset_step()

        self.soft_assert_true(False, self.ERROR_MESSAGE_1)

        self.set_step(self.STEP_2)

        self.soft_assert_true(False)

        with self.assertRaises(AssertionError):
            self.soft_assert_all()

        assert not self.is_step_in_failure_steps(self.STEP_1)
        assert self.is_step_in_failure_steps(self.STEP_2)

    def test_step_not_exist_after_assert_all(self):
        self.set_step(self.STEP_1)
        self.soft_assert_true(False, self.ERROR_MESSAGE_1)

        with self.assertRaises(AssertionError):
            self.soft_assert_all()

        assert self.is_step_in_failure_steps(self.STEP_1)

        self.init_failure_steps()
        self.soft_assert_true(False, self.ERROR_MESSAGE_1)

        with self.assertRaises(AssertionError):
            self.soft_assert_all()

        assert not self.is_step_in_failure_steps(self.STEP_1)

    def test_step_not_in_failure_steps_before_assert_all(self):
        self.set_step(self.STEP_1)
        self.soft_assert_true(False, self.ERROR_MESSAGE_1)

        assert not self.is_step_in_failure_steps(self.STEP_1)

        with self.assertRaises(AssertionError):
            self.soft_assert_all()

        assert self.is_step_in_failure_steps(self.STEP_1)

    def __verify_assert_all_raised_exception(self):
        try:
            self.soft_assert_all()
        except AssertionError:
            return

        raise AssertionError('assert_all() did not raise AssertionError')

    def __print_message(self, msg):
        global message
        message = msg

    @classmethod
    def __raise_value_error(cls):
        raise ValueError('Value error')

    @classmethod
    def __not_raise_exception(cls):
        return
