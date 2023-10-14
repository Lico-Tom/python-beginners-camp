import math


def round_example_0():
    print(round(1.23, 1))
    print(round(-1.27, 1))
    print(round(234563, -2))


def format_example_0():
    res = format(1.23456, '0.2f')
    print(res)


def format_example_1():
    res = format(1.23456, '>10.1f')
    print(res)


x = 1234


def bin_example_0():
    bin_res = bin(x)
    print(bin_res)
    print(format(x, 'b'))
    oct_res = oct(x)
    print(oct_res)
    print(format(x, 'o'))
    hex_res = hex(x)
    print(hex_res)
    print(format(x, 'x'))


def int_example_0():
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    res = int.from_bytes(data, 'little')
    print(res)


data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
import struct


def struct_example_0():
    hi, lo = struct.unpack('>QQ', data)
    print((hi << 64) + lo)


def complex_example_0():
    a = complex(2, 4)
    print(a)
    b = 3 - 5j
    print(b)
    print(a.real)
    print(a.imag)
    print(a.conjugate())
    print(a + b)
    print(a * b)
    print(a / b)
    print(abs(a))


import numpy as np


def numpy_example_0():
    a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
    print(a)
    print(a + 2)
    print(np.sin(a))
    print(np.cos(a))


def inf_nan_example_0():
    a = float('inf')  # 无穷大
    b = float('-inf')  # 负无穷小
    c = float('nan')  # 无穷小
    print(a)
    print(b)
    print(c)
    print(math.isinf(a))
    print(math.isnan(c))


from fractions import Fraction


def fractions_example_0():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(a + b)


def numpy_example_1():
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)
    print(m.T)
    print(m.I)


import random


def random_example_0():
    values = [1, 2, 3, 4, 5]
    print(random.choice(values))
    print(random.sample(values, 3))
    random.shuffle(values)
    print(values)


from datetime import timedelta, datetime, date


def datatime_example_0():
    a = timedelta(days=2, hours=4)
    print(a.days)
    print(datetime.now())


import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    print(start_date, end_date)


def str2date_example_0():
    text = '2012-09-20'
    print(datetime.strptime(text, '%Y-%m-%d'))


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class lazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


def lazyPropertyPro(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy()


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyProperty
    def perimeter(self):
        print('Computing perimeter')


class Structure1:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Structure2:  # 支持关键字参数， 可以将关键字参数设置为实例属性
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(self._fields))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args)]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalied argument(s): {}'.format(','.join(kwargs)))


class Structure3:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


class Stock1(Structure1):
    _fields = ['name', 'shares', 'price']


class Circle1(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    round_example_0()
    format_example_0()
    format_example_1()
    bin_example_0()
    int_example_0()
    struct_example_0()
    complex_example_0()
    inf_nan_example_0()
    fractions_example_0()
    numpy_example_1()
    random_example_0()
    datatime_example_0()
    get_month_range()
    str2date_example_0()
    p = Point(2, 4)
    print(p.x)
    print(p.y)
    c = Circle1(4.0)
    print(c.area)
    s2 = Stock1('ACME', 50, 30)
    print(s2.name)
    print(s2.shares)
