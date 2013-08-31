import json

x = json.loads('{"name":"David", "height":1.8542}')

print x
print x['name']
print repr(x["name"])
print x['height']