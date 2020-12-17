import unittest
import os
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()

loader = unittest.defaultTestLoader

cases=loader.discover(os.getcwd()+"\\testcase",pattern="Test*.py")
suite.addTest(cases)

with open("email/计算器测试报告.html", "w+", encoding="utf-8") as f:
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=f,
        verbosity=1,
        title="计算器测试报告",
        description="这是第三次迭代测试"
    )
    runner.run(suite)


