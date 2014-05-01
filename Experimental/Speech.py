from browser import window

Utterance = window.SpeechSynthesisUtterance

msg = window.SpeechSynthesisUtterance('Hello World')
window.speechSynthesis.speak(msg);
