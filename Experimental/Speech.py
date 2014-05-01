from browser import window

msg = window.SpeechSynthesisUtterance('Hello World')
window.speechSynthesis.speak(msg)
