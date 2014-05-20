from browser import window

canvas = window.document.getElementById( 'canvas' )

# Retrieve the WebGL context from the canvas
gl = canvas.getContext('webgl') or canvas.getContext('experimental-webgl')

# If the context doesn't exist, we don't have WebGL. Tears.
if (not gl):
    print "This is not the WebGL context you're looking for"

# Set the clearColor attribute
gl.clearColor( 0.82, 0.28, 0.35, 1.0 )

# Clear the color component of the screen buffer
gl.clear( gl.COLOR_BUFFER_BIT )