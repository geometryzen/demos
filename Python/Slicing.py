# Slicing.py
word = 'Help' + 'A'
print word
print word * 5
print word[4]
print word[0:2]
print word[2:4]
print word[:2] # omitting first index defaults to zero
print word[2:] # omitting second default to len(word)
print word[2:len(word)]
print word[:]
print 'x' + word[1:]
print word[1:100]
print word[10:0]
print word[-1] # counting from the right