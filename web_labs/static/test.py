
import re
import sys
from io import StringIO
import contextlib

    






@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def codingSummitMain():
   
    __codeWithAssertions = r'''
__code = r"""
print('')
# Write you code here
a=1
b=7
c=8
c=a+b
try:
    if 5 !=0:
        print('>> ' + str(c=a+b))
    else:
        print('>> ')
except:
    print('>> ')
print('\#\#\#\#\#')
"""


__assertions = ['a==1\r\n', '\r\nb==7\r\n', '\r\nc==8\r\n', "\r\nre.search(r'c[ ]*=[ ]*a[ ]*[+][ ]*b', __code)!=None"]


__new_code = __code
for assertion in __assertions:
    __new_code +=f'\r\nprint({assertion},sep="\#\#\#")'

exec(__new_code)

'''


    
    
    exec(__codeWithAssertions)

if __name__ == '__main__':
    with stdoutIO() as s:
        try:
            codingSummitMain()
        except Exception as e:
            print(e)
    print(s.getvalue())
