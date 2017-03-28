import subprocess
import sys
import logging

from exceptions import OSError


def execute_command(command):
    (code, out, err) = (-1, None, None)
    try:
        p = subprocess.Popen(command,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()
        code = p.wait()
        print '---------'
        print out
        print '---------'
        print err
        print '---------'
    except OSError as e:
        code = e.errno
        err = e.message
    except Exception as e:
        err = e.message
    return code, out, err


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s-%(levelname)s:%(name)s:%(message)s")
    cmd = 'cd'
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
    print execute_command(cmd)
