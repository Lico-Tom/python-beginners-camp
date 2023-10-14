import re
from urllib.request import urlopen

line = 'asd,ksfks;wer,jgkdsd'


def split_example_0():
    new_line = re.split(r'[;,\s]\s*', line)
    print(new_line)


def split_example_1():
    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)


def split_example_2():
    fields = re.split(r'(;|,|\s)\s*', line)
    values = fields[::2]
    print(values)
    delimiters = fields[1::2] + ['']
    print(delimiters)


def split_example_3():
    values = re.split(r'(?:,|;|\s)\s*', line)
    print(values)


def startswith_example_0():
    filename = "spam.txt"
    print(filename.startswith('.txt'))
    print(filename.startswith('spam'))


def endswith_example_1():
    filenames = ('mackefile', 'foo.c', 'spam.c', 'bar.py')
    python_file = [name for name in filenames if name.endswith('.py')]
    print(python_file)


def startswith_example_1(name):
    if name.startswith({'http', 'https', 'ftp'}):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


def slice_example_0():
    url = "https://baidu.com"
    res = re.match('http:|https:|ftp:', url)
    print(res)


from fnmatch import fnmatch, fnmatchcase


def fnmatch_example_0():
    fn = fnmatch('foo.txt', '*.txt')
    print(fn)


def fnmatch_example_1():
    names = ['Dat4s.csv', 'Dat2.txt', 'dat3.txt', 'Dat5.txt']
    fn_names = [name for name in names if fnmatch(name, 'Dat*.txt')]
    print(fn_names)


def fnmatchcase_example_0():
    boo = fnmatchcase('foo.txt', '.Txt')
    print(boo)


def fnmatchcase_example_1():
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    fn_case_addr = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
    print(fn_case_addr)
    fn_case_addr1 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
    print(fn_case_addr1)


def str_find_example_0():
    text = 'yeah, but no, but yeah, but no, but yeah'
    tx = text.find('no')
    print(tx)
    rtx = text.rfind('no')
    print(rtx)


def datepat_example_0():
    text = '11/27/2012'
    dated = re.compile(r'\d+/\d+/\d+')
    if dated.match(text):
        print('yes')
    else:
        print('no')
    date = dated.findall(text)
    print(date)


def text_group_example_0():
    text = '11/27/2012'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match(text)
    print(m.group(1))


def text_iter_example_0():
    text = '11/27/2012'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    for m in datepat.finditer(text):
        print(m.groups())


def text_findall_example_0():
    text = 'APPER PYTHON, lower python, Mixed Python'
    print(re.findall('python', text, re.IGNORECASE))  # 默认区分大小写


def text_sub_example_0():
    text = 'APPER PYTHON, lower python, Mixed Python'
    print(re.sub('python', 'snake', text, re.IGNORECASE))


def text_short_match_example_0():
    text = 'Computer says "no."'
    str_pat = re.compile(r'"(.*)"')
    print(str_pat.findall(text))


import unicodedata


def unicodedate_example_0():
    t1 = unicodedata.normalize('NFC', 'Spicy Jalape\u00f1o')
    t2 = unicodedata.normalize('NFC', 'Spicy Jalapen\u0303o')
    print(t1 == t2)


def text_just_example_0():
    text = 'Hello World'
    print(text.ljust(20, "="))
    print(text.rjust(20, '='))
    print(text.center(20, '='))


def text_format_example_0():
    text = 'Hello World'
    print(format(text, '>20'))
    print(format(text, '<20'))
    numb = 1.234
    print(format(numb, '^10.2f'))


def iter_join_example_0():
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    str = ' '.join(parts)
    print(str)


def text_format_example_0():
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))


if __name__ == "__main__":
    split_example_0()
    split_example_1()
    split_example_2()
    split_example_3()
    startswith_example_0()
    endswith_example_1()
    slice_example_0()
    fnmatch_example_0()
    fnmatch_example_1()
    fnmatchcase_example_0()
    fnmatchcase_example_1()
    str_find_example_0()
    datepat_example_0()
    text_group_example_0()
    text_iter_example_0()
    text_findall_example_0()
    text_sub_example_0()
    text_short_match_example_0()
    unicodedate_example_0()
    text_just_example_0()
    text_format_example_0()
    iter_join_example_0()
    text_format_example_0()
