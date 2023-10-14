import fileinput
import sys


def fileinput_0():
    with fileinput.input() as f_input:
        for line in f_input:
            print(line, end='')


def fileinput_1():
    with fileinput.input('/etc/passwd') as f:
        for line in f:
            print(f.filename(), f.lineno(), line, end='')


def system_exit_0():
    sys.stderr.write('It failed!\n')
    raise SystemExit(1)


if __name__ == '__main__':
    system_exit_0()
