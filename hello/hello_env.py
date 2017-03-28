import sys
import os

print os.getenv('PYTHON_HOME')
print os.environ.get('PYTHON_HOME')
print os.environ.__dict__.get('PYTHON_HOME')


print os.path.abspath(__file__)
print os.path.abspath('.')
print sys.argv[0]
print os.path.abspath(os.path.dirname('.'))
print os.path.dirname(os.path.abspath(__file__))
print 'PaTh' in os.environ
