class TestResult(object):
    def __init__(self):
        self.error_count = 0
        self.run_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return '%d run, %d failed' % (self.run_count, self.error_count)

    def test_failed(self):
        self.error_count += 1


class TestCase(object):
    def __init__(self, method_name):
        self.method_name = method_name

    def run(self, result):
        result.test_started()
        # noinspection PyBroadException
        try:
            method = getattr(self, self.method_name)
            self.set_up()
            method()
        except Exception:
            result.test_failed()
        self.tear_down()
        return result

    def set_up(self):
        pass

    def tear_down(self):
        pass


class WasRun(TestCase):
    def __init__(self, method_name):
        super(WasRun, self).__init__(method_name)
        self.was_run = False
        self.log = ''

    def set_up(self):
        self.log += 'set_up '

    def tear_down(self):
        self.log += 'tear_down '

    # TODO do we need it ?
    def test_method(self):
        self.was_run = True
        self.log += 'test_method '

    def test_broken_method(self):
        raise Exception


class TestSuite(object):
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert 'set_up test_method tear_down ' == test.log

    def test_result(self):
        test = WasRun('test_method')
        result = test.run(self.result)
        assert '1 run, 0 failed' == result.summary()

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert '1 run, 1 failed' == result.summary(), '\'%s\'' % result.summary()

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run(self.result)
        assert '1 run, 1 failed' == result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)
        assert '2 run, 1 failed' == self.result.summary()


def main():
    suite = TestSuite()
    suite.add(TestCaseTest('test_template_method'))
    suite.add(TestCaseTest('test_result'))
    suite.add(TestCaseTest('test_failed_result_formatting'))
    suite.add(TestCaseTest('test_failed_result'))
    suite.add(TestCaseTest('test_suite'))

    result = TestResult()
    suite.run(result)
    print result.summary()


main()

