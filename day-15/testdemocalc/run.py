
import unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()

loader = unittest.defaultTestLoader
cases = loader.discover("/testdemocalc", pattern="Test*.py")
suite.addTest(cases)


f = open("计算器测试.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "计算器的测试报告",
    description = "这是计算器加减乘除功能的测试",
    verbosity = 1,
)

htmlrunner.run(suite)



