from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected.')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


class LazyConnection_1:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()


class Date:
    __slots__ = ['year', 'month', 'day']  # 主要当成简单的数据结构的类而言，通过添加__slots__属性来极大的减少实例所占的内存

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class A:
    def __init__(self):
        self._internal = 0  # 一个内部属性
        self.public = 1  # 一个公共属性

    def public_method(self):  # 一个公共方法
        pass

    def _internal_method(self):
        pass


class B:
    def __init__(self):  # 重命名的目的是：这种属性通过继承是无法被覆盖的
        self.__private = 0  # 私有属性会被重命名为_B__private

    def __private_method(self):  # 私有属性会被重命名为 _B__private_method()
        pass

    def public_method(self):
        pass
        self.__private_method()


class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class Person_1:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("Can't delete attribute.")

    name = property(get_first_name, set_first_name, del_first_name)


class C:
    def spam(self):
        print('a.spam')


class D(C):
    def spam(self):
        print('b.spam')
        super().spam()


class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, item):
        print('Getting ' + str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('Keys must be strings')
        return super().__setitem__(key, value)


class LoggerDice(LoggedMappingMixin, dict):
    pass


from collections import defaultdict


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


if __name__ == '__main__':
    conn = LazyConnection(('www.baidu.com', 80))
    with conn as s:
        s.send(b'GET /index/html HTTP/1.0\r\n')
    p = Person('Guido')
    print(p.first_name)
    p = Person_1('Guido')
    print(p.get_first_name())
    p.set_first_name = 44
    d = D()
    d.spam()
