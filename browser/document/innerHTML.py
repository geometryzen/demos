from browser import document

# Hint: The magic number GUID is the id for the pre element used for printer output.
pre = document.getElementById('a5f435e0-c92e-11e2-8b8b-0800200c9a66')
pre.innerHTML = '''
<h1>Hello!</h1>
'''
