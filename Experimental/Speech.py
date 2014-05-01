from browser import window

msg = window.SpeechSynthesisUtterance('Hello Geometry Zen!')
window.speechSynthesis.speak(msg)

for voice in window.speechSynthesis.getVoices():
    print voice.name
    
msg = window.SpeechSynthesisUtterance()
voices = window.speechSynthesis.getVoices()
msg.voice = voices[1]
msg.voiceURI = 'native'
msg.volume = 1 # 0 to 1
msg.rate = 1 # 0.1 to 10
msg.pitch = 2 # 0 to 2
msg.text = 'Hello World'
msg.lang = 'en-US'

#msg.onend = function(e) {
#  console.log('Finished in ' + event.elapsedTime + ' seconds.');
#};
window.speechSynthesis.speak(msg)
