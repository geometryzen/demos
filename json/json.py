import json

x = json.loads('{"name":"David", "height":1.8542}', "favorite":6)

print x
print x['name']
print repr(x["name"])
print x['height']
print type(x['height'])