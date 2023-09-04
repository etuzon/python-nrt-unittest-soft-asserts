import functools
import logging

from nrt_unittest_soft_asserts.soft_asserts import SoftAsserts


def skip_steps(skip_steps_list: list[str]):
    def decorator(test_method):
        @functools.wraps(test_method)
        def wrapper(self, *args, **kwargs):
            for step in skip_steps_list:
                if self.is_step_in_failure_steps(step):
                    self.skipTest(f'Skipped because step [{step}] failed.')
            return test_method(self, *args, **kwargs)

        return wrapper

    return decorator


def raise_value_error():
    raise ValueError('ValueError raised')


class SoftAssertsExamples1Tests(SoftAsserts):
    STEP_1 = 'step 1'
    STEP_2 = 'step 2'
    STEP_3 = 'step 3'

    logger = logging.getLogger('test')

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.set_logger(cls.logger)

    def test_soft_assert_true(self):
        self.soft_assert_true(True)

    def test_01_assert_with_steps_test_will_fail(self):
        self.set_step(self.STEP_1)
        # result is False because assert_true failed
        result = self.soft_assert_true(False)
        self.logger.info(f'result: {result}')

        self.set_step(self.STEP_2)
        self.soft_assert_true(False)

        # From this code section steps will not be attached to failure asserts
        self.unset_step()
        self.soft_assert_true(False)

        self.soft_assert_all()

    @skip_steps([STEP_1])
    def test_02_skip_if_step_1_fail(self):
        self.logger.error('Test should be skipped')
        self.soft_assert_true(False)
        self.soft_assert_all()

    @skip_steps([STEP_2])
    def test_03_skip_if_step_2_fail(self):
        self.logger.error('Test should be skipped')
        self.soft_assert_true(False)
        self.soft_assert_all()

    @skip_steps([STEP_1, STEP_2])
    def test_04_skip_if_step_1_or_step2_fail(self):
        self.logger.error('Test should be skipped')
        self.soft_assert_true(False)
        self.soft_assert_all()

    @skip_steps([STEP_3])
    def test_05_skip_if_step_3_fail(self):
        self.logger.error('Test should not be skipped')
        self.soft_assert_true(True)
        self.soft_assert_all()
