# RegExp.py
import re
s = 'aggatcgtaggcatgctgggcctatactggactc'
p = 'gga'
print re.findall(p,s)
#['gga', 'gga']

p = 'gg[a|g]'
print re.findall(p,s)
#['gga', 'ggg', 'gga']

p = 'gg.'
print re.findall(p,s)
#['gga', 'ggc', 'ggg', 'gga']