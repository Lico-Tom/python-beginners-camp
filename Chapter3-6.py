import logging


class Spam:
    def __init__(self, name):
        self.name = name


import weakref

_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


if __name__ == '__main__':
    foo = logging.getLogger('foo')
    bar = logging.getLogger('bar')
    print(foo is bar)
    foo1 = logging.getLogger('foo')
    print(foo is foo1)
    foot = get_spam('foot')
    bart = get_spam('bart')
    print(foot is bart)
    foot1 = get_spam('foot')
    print(foot is foot1)
