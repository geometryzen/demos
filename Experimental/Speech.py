from browser import window
import sys

sys.debug()
msg = window.SpeechSynthesisUtterance('Hello Geometry Zen!')
window.speechSynthesis.speak(msg)

for voice in window.speechSynthesis.getVoices():
    print voice.name
    
msg = window.SpeechSynthesisUtterance()
voices = window.speechSynthesis.getVoices()
msg.voice = voices[4]
msg.voiceURI = 'native'
msg.volume = 1 # 0 to 1
msg.rate = 1 # 0.1 to 10
msg.pitch = 2 # 0 to 2
msg.text = 'Bonjour Geometry Zen!'
msg.lang = 'fr'

#def onEndHandler(event):
#    print 'Finished in ' + str(event.elapsedTime) + ' seconds.'
    
#msg.onend = onEndHandler
    
window.speechSynthesis.speak(msg)
