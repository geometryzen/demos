import json

def givesNone():
    return

print "givesNone() => " + str(givesNone())

# Note: It's not possible to return 'undefined' and drop an attribute.
def replacer(key, value):
    if key == '':
        return value
    elif key == 'height':
        return value * 2
    elif key == 'favorite':
        return None
    else:
        return None

#x = json.parse('{"name":"David", "height":1.8542, "favorite":6, "male":true, "religion":null}')

#print type(replacer)

#print json.stringify(x)
#print json.stringify(x, None)
#print json.stringify(x, None, 5)
#print json.stringify(x, replacer, 5)

# This gives a TypeError 'function' does not support indexing
#x = json.parse['["David"]']
