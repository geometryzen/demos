from browser import window

msg = window.SpeechSynthesisUtterance('Hello GeometryZen!')
window.speechSynthesis.speak(msg)
