from browser import window

graph = window.JXG.JSXGraph

board = graph.initBoard("box",{"grid":True,"boundingbox":[-2,2,2,-2]})

board.create('axis', [[0.0,1.0], [1.0,1.3]], {"withLabel": True, "name": "x-axis", "label": {"offset": [280,130]}})
