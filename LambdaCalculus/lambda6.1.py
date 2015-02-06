#!/usr/bin/env python3.4

"""Untyped Lambda Calculus"""

# "Understanding Computation: Impossible Code and the Meaning of Programs"
# Chapter 6.1 's Code. Use Python3.
# Authors: Chai Fei

# Python中没有类似Ruby的proc功能的函数，只能直接用lambda来实现

# 6.1.3 实现数字
ZERO = lambda p: lambda x: x
ONE = lambda p: lambda x: p(x)
TWO = lambda p: lambda x: p(p(x))
THREE = lambda p: lambda x: p(p(p(x)))
FIVE = lambda p: lambda x: p(p(p(p(p(x)))))
FIFTEEN = lambda p: lambda x: p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(x)))))))))))))))
# 一百层嵌套括号会导致Python解释器解析溢出错误，改用五十层
FIFTY = lambda p: lambda x: p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(x))))))))))))))))))))))))))))))))))))))))))))))))))
                                              
def to_integer(proc):
    return proc(lambda n: n + 1)(0)


# 6.1.4 实现布尔值
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

def to_boolean(proc):
    return proc(True)(False)


# 实现if语句
IF = lambda b: lambda x: lambda y: b(x)(y)

def to_boolean(proc):
    return IF(proc)(True)(False)


# if语句简化
IF = lambda b: b


# 6.1.5 实现谓词
IS_ZERO = lambda n: n(lambda x: FALSE)(TRUE)


# 6.1.6 有序对
PAIR = lambda x: lambda y: lambda f: f(x)(y)
LEFT = lambda p: p(lambda x: lambda y: x)
RIGHT = lambda p: p(lambda x: lambda y: y)


# 6.1.7 数值运算
INCREMENT = lambda n: lambda p: lambda x: p(n(p)(x))
SLIDE = lambda p: PAIR(RIGHT(p))(INCREMENT(RIGHT(p)))
DECREMENT = lambda n :LEFT(n(SLIDE)(PAIR(ZERO)(ZERO)))
ADD = lambda m: lambda n: n(INCREMENT)(m)
SUBTRACT = lambda m: lambda n: n(DECREMENT)(m)
MULTIPLY = lambda m: lambda n: n(ADD(m))(ZERO)
POWER = lambda m: lambda n: n(MULTIPLY(m))(ONE)


## UnitTest
import unittest

class TestLambda(unittest.TestCase):
    """ Tests of the books's code
    """
        
    def test_proc(self):
        self.assertEqual((lambda x: x + 2)(1), 3)
        self.assertEqual((lambda x:(lambda y: x + y))(3)(4), 7)
        p = lambda n: n * 2
        q = lambda x: p(x)
        self.assertEqual(p(5), 10)
        self.assertEqual(q(5), 10)

    def test_number(self):
        self.assertEqual(to_integer(ZERO), 0)
        self.assertEqual(to_integer(THREE), 3)
        self.assertEqual(to_integer(FIFTY), 50)

    def test_boolean(self):
        self.assertEqual(to_boolean(TRUE), True)
        self.assertEqual(to_boolean(FALSE), False)

    def test_if(self):
        self.assertEqual(IF(TRUE)('happy')('sad'), 'happy')
        self.assertEqual(IF(FALSE)('happy')('sad'), 'sad')

    def test_is_zero(self):
        self.assertEqual(to_boolean(IS_ZERO(ZERO)), True)
        self.assertEqual(to_boolean(IS_ZERO(THREE)), False)

    def test_pair(self):
        my_pair = PAIR(THREE)(FIVE)
        self.assertEqual(to_integer(LEFT(my_pair)), 3)
        self.assertEqual(to_integer(RIGHT(my_pair)), 5)

    def test_calculation(self):
        self.assertEqual(to_integer(INCREMENT(FIVE)), 6)
        self.assertEqual(to_integer(DECREMENT(FIVE)), 4)
        self.assertEqual(to_integer(ADD(FIVE)(THREE)), 8)
        self.assertEqual(to_integer(SUBTRACT(FIVE)(THREE)), 2)
        self.assertEqual(to_integer(MULTIPLY(FIVE)(THREE)), 15)
        self.assertEqual(to_integer(POWER(THREE)(THREE)), 27)



if __name__ == '__main__':
    unittest.main()