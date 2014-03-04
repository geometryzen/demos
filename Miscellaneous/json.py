import json

# Note: It's not possible to return 'undefined' and drop an attribute.
def replacer(key, value):
    if key == '':
        return value
    elif key == 'height':
        return value * 100
    elif key == 'favorite':
        return None
    else:
        return value

x = json.parse('{"name":"David", "height":1.8542, "favorite":6, "male":true, "other":null}')

print json.stringify(x)
print json.stringify(x, None)
print json.stringify(x, None, 5)
print json.stringify(x, replacer, 5)

# This gives a TypeError 'function' does not support indexing
#x = json.parse['["David"]']
