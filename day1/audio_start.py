# # Creating an audio file

# import google text to speech library
from gtts import gTTS

# process text to audio
text = gTTS("This is a message from Krishna Teja")

# write the file 
text.save('audio2.mp3')
