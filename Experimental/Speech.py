from browser import window

msg = window.SpeechSynthesisUtterance('Hello Geometry Zen!')
window.speechSynthesis.speak(msg)

print speechSynthesis.getVoices()