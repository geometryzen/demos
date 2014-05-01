from browser import window

msg = window.SpeechSynthesisUtterance('Hello Geometry Zen!')
window.speechSynthesis.speak(msg)

print type(window.speechSynthesis.getVoices())
for voice in window.speechSynthesis.getVoices():
    print voice.name
#print map(window.speechSynthesis.getVoices(), lambda voice: (voice.name))