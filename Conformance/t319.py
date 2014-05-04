import sys
x = {}
x['a'] = 1
print x.get('a')
sys.debug()
print x.get('b')
print type(x.get('a'))
print type(x.get('b'))
