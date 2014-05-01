from browser import window

msg = window.SpeechSynthesisUtterance('Hello Geometry Zen!')
window.speechSynthesis.speak(msg)

print type(window.speechSyntheses.getVoices())
print map(window.speechSynthesis.getVoices(), lambda voice: (voice.name))