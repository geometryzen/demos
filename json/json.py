import json

def replacer(key, value):
    print key
    print value
    return "pqr"

x = json.parse('{"name":"David", "height":1.8542, "favorite":6, "male":true, "religion":null}')

print json.stringify(x)
#print json.stringify(x, None)
#print json.stringify(x, None, 5)
print json.stringify(x, replacer, 5)

# This gives a TypeError 'function' does not support indexing
#x = json.parse['["David"]']
