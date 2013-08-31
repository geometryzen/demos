import json

x = json.parse('{"name":"David", "height":1.8542, "favorite":6, "male":true, "religion":null}')

print x
print x['name']
print repr(x["name"])
print x['height']
print type(x['height'])
print x['favorite']
print type(x['favorite'])

print json.stringify(x)

x = json.parse['["David",1.8542,true,null]']

print x