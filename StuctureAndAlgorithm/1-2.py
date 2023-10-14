"""
    需要从某个可迭代对象中分解N个元素，但是这个可迭代对象的长度可能超过N，这个导致出现“分解的值过多的异常”
    * 表达式
"""
from audioop import avg

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 5)
]


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


if __name__ == "__main__":
    record = ('dave', 'dave@qq.com', '12345678', '432153344556')
    name, email, *phone_numbers = record
    print(phone_numbers)
    print("=========================================================")
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)
    print("==========================================================")
    line = 'mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/false'
    uname, *fields = line.split(':')
    print(uname)
    print("===========================================================")
    uname, *_ = line.split(':')  # 省略后面的参数
    print(uname)
