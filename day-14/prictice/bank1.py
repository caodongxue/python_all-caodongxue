import unittest

from prictice.testbank2 import TestInquire
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

# 用测试集加载测试用例方法
# suite.addTest(TestInquire("testQuire"))
# suite.addTest(TestInquire("testQuire1"))
# suite.addTest(TestInquire("testQuire2"))

# 用加载器加载测试用例方法
loader = unittest.defaultTestLoader  # 获取加载器
cases = loader.discover("D:\\Users\\PycharmProjects\\day-14\\prictice",pattern="test*.py") #寻找匹配的用例
suite.addTest(cases)  # 添加到测试集里

f = open("银行查询.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream = f, # 将生成的报告写入到f文件里
    title = "银行查询的测试报告", # 报告的标题
    description = "这是银行查询功能的测试", # 报告的描述
    verbosity = 1, # 粗细粒度
)
# 运行器运行测试集
htmlrunner.run(suite)


