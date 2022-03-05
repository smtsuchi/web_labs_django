def makeRunCode(code, assertions=[]):
    import re as __re
    __printPattern = __re.compile('print[ ]?\([\w\W]*\)')
    __filter = lambda x:x.strip('\n\r\t ')
    out = f"""
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
__code = r\"\"\"
print('')
{code}
try:
    if {len(code.splitlines())} !=0:
        print('>> ' + str({'' if len(code.splitlines()) == 0 or __printPattern.search(code.splitlines()[-1]) else list(filter(__filter,code.splitlines()))[-1]}))
    else:
        print('>> ')
except:
    print('>> ')
print('\#\#\#\#\#')
\"\"\"


__assertions = {assertions}


__new_code = __code
for assertion in __assertions:
    __new_code +=f'\\r\\nprint({{assertion}},sep="\#\#\#")'

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
"""
    return out