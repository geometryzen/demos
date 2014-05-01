from browser import window

Utterance = window.SpeechSynthesisUtterance

msg = Utterance('Hello World')
window.speechSynthesis.speak(msg);
