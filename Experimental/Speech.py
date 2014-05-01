from browser import window

msg = window.SpeechSynthesisUtterance('Hello Geometry Zen!')
window.speechSynthesis.speak(msg)

for voice in window.speechSynthesis.getVoices():
    print voice.name
    
msg = window.SpeechSynthesisUtterance()
window.speechSynthesis.speak(msg)
