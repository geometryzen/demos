from browser import window

msg = window.SpeechSynthesisUtterance('Hello Geometric Physics!')
window.speechSynthesis.speak(msg)
